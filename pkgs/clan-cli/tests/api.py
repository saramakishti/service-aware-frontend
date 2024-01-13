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

import config
from clan_cli.webui.app import app


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
    host = config.host
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
