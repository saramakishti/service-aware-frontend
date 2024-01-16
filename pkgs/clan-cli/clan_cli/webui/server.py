# Imports
import argparse
import logging
import multiprocessing as mp
import shutil
import subprocess
import time
import urllib.request
from contextlib import ExitStack, contextmanager
from pathlib import Path
from threading import Thread
from typing import Iterator

import uvicorn
from pydantic import AnyUrl, IPvAnyAddress
from pydantic.tools import parse_obj_as

import clan_cli.config as config
from clan_cli.emulate_fastapi import apps, get_health
from clan_cli.errors import ClanError

# Setting up logging
log = logging.getLogger(__name__)


# Function to open the browser for a specified URL
def open_browser(base_url: AnyUrl, sub_url: str) -> None:
    for i in range(5):
        try:
            urllib.request.urlopen(base_url + "/health")
            break
        except OSError:
            time.sleep(i)
    url = parse_obj_as(AnyUrl, f"{base_url}/{sub_url.removeprefix('/')}")
    _open_browser(url)


# Helper function to open a web browser for a given URL using available browsers
def _open_browser(url: AnyUrl) -> subprocess.Popen:
    for browser in ("firefox", "iceweasel", "iceape", "seamonkey"):
        if shutil.which(browser):
            # Do not add a new profile, as it will break in combination with
            # the -kiosk flag.
            cmd = [
                browser,
                "-kiosk",
                "-new-window",
                url,
            ]
            print(" ".join(cmd))
            return subprocess.Popen(cmd)
    for browser in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        if shutil.which(browser):
            return subprocess.Popen([browser, f"--app={url}"])
    raise ClanError("No browser found")


# Context manager to spawn the Node.js development server
@contextmanager
def spawn_node_dev_server(host: IPvAnyAddress, port: int) -> Iterator[None]:
    log.info("Starting node dev server...")
    path = Path(__file__).parent.parent.parent.parent / "ui"
    with subprocess.Popen(
        [
            "direnv",
            "exec",
            path,
            "npm",
            "run",
            "dev",
            "--",
            "--hostname",
            str(host),
            "--port",
            str(port),
        ],
        cwd=path,
    ) as proc:
        try:
            yield
        finally:
            proc.terminate()


# Main function to start the server
def start_server(args: argparse.Namespace) -> None:
    with ExitStack() as stack:
        headers: list[tuple[str, str]] = []
        if args.dev:
            stack.enter_context(spawn_node_dev_server(args.dev_host, args.dev_port))

            base_url = f"http://{args.dev_host}:{args.dev_port}"
            host = args.dev_host
            if ":" in host:
                host = f"[{host}]"
            headers = [
                # (
                #     "Access-Control-Allow-Origin",
                #     f"http://{host}:{args.dev_port}",
                # ),
                # (
                #     "Access-Control-Allow-Methods",
                #     "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
                # ),
                # (
                #     "Allow",
                #     "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
                # )
            ]
        else:
            base_url = f"http://{args.host}:{args.port}"

        if not args.no_open:
            Thread(target=open_browser, args=(base_url, args.sub_url)).start()

        # DELETE all data from the database
        from . import sql_models
        from .sql_db import engine

        sql_models.Base.metadata.drop_all(engine)

        if args.populate:
            # pre populate the server with some test data
            test_dir = Path(__file__).parent.parent.parent / "tests"

            if not test_dir.is_dir():
                raise ClanError(f"Could not find test dir: {test_dir}")

            test_db_api = test_dir / "test_db_api.py"
            if not test_db_api.is_file():
                raise ClanError(f"Could not find test db api: {test_db_api}")

            import subprocess

            cmd = ["pytest", "-s", str(test_db_api)]
            subprocess.run(cmd, check=True)

        config.host = args.host
        if args.emulate:
            # start servers as processes (dlg, ap, c1 and c2 for tests)
            for app, port in apps:
                proc = mp.Process(
                    target=uvicorn.run,
                    args=(app,),
                    kwargs={
                        "host": args.host,
                        "port": port,
                        "log_level": args.log_level,
                    },
                    daemon=True,
                )
                proc.start()
                url = f"http://{args.host}:{port}"
                res = get_health(url=url + "/health")
                if res is None:
                    raise Exception(f"Couldn't reach {url} after starting server")

        uvicorn.run(
            "clan_cli.webui.app:app",
            host=args.host,
            port=args.port,
            log_level=args.log_level,
            reload=args.reload,
            access_log=args.log_level == "debug",
            headers=headers,
        )
