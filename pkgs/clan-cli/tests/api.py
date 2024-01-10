import sys
import time
import urllib.request
from multiprocessing import Process
from typing import Generator
from urllib.error import URLError

import pytest
import uvicorn
from fastapi.testclient import TestClient
from openapi_client import ApiClient, Configuration
from ports import PortFunction

from clan_cli.webui.app import app

import emulate_fastapi


# TODO config file
#is linked to the emulate_fastapi.py and api.py
host = "127.0.0.1"
port_dlg = 6000
port_ap = 6600
port_client_base = 7000

@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)


def get_health(*, url: str, max_retries: int = 20, delay: float = 0.2) -> str | None:
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read()
        except URLError as e:
            print(f"Attempt {attempt + 1} failed: {e.reason}", file=sys.stderr)
            time.sleep(delay)
    return None


# Pytest fixture to run the server in a separate process
# server
@pytest.fixture(scope="session")
def server_url(unused_tcp_port: PortFunction) -> Generator[str, None, None]:
    port = unused_tcp_port()
    host = host
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": host, "port": port, "log_level": "info"},
        daemon=True,
    )
    proc.start()

    url = f"http://{host}:{port}"
    res = get_health(url=url + "/health")
    if res is None:
        raise Exception(f"Couldn't reach {url} after starting server")

    yield url
    proc.terminate()

# Pytest fixture to run the server in a separate process
# emulating c1
@pytest.fixture(scope="session")
def server_c1() -> Generator[str, None, None]:
    port = port_client_base
    host = host
    # server
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": host, "port": port, "log_level": "info"},
        daemon=True,
    )
    proc.start()

    url = f"http://{host}:{port}"
    res = get_health(url=url + "/health")
    if res is None:
        raise Exception(f"Couldn't reach {url} after starting server")

    yield url
    proc.terminate()

# Pytest fixture to run the server in a separate process
# emulating c2
@pytest.fixture(scope="session")
def server_c2() -> Generator[str, None, None]:
    port = port_client_base+1
    host = host
    # server
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": host, "port": port, "log_level": "info"},
        daemon=True,
    )
    proc.start()

    url = f"http://{host}:{port}"
    res = get_health(url=url + "/health")
    if res is None:
        raise Exception(f"Couldn't reach {url} after starting server")

    yield url
    proc.terminate()
    proc.terminate()

# Pytest fixture to run the server in a separate process
# emulating ap
@pytest.fixture(scope="session")
def server_ap() -> Generator[str, None, None]:
    port = port_ap
    host = host
    # server
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": host, "port": port, "log_level": "info"},
        daemon=True,
    )
    proc.start()

    url = f"http://{host}:{port}"
    res = get_health(url=url + "/health")
    if res is None:
        raise Exception(f"Couldn't reach {url} after starting server")

    yield url
    proc.terminate()

# Pytest fixture to run the server in a separate process
# emulating dlg
@pytest.fixture(scope="session")
def server_dlg() -> Generator[str, None, None]:
    port = port_dlg
    host = host
    # server
    proc = Process(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": host, "port": port, "log_level": "info"},
        daemon=True,
    )
    proc.start()

    url = f"http://{host}:{port}"
    res = get_health(url=url + "/health")
    if res is None:
        raise Exception(f"Couldn't reach {url} after starting server")

    yield url
    proc.terminate()

@pytest.fixture(scope="session")
def api_client(server_url: str) -> Generator[ApiClient, None, None]:
    configuration = Configuration(host=server_url)

    # Enter a context with an instance of the API client
    with ApiClient(configuration) as api_client:
        yield api_client
