import urllib.parse as url
from typing import Any

from api import TestClient

default_entity_did_url = "entity_did=did%3Asov%3Atest%3A1234"
default_entity_did = "did:sov:test:1234"
default_entity_did2 = "did:sov:test:1235"
default_entity_did3 = "did:sov:test:1236"
default_entity_did4 = "did:sov:test:1237"
default_entity_did5 = "did:sov:test:1238"


def assert_extra_info(
    infos: list[str],
    request_body: dict[str, Any],
    response: dict[str, str],
) -> None:
    # print(type())
    for info in infos:
        assert info in response.keys()
        # TODO maybe check the content of the extra info ...
        response.pop(info)
    assert response == request_body


def make_test_post_and_get(
    api: TestClient,
    request_body: dict[str, Any],
    paramter: str,
    get_request: str = default_entity_did_url,
    apiversion: str = "v1",
) -> None:
    # test post
    response = api.post(
        f"/api/{apiversion}/create_{paramter}",
        json=request_body,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    if paramter == "repository":
        assert_extra_info(["time_created"], request_body, response.json())
    elif paramter == "consumer":
        assert_extra_info(["id"], request_body, response.json())
    elif paramter == "entity":
        assert_extra_info(
            ["consumers", "producers", "repository"], request_body, response.json()
        )
    else:
        assert response.json() == request_body
    # test get
    response = api.get(
        f"api/{apiversion}/get_{paramter}?{get_request}&skip=0&limit=100"
    )
    assert response.status_code == 200
    if paramter == "repository":
        assert_extra_info(["time_created"], request_body, response.json()[0])
    elif paramter == "consumer":
        assert_extra_info(["id"], request_body, response.json()[0])
    elif paramter == "entity":
        assert_extra_info(
            ["consumers", "producers", "repository"], request_body, response.json()
        )
    else:
        assert response.json() == [request_body]


#########################
#                       #
#       Producer        #
#                       #
#########################
def test_producer(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30df",
        "service_name": "Carlo'''s Printing",
        "service_type": "3D Printing",
        "endpoint_url": "http://127.0.0.1:8000",
        "status": "unknown",
        "other": {"test": "test"},
        "entity_did": default_entity_did,
    }
    paramter = "producer"
    # get_request = "entity_did=did%3Asov%3Atest%3A1234"
    make_test_post_and_get(api, request_body, paramter)

def test_producer2(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d1",
        "service_name": "Luis'''s Fax",
        "service_type": "Fax",
        "endpoint_url": "http://127.0.0.1:8001",
        "status": "unknown",
        "other": {"faxen": "dicke"},
        "entity_did": default_entity_did2,
    }
    paramter = "producer"
    get_request = "entity_did="+url.quote(default_entity_did2)
    make_test_post_and_get(api, request_body, paramter, get_request)

def test_producer3(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d2",
        "service_name": "Erdem'''s VR-Stream",
        "service_type": "VR-Stream",
        "endpoint_url": "http://127.0.0.1:8002",
        "status": "unknown",
        "other": {"oculos": "rift"},
        "entity_did": default_entity_did3,
    }
    paramter = "producer"
    get_request = "entity_did="+url.quote(default_entity_did3)
    make_test_post_and_get(api, request_body, paramter, get_request)


def test_producer4(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d3",
        "service_name": "Onur'''s gallary",
        "service_type": "gallary",
        "endpoint_url": "http://127.0.0.1:8003",
        "status": "unknown",
        "other": {"nice": "pics"},
        "entity_did": default_entity_did4,
    }
    paramter = "producer"
    get_request = "entity_did="+url.quote(default_entity_did4)
    make_test_post_and_get(api, request_body, paramter, get_request)


def test_producer5(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d4",
        "service_name": "Sara'''s Game-Shop",
        "service_type": "Game-Shop",
        "endpoint_url": "http://127.0.0.1:8004",
        "status": "unknown",
        "other": {"war": "games"},
        "entity_did": default_entity_did5,
    }
    paramter = "producer"
    get_request = "entity_did="+url.quote(default_entity_did5)
    make_test_post_and_get(api, request_body, paramter, get_request)



#########################
#                       #
#       Consumer        #
#                       #
#########################
def test_consumer(api: TestClient) -> None:
    request_body = {
        "entity_did": default_entity_did,
        "producer_uuid": "8e285c0c-4e40-430a-a477-26b3b81e30df",
        "other": {"test": "test"},
    }
    paramter = "consumer"
    # get_request = "entity_did=did%3Asov%3Atest%3A1234"
    make_test_post_and_get(api, request_body, paramter)

def test_consumer2(api: TestClient) -> None:
    request_body = {
        "entity_did": default_entity_did2,
        "producer_uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d4",
        "other": {"war": "games"},
    }
    paramter = "consumer"
    get_request = "entity_did="+url.quote(default_entity_did2)
    make_test_post_and_get(api, request_body, paramter, get_request)

#########################
#                       #
#       REPOSITORY      #
#                       #
#########################
def test_repository(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30df",
        "service_name": "Carlo'''s Printing",
        "service_type": "3D Printing",
        "endpoint_url": "http://127.0.0.1:8000",
        "status": "unknown",
        "other": {"test": "test"},
        "entity_did": default_entity_did,
    }
    paramter = "repository"
    # get_request = "entity_did=did%3Asov%3Atest%3A1234"
    make_test_post_and_get(api, request_body, paramter)
def test_repository2(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d1",
        "service_name": "Luis'''s Fax",
        "service_type": "Fax",
        "endpoint_url": "http://127.0.0.1:8001",
        "status": "unknown",
        "other": {"faxen": "dicke"},
        "entity_did": default_entity_did2,
    }
    paramter = "repository"
    get_request = "entity_did="+url.quote(default_entity_did2)
    make_test_post_and_get(api, request_body, paramter, get_request)

def test_repository3(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d2",
        "service_name": "Erdem'''s VR-Stream",
        "service_type": "VR-Stream",
        "endpoint_url": "http://127.0.0.1:8002",
        "status": "unknown",
        "other": {"oculos": "rift"},
        "entity_did": default_entity_did3,
    }
    paramter = "repository"
    get_request = "entity_did="+url.quote(default_entity_did3)
    make_test_post_and_get(api, request_body, paramter, get_request)


def test_repository4(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d3",
        "service_name": "Onur'''s gallary",
        "service_type": "gallary",
        "endpoint_url": "http://127.0.0.1:8003",
        "status": "unknown",
        "other": {"nice": "pics"},
        "entity_did": default_entity_did4,
    }
    paramter = "repository"
    get_request = "entity_did="+url.quote(default_entity_did4)
    make_test_post_and_get(api, request_body, paramter, get_request)


def test_repository5(api: TestClient) -> None:
    request_body = {
        "uuid": "8e285c0c-4e40-430a-a477-26b3b81e30d4",
        "service_name": "Sara'''s Game-Shop",
        "service_type": "Game-Shop",
        "endpoint_url": "http://127.0.0.2:8004",
        "status": "unknown",
        "other": {"war": "games"},
        "entity_did": default_entity_did5,
    }
    paramter = "repository"
    get_request = "entity_did="+url.quote(default_entity_did5)
    make_test_post_and_get(api, request_body, paramter, get_request)



#########################
#                       #
#        Entity         #
#                       #
#########################
def test_entity(api: TestClient) -> None:
    request_body = {
        "did": default_entity_did,
        "name": "C1",
        "ip": "127.0.0.1",
        "attached": False,
        "other": {"test": "test"},
    }
    paramter = "entity"
    # get_request = "entity_did=did%3Asov%3Atest%3A1234"
    make_test_post_and_get(api, request_body, paramter)

def test_entity2(api: TestClient) -> None:
    request_body = {
        "did": default_entity_did2,
        "name": "C2",
        "ip": "127.0.0.2",
        "attached": False,
        "other": {"test": "test"},
    }
    paramter = "entity"
    get_request = "entity_did="+url.quote(default_entity_did2)
    make_test_post_and_get(api, request_body, paramter, get_request)