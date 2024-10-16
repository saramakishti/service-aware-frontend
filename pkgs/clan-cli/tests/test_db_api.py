import random
import time
import uuid

from openapi_client import ApiClient
from openapi_client.api import DefaultApi
from openapi_client.api.entities_api import EntitiesApi
from openapi_client.api.eventmessages_api import EventmessagesApi
from openapi_client.api.services_api import ServicesApi
from openapi_client.models import (
    Entity,
    EntityCreate,
    Eventmessage,
    EventmessageCreate,
    Machine,
    Role,
    ServiceCreate,
    Status,
)

import clan_cli.config as config

random.seed(42)


host = config.host
port_dlg = config.port_dlg
port_ap = config.port_ap
port_client_base = config._port_client_base

num_uuids = 100
uuids = [str(uuid.UUID(int=random.getrandbits(128))) for i in range(num_uuids)]


def test_health(api_client: ApiClient) -> None:
    default = DefaultApi(api_client=api_client)
    res: Machine = default.health()
    assert res.status == Status.ONLINE


def create_entities(num: int = 5, role: str = "entity") -> list[EntityCreate]:
    res = []
    for i in range(1, num + 1):
        en = EntityCreate(
            did=f"did:sov:test:12{i}",
            name=f"C{i}",
            ip=f"{host}:{port_client_base+i}",
            network="255.255.0.0",
            roles=[Role("service_prosumer")],
            visible=True,
            other={},
        )
        res.append(en)
    dlg = EntityCreate(
        did=f"did:sov:test:{port_dlg}",
        name="DLG",
        ip=f"{host}:{port_dlg}",
        network="255.255.0.0",
        roles=[Role("DLG")],
        visible=True,
        other={},
    )
    res.append(dlg)
    ap = EntityCreate(
        did=f"did:sov:test:{port_ap}",
        name="AP",
        ip=f"{host}:{port_ap}",
        network="255.255.0.0",
        roles=[Role("AP")],
        visible=True,
        other={},
    )
    res.append(ap)
    return res


def create_service(idx: int, entity: Entity) -> ServiceCreate:
    idx += 1
    se = ServiceCreate(
        uuid=uuids[idx],
        service_name=f"Carlos Printing{idx}",
        service_type="3D Printing",
        endpoint_url=f"http://{entity.ip}/v1/print_daemon{idx}",
        status={"data": ["draft", "registered"]},
        other={},
        action={
            "data": [
                {
                    "name": "register",
                    "endpoint": f"http://{entity.ip}/v1/print_daemon{idx}/register",
                },
                {
                    "name": "deregister",
                    "endpoint": f"http://{entity.ip}/v1/print_daemon{idx}/deregister",
                },
            ]
        },
        entity_did=entity.did,
        usage=[{"times_consumed": 2, "consumer_entity_did": "did:sov:test:120"}],
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
    for midx, entity in enumerate(eapi.get_entity_by_roles([Role("service_prosumer")])):
        service_obj = create_service(midx, entity)
        service = sapi.create_service(service_obj)
        assert service.uuid == service_obj.uuid


random.seed(77)


def create_eventmessages(num: int = 4) -> list[EventmessageCreate]:
    res = []
    starttime = int(time.time())
    for i2 in range(1, num + 1):
        group_id = i2 % 5 + random.getrandbits(6) + 1
        em_req_send = EventmessageCreate(
            timestamp=starttime + i2 * 10,
            group=i2 % 5,
            group_id=group_id,
            msg_type=1,
            src_did=f"did:sov:test:12{i2}",
            des_did=f"did:sov:test:12{i2+1}",
            msg={},
        )
        res.append(em_req_send)
        em_req_rec = EventmessageCreate(
            timestamp=starttime + (i2 * 10) + 2,
            group=i2 % 5,
            group_id=group_id,
            msg_type=2,
            src_did=f"did:sov:test:12{i2}",
            des_did=f"did:sov:test:12{i2+1}",
            msg={},
        )
        res.append(em_req_rec)
        group_id = i2 % 5 + random.getrandbits(6)
        em_res_send = EventmessageCreate(
            timestamp=starttime + i2 * 10 + 4,
            group=i2 % 5,
            group_id=group_id,
            msg_type=3,
            src_did=f"did:sov:test:12{i2+1}",
            des_did=f"did:sov:test:12{i2}",
            msg={},
        )
        res.append(em_res_send)
        em_res_rec = EventmessageCreate(
            timestamp=starttime + (i2 * 10) + 8,
            group=i2 % 5,
            group_id=group_id,
            msg_type=4,
            src_did=f"did:sov:test:12{i2+1}",
            des_did=f"did:sov:test:12{i2}",
            msg={},
        )
        res.append(em_res_rec)
    return res


def test_create_eventmessages(api_client: ApiClient) -> None:
    api = EventmessagesApi(api_client=api_client)

    assert api.get_all_eventmessages() is None
    for idx, own_eventmsg in enumerate(create_eventmessages()):
        res: Eventmessage = api.create_eventmessage(own_eventmsg)

        assert res.msg == own_eventmsg.msg
        assert res.src_did == own_eventmsg.src_did
        assert res.des_did == own_eventmsg.des_did
    assert {} != api.get_all_eventmessages()
