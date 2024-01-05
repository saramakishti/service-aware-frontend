from openapi_client import ApiClient
from openapi_client.api import default_api
from openapi_client.models import Machine, Status

default_entity_did_url = "entity_did=did%3Asov%3Atest%3A1234"
default_entity_did = "did:sov:test:1234"
default_entity_did2 = "did:sov:test:1235"
default_entity_did3 = "did:sov:test:1236"
default_entity_did4 = "did:sov:test:1237"
default_entity_did5 = "did:sov:test:1238"


def test_health(api_client: ApiClient) -> None:
    default = default_api.DefaultApi(api_client=api_client)
    res: Machine = default.health()
    assert res.status == Status.ONLINE
