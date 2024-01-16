# Importing necessary modules and packages
import sys
import time
import urllib
from datetime import datetime

# Importing FastAPI and related components
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

# Importing configuration and schemas from the clan_cli package
import clan_cli.config as config
from clan_cli.webui.schemas import Resolution

# Creating FastAPI instances for different applications
app_dlg = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
app_ap = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
app_c1 = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
app_c2 = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

# List of FastAPI instances and their associated ports
apps = [
    (app_dlg, config.port_dlg),
    (app_ap, config.port_ap),
    (app_c1, config.c1_port),
    (app_c2, config.c2_port),
]


# Healthcheck endpoints for different applications
@app_c1.get("/")
async def root_c1() -> str:
    return "C1 is alive"


@app_c1.get("/health")
async def healthcheck_c1() -> str:
    return "200 OK"


@app_c2.get("/")
async def root_c2() -> str:
    return "C2 is alive"


@app_c2.get("/health")
async def healthcheck_c2() -> str:
    return "200 OK"


@app_dlg.get("/")
async def root_dlg() -> str:
    return "DLG is alive"


@app_dlg.get("/health")
async def healthcheck_dlg() -> str:
    return "200 OK"


@app_ap.get("/")
async def root_ap() -> str:
    return "AP is alive"


@app_ap.get("/health")
async def healthcheck_ap() -> str:
    return "200 OK"


# Function for performing health checks on a given URL with retries
def get_health(*, url: str, max_retries: int = 20, delay: float = 0.2) -> str | None:
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(url) as response:  # type: ignore
                return response.read()
        except urllib.error.URLError as e:  # type: ignore
            print(f"Attempt {attempt + 1} failed: {e.reason}", file=sys.stderr)
            time.sleep(delay)
    return None


# Service consumption emulation for c1 which returns a gif1
@app_c1.get("/v1/print_daemon1", response_class=HTMLResponse)
async def consume_service_from_other_entity_c1() -> HTMLResponse:
    # HTML content for the response
    html_content = """
    <html>
        <body>
            <div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/IOWD3uknMxYyh7CsgN/video" width="480"></iframe></div>
        </body>
    </html>
    """
    time.sleep(3)
    return HTMLResponse(content=html_content, status_code=200)


@app_c1.get("/v1/print_daemon1/register", response_class=JSONResponse)
async def register_c1() -> JSONResponse:
    return JSONResponse(content={"status": "registered"}, status_code=200)


@app_c1.get("/v1/print_daemon1/deregister", response_class=JSONResponse)
async def deregister_c1() -> JSONResponse:
    return JSONResponse(content={"status": "deregistered"}, status_code=200)


@app_c2.get("/v1/print_daemon2", response_class=HTMLResponse)
async def consume_service_from_other_entity_c2() -> HTMLResponse:
    # Similar HTML content for the response
    html_content = """
    <html>
        <body>
            <div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/IOWD3uknMxYyh7CsgN/video" width="480"></iframe></div>
        </body>
    </html>
    """
    time.sleep(3)
    return HTMLResponse(content=html_content, status_code=200)


@app_c2.get("/v1/print_daemon1/register", response_class=JSONResponse)
async def register_c2() -> JSONResponse:
    return JSONResponse(content={"status": "registered"}, status_code=200)


@app_c2.get("/v1/print_daemon1/deregister", response_class=JSONResponse)
async def deregister_c2() -> JSONResponse:
    return JSONResponse(content={"status": "deregistered"}, status_code=200)


@app_ap.get("/ap_list_of_services", response_class=JSONResponse)
async def ap_list_of_services() -> JSONResponse:
    # Sample list of services as a JSON response
    res = [
        # Service 1
        {
            "uuid": "bdd640fb-0667-1ad1-1c80-317fa3b1799d",
            "service_name": "Carlos Printing0",
            "service_type": "3D Printing",
            "endpoint_url": "http://127.0.0.1:8000/v1/print_daemon0",
            "other": {},
            "entity_did": "did:sov:test:120",
            "status": {"data": ["draft", "registered"]},
            "action": {
                "data": [
                    {
                        "name": "register",
                        "endpoint": "http://127.0.0.1:8000/v1/print_daemon0/register",
                    },
                    {
                        "name": "deregister",
                        "endpoint": "http://127.0.0.1:8000/v1/print_daemon0/deregister",
                    },
                ]
            },
            "usage": [{"times_consumed": 2, "consumer_entity_did": "did:sov:test:120"}],
        },
        # Service 2 (similar structure)
        {
            "uuid": "23b8c1e9-3924-56de-3eb1-3b9046685257",
            "service_name": "Carlos Printing1",
            "service_type": "3D Printing",
            "endpoint_url": "http://127.0.0.1:8001/v1/print_daemon1",
            "other": {},
            "entity_did": "did:sov:test:121",
            "status": {"data": ["draft", "registered"]},
            "action": {
                "data": [
                    {
                        "name": "register",
                        "endpoint": "http://127.0.0.1:8001/v1/print_daemon1/register",
                    },
                    {
                        "name": "deregister",
                        "endpoint": "http://127.0.0.1:8001/v1/print_daemon1/deregister",
                    },
                ]
            },
            "usage": [{"times_consumed": 2, "consumer_entity_did": "did:sov:test:120"}],
        },
        {
            "uuid": "bd9c66b3-ad3c-2d6d-1a3d-1fa7bc8960a9",
            "service_name": "Carlos Printing2",
            "service_type": "3D Printing",
            "endpoint_url": "http://127.0.0.1:8002/v1/print_daemon2",
            "other": {},
            "entity_did": "did:sov:test:122",
            "status": {"data": ["draft", "registered"]},
            "action": {
                "data": [
                    {
                        "name": "register",
                        "endpoint": "http://127.0.0.1:8002/v1/print_daemon2/register",
                    },
                    {
                        "name": "deregister",
                        "endpoint": "http://127.0.0.1:8002/v1/print_daemon2/deregister",
                    },
                ]
            },
            "usage": [{"times_consumed": 2, "consumer_entity_did": "did:sov:test:120"}],
        },
        {
            "uuid": "972a8469-1641-9f82-8b9d-2434e465e150",
            "service_name": "Carlos Printing3",
            "service_type": "3D Printing",
            "endpoint_url": "http://127.0.0.1:8003/v1/print_daemon3",
            "other": {},
            "entity_did": "did:sov:test:123",
            "status": {"data": ["draft", "registered"]},
            "action": {
                "data": [
                    {
                        "name": "register",
                        "endpoint": "http://127.0.0.1:8003/v1/print_daemon3/register",
                    },
                    {
                        "name": "deregister",
                        "endpoint": "http://127.0.0.1:8003/v1/print_daemon3/deregister",
                    },
                ]
            },
            "usage": [{"times_consumed": 2, "consumer_entity_did": "did:sov:test:120"}],
        },
    ]
    return JSONResponse(content=res, status_code=200)


@app_dlg.get("/dlg_list_of_did_resolutions", response_model=list[Resolution])
async def dlg_list_of_did_resolutions() -> list[Resolution]:
    res = []

    res.append(
        Resolution(
            timestamp=datetime.fromisoformat("2021-10-12T12:52:00.000Z"),
            requester_name="C1",
            requester_did="did:sov:test:1122",
            resolved_did="did:sov:test:1234",
            other={"test": "test"},
        )
    )
    res.append(
        Resolution(
            timestamp=datetime.fromisoformat("2021-10-12T12:53:00.000Z"),
            requester_name="C2",
            requester_did="did:sov:test:1123",
            resolved_did="did:sov:test:1234",
            other={"test": "test"},
        )
    )
    return res
