from typing import Any

from api import TestClient

default_entity_did_url = "entity_did=did%3Asov%3Atest%3A1234"
default_entity_did = "did:sov:test:1234"


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
