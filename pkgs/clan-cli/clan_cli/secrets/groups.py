import argparse
import os
from pathlib import Path

from ..errors import ClanError
from ..machines.types import machine_name_type, validate_hostname
from ..types import FlakeName
from . import secrets
from .folders import (
    sops_groups_folder,
    sops_machines_folder,
    sops_secrets_folder,
    sops_users_folder,
)
from .sops import update_keys
from .types import (
    VALID_USER_NAME,
    group_name_type,
    secret_name_type,
    user_name_type,
)


def machines_folder(flake_name: FlakeName, group: str) -> Path:
    return sops_groups_folder(flake_name) / group / "machines"


def users_folder(flake_name: FlakeName, group: str) -> Path:
    return sops_groups_folder(flake_name) / group / "users"


class Group:
    def __init__(
        self, flake_name: FlakeName, name: str, machines: list[str], users: list[str]
    ) -> None:
        self.name = name
        self.machines = machines
        self.users = users
        self.flake_name = flake_name


def list_groups(flake_name: FlakeName) -> list[Group]:
    groups: list[Group] = []
    folder = sops_groups_folder(flake_name)
    if not folder.exists():
        return groups

    for name in os.listdir(folder):
        group_folder = folder / name
        if not group_folder.is_dir():
            continue
        machines_path = machines_folder(flake_name, name)
        machines = []
        if machines_path.is_dir():
            for f in machines_path.iterdir():
                if validate_hostname(f.name):
                    machines.append(f.name)
        users_path = users_folder(flake_name, name)
        users = []
        if users_path.is_dir():
            for f in users_path.iterdir():
                if VALID_USER_NAME.match(f.name):
                    users.append(f.name)
        groups.append(Group(flake_name, name, machines, users))
    return groups


def list_command(args: argparse.Namespace) -> None:
    for group in list_groups(args.flake):
        print(group.name)
        if group.machines:
            print("machines:")
            for machine in group.machines:
                print(f"  {machine}")
        if group.users:
            print("users:")
            for user in group.users:
                print(f"  {user}")
        print()


def list_directory(directory: Path) -> str:
    if not directory.exists():
        return f"{directory} does not exist"
    msg = f"\n{directory} contains:"
    for f in directory.iterdir():
        msg += f"\n  {f.name}"
    return msg


def update_group_keys(flake_name: FlakeName, group: str) -> None:
    for secret_ in secrets.list_secrets(flake_name):
        secret = sops_secrets_folder(flake_name) / secret_
        if (secret / "groups" / group).is_symlink():
            update_keys(
                secret,
                list(sorted(secrets.collect_keys_for_path(secret))),
            )


def add_member(
    flake_name: FlakeName, group_folder: Path, source_folder: Path, name: str
) -> None:
    source = source_folder / name
    if not source.exists():
        msg = f"{name} does not exist in {source_folder}: "
        msg += list_directory(source_folder)
        raise ClanError(msg)
    group_folder.mkdir(parents=True, exist_ok=True)
    user_target = group_folder / name
    if user_target.exists():
        if not user_target.is_symlink():
            raise ClanError(
                f"Cannot add user {name}. {user_target} exists but is not a symlink"
            )
        os.remove(user_target)
    user_target.symlink_to(os.path.relpath(source, user_target.parent))
    update_group_keys(flake_name, group_folder.parent.name)


def remove_member(flake_name: FlakeName, group_folder: Path, name: str) -> None:
    target = group_folder / name
    if not target.exists():
        msg = f"{name} does not exist in group in {group_folder}: "
        msg += list_directory(group_folder)
        raise ClanError(msg)
    os.remove(target)

    if len(os.listdir(group_folder)) > 0:
        update_group_keys(flake_name, group_folder.parent.name)

    if len(os.listdir(group_folder)) == 0:
        os.rmdir(group_folder)

    if len(os.listdir(group_folder.parent)) == 0:
        os.rmdir(group_folder.parent)


def add_user(flake_name: FlakeName, group: str, name: str) -> None:
    add_member(
        flake_name, users_folder(flake_name, group), sops_users_folder(flake_name), name
    )


