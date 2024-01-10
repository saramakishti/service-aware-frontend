import sys
import time
import urllib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import test_db_api

app_dlg = FastAPI()
app_ap = FastAPI()
app_c1 = FastAPI()
app_c2 = FastAPI()

# bash tests: curl localhost:8000/ap_list_of_services


#### HEALTH

@app_c1.get("/health")
async def healthcheck() -> str:
    return "200 OK"
@app_c2.get("/health")
async def healthcheck() -> str:
    return "200 OK"
@app_dlg.get("/health")
async def healthcheck() -> str:
    return "200 OK"
@app_ap.get("/health")
async def healthcheck() -> str:
    return "200 OK"

def get_health(*, url: str, max_retries: int = 20, delay: float = 0.2) -> str | None:
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read()
        except urllib.URLError as e:
            print(f"Attempt {attempt + 1} failed: {e.reason}", file=sys.stderr)
            time.sleep(delay)
    return None


#### CONSUME SERVICE

# TODO send_msg???

@app_c1.get("/consume_service_from_other_entity", response_class=HTMLResponse)
async def consume_service_from_other_entity() -> HTMLResponse:
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
async def consume_service_from_other_entity() -> HTMLResponse:
    html_content = """
    <html>
        <body>
            <div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/IOWD3uknMxYyh7CsgN/video" width="480"></iframe></div>
        </body>
    </html>
    """
    time.sleep(3)
    return HTMLResponse(content=html_content, status_code=200)


#### ap_list_of_services

@app_ap.get("/ap_list_of_services", response_class=HTMLResponse)
async def ap_list_of_services() -> HTMLResponse:
    html_content = b"""HTTP/1.1 200 OK\r\n\r\n[[
  {
    "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30df",
    "service_name": "Carlos Printing",
    "service_type": "3D Printing",
    "endpoint_url": "http://127.0.0.1:8000",
    "status": "unknown",
    "other": {
      "action": [
        "register",
        "deregister",
        "delete",
        "create"
      ]
    },
    "entity_did": "did:sov:test:1234"
  },
  {
    "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d1",
    "service_name": "Luiss Fax",
    "service_type": "Fax",
    "endpoint_url": "http://127.0.0.1:8000",
    "status": "unknown",
    "other": {
      "action": [
        "register",
        "deregister",
        "delete",
        "create"
      ]
    },
    "entity_did": "did:sov:test:1235"
  },
  {
    "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d2",
    "service_name": "Erdems VR-Stream",
    "service_type": "VR-Stream",
    "endpoint_url": "http://127.0.0.1:8000",
    "status": "unknown",
    "other": {
      "action": [
        "register",
        "deregister",
        "delete",
        "create"
      ]
    },
    "entity_did": "did:sov:test:1236"
  },
  {
    "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d3",
    "service_name": "Onurs gallary",
    "service_type": "gallary",
    "endpoint_url": "http://127.0.0.1:8000",
    "status": "unknown",
    "other": {
      "action": [
        "register",
        "deregister",
        "delete",
        "create"
      ]
    },
    "entity_did": "did:sov:test:1237"
  },
  {
    "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d4",
    "service_name": "Saras Game-Shop",
    "service_type": "Game-Shop",
    "endpoint_url": "http://127.0.0.1:8000",
    "status": "unknown",
    "other": {
      "action": [
        "register",
        "deregister",
        "delete",
        "create"
      ]
    },
    "entity_did": "did:sov:test:1238"
  }
]]"""
    return HTMLResponse(content=html_content, status_code=200)


@app_dlg.get("/dlg_list_of_did_resolutions", response_class=HTMLResponse)
async def dlg_list_of_did_resolutions() -> HTMLResponse:
    html_content = b"""HTTP/1.1 200 OK\r\n\r\n
[
  {
    "did": "did:sov:test:1234",
    "name": "C1",
    "ip": "127.0.0.1:5100",
    "attached": false,
    "visible": true,
    "other": {
      "network": "Carlo1's Home Network",
      "roles": [
        "service repository",
        "service consumer"
      ]
    }
  },
  {
    "did": "did:sov:test:1235",
    "name": "C2",
    "ip": "127.0.0.1:5100",
    "attached": false,
    "visible": true,
    "other": {
      "network": "Carlo2's Home Network",
      "roles": [
        "service repository",
        "service prosumer"
      ]
    }
  }
]"""
    return HTMLResponse(content=html_content, status_code=200)

uvicorn.run(app_dlg, host=f"{test_db_api.host}", port=test_db_api.port_dlg)
uvicorn.run(app_ap, host=f"{test_db_api.host}", port=test_db_api.port_dlg)
uvicorn.run(app_c1, host=f"{test_db_api.host}", port=test_db_api.port_client_base)
uvicorn.run(app_c2, host=f"{test_db_api.host}", port=test_db_api.port_client_base+1)
