import random
import uuid

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

random.seed(42)


num_uuids = 100
uuids = [str(uuid.UUID(int=random.getrandbits(128))) for i in range(num_uuids)]


def test_health(api_client: ApiClient) -> None:
    default = DefaultApi(api_client=api_client)
    res: Machine = default.health()
    assert res.status == Status.ONLINE


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
    for midx, entity in enumerate(eapi.get_all_entities()):
        for idx in range(4):
            service_obj = create_service(idx + 4 * midx, entity)
            service = sapi.create_service(service_obj)
            assert service.uuid == service_obj.uuid