def add_user_command(args: argparse.Namespace) -> None:
    add_user(args.flake, args.group, args.user)


def remove_user(flake_name: FlakeName, group: str, name: str) -> None:
    remove_member(flake_name, users_folder(flake_name, group), name)


def remove_user_command(args: argparse.Namespace) -> None:
    remove_user(args.flake, args.group, args.user)


def add_machine(flake_name: FlakeName, group: str, name: str) -> None:
    add_member(
        flake_name,
        machines_folder(flake_name, group),
        sops_machines_folder(flake_name),
        name,
    )


def add_machine_command(args: argparse.Namespace) -> None:
    add_machine(args.flake, args.group, args.machine)


def remove_machine(flake_name: FlakeName, group: str, name: str) -> None:
    remove_member(flake_name, machines_folder(flake_name, group), name)


def remove_machine_command(args: argparse.Namespace) -> None:
    remove_machine(args.flake, args.group, args.machine)


def add_group_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("group", help="the name of the secret", type=group_name_type)


def add_secret(flake_name: FlakeName, group: str, name: str) -> None:
    secrets.allow_member(
        secrets.groups_folder(flake_name, name), sops_groups_folder(flake_name), group
    )


def add_secret_command(args: argparse.Namespace) -> None:
    add_secret(args.flake, args.group, args.secret)


def remove_secret(flake_name: FlakeName, group: str, name: str) -> None:
    secrets.disallow_member(secrets.groups_folder(flake_name, name), group)


def remove_secret_command(args: argparse.Namespace) -> None:
    remove_secret(args.flake, args.group, args.secret)


def register_groups_parser(parser: argparse.ArgumentParser) -> None:
    subparser = parser.add_subparsers(
        title="command",
        description="the command to run",
        help="the command to run",
        required=True,
    )

    # List groups
    list_parser = subparser.add_parser("list", help="list groups")
    list_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    list_parser.set_defaults(func=list_command)

    # Add user
    add_machine_parser = subparser.add_parser(
        "add-machine", help="add a machine to group"
    )
    add_group_argument(add_machine_parser)
    add_machine_parser.add_argument(
        "machine", help="the name of the machines to add", type=machine_name_type
    )
    add_machine_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    add_machine_parser.set_defaults(func=add_machine_command)

    # Remove machine
    remove_machine_parser = subparser.add_parser(
        "remove-machine", help="remove a machine from group"
    )
    add_group_argument(remove_machine_parser)
    remove_machine_parser.add_argument(
        "machine", help="the name of the machines to remove", type=machine_name_type
    )
    remove_machine_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    remove_machine_parser.set_defaults(func=remove_machine_command)

    # Add user
    add_user_parser = subparser.add_parser("add-user", help="add a user to group")
    add_group_argument(add_user_parser)
    add_user_parser.add_argument(
        "user", help="the name of the user to add", type=user_name_type
    )
    add_user_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    add_user_parser.set_defaults(func=add_user_command)

    # Remove user
    remove_user_parser = subparser.add_parser(
        "remove-user", help="remove a user from group"
    )
    add_group_argument(remove_user_parser)
    remove_user_parser.add_argument(
        "user", help="the name of the user to remove", type=user_name_type
    )
    remove_user_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    remove_user_parser.set_defaults(func=remove_user_command)

    # Add secret
    add_secret_parser = subparser.add_parser(
        "add-secret", help="allow a user to access a secret"
    )
    add_secret_parser.add_argument(
        "group", help="the name of the user", type=group_name_type
    )
    add_secret_parser.add_argument(
        "secret", help="the name of the secret", type=secret_name_type
    )
    add_secret_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    add_secret_parser.set_defaults(func=add_secret_command)

    # Remove secret
    remove_secret_parser = subparser.add_parser(
        "remove-secret", help="remove a group's access to a secret"
    )
    remove_secret_parser.add_argument(
        "group", help="the name of the group", type=group_name_type
    )
    remove_secret_parser.add_argument(
        "secret", help="the name of the secret", type=secret_name_type
    )
    remove_secret_parser.add_argument(
        "flake",
        type=str,
        help="name of the flake to create machine for",
    )
    remove_secret_parser.set_defaults(func=remove_secret_command)
