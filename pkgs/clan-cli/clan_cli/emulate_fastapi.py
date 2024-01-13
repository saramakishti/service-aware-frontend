import sys
import time
import urllib
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from clan_cli.webui.schemas import Resolution

from .config import config

app_dlg = FastAPI()
app_ap = FastAPI()
app_c1 = FastAPI()
app_c2 = FastAPI()

apps = [
    (app_dlg, config.port_dlg),
    (app_ap, config.port_ap),
    (app_c1, config.port_client_base),
    (app_c2, config.port_client_base + 1),
]


#### HEALTHCHECK
@app_c1.get("/health")
async def healthcheck_c1() -> str:
    return "200 OK"


@app_c2.get("/health")
async def healthcheck_c2() -> str:
    return "200 OK"


@app_dlg.get("/health")
async def healthcheck_dlg() -> str:
    return "200 OK"


@app_ap.get("/health")
async def healthcheck_ap() -> str:
    return "200 OK"


def get_health(*, url: str, max_retries: int = 20, delay: float = 0.2) -> str | None:
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(url) as response:  # type: ignore
                return response.read()
        except urllib.error.URLError as e:  # type: ignore
            print(f"Attempt {attempt + 1} failed: {e.reason}", file=sys.stderr)
            time.sleep(delay)
    return None


#### CONSUME SERVICE

# TODO send_msg???


@app_c1.get("/consume_service_from_other_entity", response_class=HTMLResponse)
async def consume_service_from_other_entity_c1() -> HTMLResponse:
    html_content = """
    <html>
        <body>
            <div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/IOWD3uknMxYyh7CsgN/video" width="480"></iframe></div>
        </body>
    </html>
    """
    time.sleep(3)
    return HTMLResponse(content=html_content, status_code=200)


@app_c2.get("/consume_service_from_other_entity", response_class=HTMLResponse)
async def consume_service_from_other_entity_c2() -> HTMLResponse:
    html_content = """
    <html>
        <body>
            <div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/IOWD3uknMxYyh7CsgN/video" width="480"></iframe></div>
        </body>
    </html>
    """
    time.sleep(3)
    return HTMLResponse(content=html_content, status_code=200)


@app_ap.get("/ap_list_of_services", response_class=JSONResponse)
async def ap_list_of_services() -> JSONResponse:
    res = [
        {
            "uuid": "98ae4334-6c12-ace8-ae34-0454cac5b68c",
            "service_name": "Carlos Printing46",
            "service_type": "3D Printing",
            "endpoint_url": "127.0.0.1:6600/v1/print_daemon46",
            "status": "unknown",
            "other": {"action": ["register", "deregister", "delete", "create"]},
            "entity_did": "did:sov:test:6600",
            "entity": {
                "did": "did:sov:test:6600",
                "name": "AP",
                "ip": "127.0.0.1:6600",
                "network": "255.255.0.0",
                "visible": True,
                "other": {},
                "attached": False,
                "stop_health_task": False,
                "roles": ["AP"],
            },
        },
        {
            "uuid": "988c24c9-61b1-cd22-6280-1c4510435a10",
            "service_name": "Carlos Printing47",
            "service_type": "3D Printing",
            "endpoint_url": "127.0.0.1:6600/v1/print_daemon47",
            "status": "unknown",
            "other": {"action": ["register", "deregister", "delete", "create"]},
            "entity_did": "did:sov:test:6600",
            "entity": {
                "did": "did:sov:test:6600",
                "name": "AP",
                "ip": "127.0.0.1:6600",
                "network": "255.255.0.0",
                "visible": True,
                "other": {},
                "attached": False,
                "stop_health_task": False,
                "roles": ["AP"],
            },
        },
    ]
    # resp = json.dumps(obj=res)
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
