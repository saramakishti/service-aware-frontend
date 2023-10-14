import json
import os
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import IO, Iterator

from ..dirs import user_config_dir
from ..errors import ClanError
from ..nix import nix_shell
from .folders import sops_machines_folder, sops_users_folder


class SopsKey:
    def __init__(self, pubkey: str, username: str) -> None:
        self.pubkey = pubkey
        self.username = username


def get_public_key(privkey: str) -> str:
    cmd = nix_shell(["age"], ["age-keygen", "-y"])
    try:
        res = subprocess.run(cmd, input=privkey, stdout=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        raise ClanError(
            "Failed to get public key for age private key. Is the key malformed?"
        ) from e
    return res.stdout.strip()


def generate_private_key() -> tuple[str, str]:
    cmd = nix_shell(["age"], ["age-keygen"])
    try:
        proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, text=True)
        res = proc.stdout.strip()
        pubkey = None
        private_key = None
        for line in res.splitlines():
            if line.startswith("# public key:"):
                pubkey = line.split(":")[1].strip()
            if not line.startswith("#"):
                private_key = line
        if not pubkey:
            raise ClanError("Could not find public key in age-keygen output")
        if not private_key:
            raise ClanError("Could not find private key in age-keygen output")
        return private_key, pubkey
    except subprocess.CalledProcessError as e:
        raise ClanError("Failed to generate private sops key") from e


def get_user_name(flake_name: str, user: str) -> str:
    """Ask the user for their name until a unique one is provided."""
    while True:
        name = input(
            f"Your key is not yet added to the repository. Enter your user name for which your sops key will be stored in the repository [default: {user}]: "
        )
        if name:
            user = name
        if not (sops_users_folder(flake_name) / user).exists():
            return user
        print(f"{sops_users_folder(flake_name) / user} already exists")


def ensure_user_or_machine(flake_name: str, pub_key: str) -> SopsKey:
    key = SopsKey(pub_key, username="")
    folders = [sops_users_folder(flake_name), sops_machines_folder(flake_name)]
    for folder in folders:
        if folder.exists():
            for user in folder.iterdir():
                if not (user / "key.json").exists():
                    continue

                if read_key(user) == pub_key:
                    key.username = user.name
                    return key

    raise ClanError(
        f"Your sops key is not yet added to the repository. Please add it with 'clan secrets users add youruser {pub_key}' (replace youruser with your user name)"
    )


def default_sops_key_path() -> Path:
    raw_path = os.environ.get("SOPS_AGE_KEY_FILE")
    if raw_path:
        return Path(raw_path)
    else:
        return user_config_dir() / "sops" / "age" / "keys.txt"


def ensure_sops_key(flake_name: str) -> SopsKey:
    key = os.environ.get("SOPS_AGE_KEY")
    if key:
        return ensure_user_or_machine(flake_name, get_public_key(key))
    path = default_sops_key_path()
    if path.exists():
        return ensure_user_or_machine(flake_name, get_public_key(path.read_text()))
    else:
        raise ClanError(
            "No sops key found. Please generate one with 'clan secrets key generate'."
        )


@contextmanager
def sops_manifest(keys: list[str]) -> Iterator[Path]:
    with NamedTemporaryFile(delete=False, mode="w") as manifest:
        json.dump(
            dict(creation_rules=[dict(key_groups=[dict(age=keys)])]), manifest, indent=2
        )
        manifest.flush()
        yield Path(manifest.name)


def update_keys(secret_path: Path, keys: list[str]) -> None:
    with sops_manifest(keys) as manifest:
        cmd = nix_shell(
            ["sops"],
            [
                "sops",
                "--config",
                str(manifest),
                "updatekeys",
                "--yes",
                str(secret_path / "secret"),
            ],
        )
        res = subprocess.run(cmd)
        if res.returncode != 0:
            raise ClanError(
                f"Failed to update keys for {secret_path}: sops exited with {res.returncode}"
            )


def encrypt_file(
    secret_path: Path, content: IO[str] | str | None, keys: list[str]
) -> None:
    folder = secret_path.parent
    folder.mkdir(parents=True, exist_ok=True)

    with sops_manifest(keys) as manifest:
        if not content:
            args = ["sops", "--config", str(manifest)]
            args.extend([str(secret_path)])
            cmd = nix_shell(["sops"], args)
            p = subprocess.run(cmd)
            # returns 200 if the file is changed
            if p.returncode != 0 and p.returncode != 200:
                raise ClanError(
                    f"Failed to encrypt {secret_path}: sops exited with {p.returncode}"
                )
            return

        # hopefully /tmp is written to an in-memory file to avoid leaking secrets
        with NamedTemporaryFile(delete=False) as f:
            try:
                with open(f.name, "w") as fd:
                    if isinstance(content, str):
                        fd.write(content)
                    else:
                        shutil.copyfileobj(content, fd)
                # we pass an empty manifest to pick up existing configuration of the user
                args = ["sops", "--config", str(manifest)]
                args.extend(["-i", "--encrypt", str(f.name)])
                cmd = nix_shell(["sops"], args)
                subprocess.run(cmd, check=True)
                # atomic copy of the encrypted file
                with NamedTemporaryFile(dir=folder, delete=False) as f2:
                    shutil.copyfile(f.name, f2.name)
                    os.rename(f2.name, secret_path)
            finally:
                try:
                    os.remove(f.name)
                except OSError:
                    pass


def decrypt_file(secret_path: Path) -> str:
    with sops_manifest([]) as manifest:
        cmd = nix_shell(
            ["sops"], ["sops", "--config", str(manifest), "--decrypt", str(secret_path)]
        )
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise ClanError(
            f"Failed to decrypt {secret_path}: sops exited with {res.returncode}"
        )
    return res.stdout


def write_key(path: Path, publickey: str, overwrite: bool) -> None:
    path.mkdir(parents=True, exist_ok=True)
    try:
        flags = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
        if not overwrite:
            flags |= os.O_EXCL
        fd = os.open(path / "key.json", flags)
    except FileExistsError:
        raise ClanError(f"{path.name} already exists in {path}")
    with os.fdopen(fd, "w") as f:
        json.dump({"publickey": publickey, "type": "age"}, f, indent=2)


def read_key(path: Path) -> str:
    with open(path / "key.json") as f:
        try:
            key = json.load(f)
        except json.JSONDecodeError as e:
            raise ClanError(f"Failed to decode {path.name}: {e}")
    if key["type"] != "age":
        raise ClanError(
            f"{path.name} is not an age key but {key['type']}. This is not supported"
        )
    publickey = key.get("publickey")
    if not publickey:
        raise ClanError(f"{path.name} does not contain a public key")
    return publickey
