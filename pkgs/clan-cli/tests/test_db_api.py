from openapi_client import ApiClient
from openapi_client.api import DefaultApi
from openapi_client.api.entities_api import EntitiesApi
from openapi_client.api.services_api import ServicesApi
from openapi_client.models import (
    Entity,
    EntityCreate,
    Machine,
    ServiceCreate,
    Status,
)

uuids = [
    "e95bb72f-b1b3-4452-8065-c7acf09068fc",
    "411d772e-1ad0-4d99-8da0-133ab2972322",
    "8cfdf359-c3b9-4951-9e51-08dce797725a",
    "24b5b4de-9f5f-4e60-878e-cc5be085fd0d",
    "d45f9687-c413-43b9-8e0d-cb610b39fcaf",
    "083e09a0-1d71-4819-83e2-ce2a6d831713",
    "e6f74e55-c163-4368-98c0-a2b04c99d6e3",
    "1b577ba7-c9dd-4e66-b695-9350e9db0b6c",
    "bfd9e653-98a4-4451-9d97-bcc2908f213d",
    "0e481624-b886-437c-89a0-b9e73651cc72",
]


def test_health(api_client: ApiClient) -> None:
    default = DefaultApi(api_client=api_client)
    res: Machine = default.health()
    assert res.status == Status.ONLINE


def test_entities_empty(api_client: ApiClient) -> None:
    entity = EntitiesApi(api_client=api_client)
    res = entity.get_all_entities()
    assert res == []


def create_entities(num: int = 10) -> list[EntityCreate]:
    res = []
    for i in range(num):
        en = EntityCreate(
            did=f"did:sov:test:12{i}",
            name=f"C{i}",
            ip=f"127.0.0.1:{7000+i}",
            visible=True,
            other={},
        )
        res.append(en)
    return res


def create_service(idx: int, entity: Entity) -> ServiceCreate:
    se = ServiceCreate(
        uuid=uuids[idx],
        service_name=f"Carlos Printing{idx}",
        service_type="3D Printing",
        endpoint_url=f"{entity.ip}/v1/print_daemon{idx}",
        status="unknown",
        other={"action": ["register", "deregister", "delete", "create"]},
        entity_did=entity.did,
    )

    return se


def test_create_entities(api_client: ApiClient) -> None:
    api = EntitiesApi(api_client=api_client)
    for own_entity in create_entities():
        res: Entity = api.create_entity(own_entity)
        assert res.did == own_entity.did
        assert res.attached is False


def test_create_services(api_client: ApiClient) -> None:
    sapi = ServicesApi(api_client=api_client)
    eapi = EntitiesApi(api_client=api_client)
    for idx, entity in enumerate(eapi.get_all_entities()):
        service_obj = create_service(idx, entity)
        service = sapi.create_service(service_obj)
        assert service.uuid == service_obj.uuid
