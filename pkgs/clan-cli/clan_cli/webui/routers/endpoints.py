import json
import logging
import time
import typing
from collections import OrderedDict
from typing import Any, List, Optional

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends, Query
from fastapi.responses import HTMLResponse, PlainTextResponse
from sqlalchemy.orm import Session

from clan_cli.config import ap_url, c1_url, c2_url, dlg_url, group_type_to_label

from ...errors import ClanError
from .. import sql_crud, sql_db, sql_models
from ..schemas import (
    Entity,
    EntityCreate,
    Eventmessage,
    EventmessageCreate,
    Resolution,
    Role,
    Service,
    ServiceCreate,
    ServiceUsageCreate,
)
from ..tags import Tags

router = APIRouter()

log = logging.getLogger(__name__)


# API Endpoints for all tables
# see the default api documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/DefaultApi.md


#########################
#                       #
#        Service        #
#                       #
#########################
# see the corresponding documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/Service.md
### pkgs/clan-cli/tests/openapi_client/docs/ServiceCreate.md
### pkgs/clan-cli/tests/openapi_client/docs/ServiceUsageCreate.md
### pkgs/clan-cli/tests/openapi_client/docs/ServicesApi.md
@router.post("/api/v1/service", response_model=Service, tags=[Tags.services])
def create_service(
    service: ServiceCreate, db: Session = Depends(sql_db.get_db)
) -> Service:
    services = sql_crud.create_service(db=db, service=service)
    return services


@router.post("/api/v1/service_usage", response_model=Service, tags=[Tags.services])
def add_service_usage(
    usage: ServiceUsageCreate,
    service_uuid: str = "bdd640fb-0667-1ad1-1c80-317fa3b1799d",
    db: Session = Depends(sql_db.get_db),
) -> Service:
    service = sql_crud.add_service_usage(db, service_uuid, usage)
    return service


@router.put("/api/v1/inc_service_usage", response_model=Service, tags=[Tags.services])
def inc_service_usage(
    usage: ServiceUsageCreate,
    consumer_entity_did: str = "did:sov:test:120",
    service_uuid: str = "bdd640fb-0667-1ad1-1c80-317fa3b1799d",
    db: Session = Depends(sql_db.get_db),
) -> Service:
    service = sql_crud.increment_service_usage(db, service_uuid, consumer_entity_did)
    return service


@router.put("/api/v1/service", response_model=Service, tags=[Tags.services])
def update_service(
    service: ServiceCreate,
    uuid: str = "bdd640fb-0667-1ad1-1c80-317fa3b1799d",
    db: Session = Depends(sql_db.get_db),
) -> Service:
    service = sql_crud.set_service(db, uuid, service)
    return service


@router.get("/api/v1/services", response_model=List[Service], tags=[Tags.services])
def get_all_services(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Service]:
    services = sql_crud.get_services(db, skip=skip, limit=limit)
    return services


@router.get(
    "/api/v1/service_by_did", response_model=List[Service], tags=[Tags.services]
)
def get_service_by_did(
    entity_did: str = "did:sov:test:120",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_by_entity_did(db, entity_did=entity_did)
    return service


@router.get("/api/v1/service", response_model=Service, tags=[Tags.services])
def get_service_by_uuid(
    uuid: str = "bdd640fb-0667-1ad1-1c80-317fa3b1799d",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Service]:
    service = sql_crud.get_service_by_uuid(db, uuid=uuid)
    return service


@router.get(
    "/api/v1/services_without_entity",
    response_model=List[Service],
    tags=[Tags.services],
)
def get_services_without_entity(
    entity_did: str = "did:sov:test:120",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_without_entity_id(db, entity_did=entity_did)
    return service


@router.delete("/api/v1/service", tags=[Tags.services])
def delete_service(
    entity_did: str = "did:sov:test:120",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_service_by_entity_did(db, entity_did)
    return {"message": "service deleted"}


#########################
#                       #
#        Entity         #
#                       #
#########################
# see the corresponding documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/Entity.md
### pkgs/clan-cli/tests/openapi_client/docs/EntityCreate.md
### pkgs/clan-cli/tests/openapi_client/docs/EntitiesApi.md
@router.post("/api/v1/entity", response_model=Entity, tags=[Tags.entities])
def create_entity(
    entity: EntityCreate, db: Session = Depends(sql_db.get_db)
) -> sql_models.Entity:
    return sql_crud.create_entity(db, entity)


@router.get(
    "/api/v1/entity_by_roles", response_model=List[Entity], tags=[Tags.entities]
)
def get_entity_by_roles(
    roles: List[Role] = Query(...), db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entity = sql_crud.get_entity_by_role(db, roles=roles)
    return entity


@router.get("/api/v1/entities", response_model=List[Entity], tags=[Tags.entities])
def get_all_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_entities(db, skip=skip, limit=limit)
    return entities


@router.get("/api/v1/entity", response_model=Entity, tags=[Tags.entities])
def get_entity_by_did(
    entity_did: str = "did:sov:test:120",
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_name_or_did(db, name=entity_did)
    return entity


@router.get(
    "/api/v1/attached_entities",
    response_model=List[Entity],
    tags=[Tags.entities],
)
def get_attached_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_attached_entities(db, skip=skip, limit=limit)
    return entities


@router.put("/api/v1/detach", tags=[Tags.entities])
def detach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:120",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.set_stop_health_task(db, entity_did, True)
    return {"message": f"Detached {entity_did} successfully"}


@router.put("/api/v1/attach", tags=[Tags.entities])
def attach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:120",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    if entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")
    url = f"http://{entity.ip}/health"
    sql_crud.set_stop_health_task(db, entity_did, False)
    print("Start health query at", url)
    background_tasks.add_task(attach_entity_loc, db, entity_did)
    return {"message": f"Started attachment task for {entity.name}"}


@router.get("/api/v1/is_attached", tags=[Tags.entities])
def is_attached(
    entity_did: str = "did:sov:test:120", db: Session = Depends(sql_db.get_db)
) -> dict[str, str]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)

    if entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    timer = 0.0
    timeout = 2
    while not entity.attached:
        time.sleep(0.1)

        timer += 0.1
        if timer > timeout:
            url = f"http://{entity.ip}"
            raise ClanError(f"Entity at {url} not reachable")

        db.refresh(entity)
    return {"message": f"Attached to {entity.name} successfully"}


def attach_entity_loc(db: Session, entity_did: str) -> None:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    try:
        assert entity is not None
        url = f"http://{entity.ip}/health"

        while entity.stop_health_task is False:
            response = httpx.get(url, timeout=2)
            if response.status_code != 200:
                raise ClanError(
                    f"Entity with did '{entity_did}' returned {response.status_code}"
                )

            if entity.attached is False:
                sql_crud.set_attached_by_entity_did(db, entity_did, True)
            if entity is None:
                raise ClanError(f"Entity with did '{entity_did}' has been deleted")

            time.sleep(1)
            db.refresh(entity)
    except Exception:
        print(f"Entity {entity_did} not reachable at {url}")
    finally:
        sql_crud.set_attached_by_entity_did(db, entity_did, False)
        sql_crud.set_stop_health_task(db, entity_did, False)


@router.delete("/api/v1/entity", tags=[Tags.entities])
def delete_entity(
    entity_did: str = "did:sov:test:120",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_entity_by_did_recursive(db, did=entity_did)
    return {"message": "Entity deleted and all relations to that entity"}


def get_rpc_by_role(db: Session, role: Role, path: str) -> Any:
    matching_entities = sql_crud.get_entity_by_role(db, roles=[role])
    if matching_entities is None:
        raise ClanError(f"No {role} found")
    if len(matching_entities) > 1:
        raise ClanError(f"More than one {role} found")
    if len(matching_entities) == 0:
        raise ClanError(f"No {role} found")
    dlg = matching_entities[0]

    url = f"http://{dlg.ip}/{path}"
    try:
        response = httpx.get(url, timeout=2)
    except httpx.HTTPError as e:
        raise ClanError(f"{role} not reachable at {url}") from e

    if response.status_code != 200:
        raise ClanError(f"{role} returned {response.status_code}")

    return response.json()


#########################
#                       #
#      Resolution       #
#                       #
#########################
# see the corresponding documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/Resolution.md
### pkgs/clan-cli/tests/openapi_client/docs/ResolutionApi.md
@router.get(
    "/api/v1/resolutions", response_model=List[Resolution], tags=[Tags.resolutions]
)
def get_all_resolutions(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[Resolution]:
    return get_rpc_by_role(db, Role("DLG"), "dlg_list_of_did_resolutions")


#########################
#                       #
#      Repository       #
#                       #
#########################
# see the corresponding documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/RepositoriesApi.md
@router.get(
    "/api/v1/repositories", tags=[Tags.repositories], response_model=List[Service]
)
def get_all_repositories(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[Service]:
    return get_rpc_by_role(db, Role("AP"), "ap_list_of_services")


#########################
#                       #
#      Eventmessage     #
#                       #
#########################
# see the corresponding documentation under:
### pkgs/clan-cli/tests/openapi_client/docs/Eventmessage.md
### pkgs/clan-cli/tests/openapi_client/docs/EventmessageCreate.md
### pkgs/clan-cli/tests/openapi_client/docs/EventmessageApi.md
@router.post(
    "/api/v1/event_message", response_model=Eventmessage, tags=[Tags.eventmessages]
)
def create_eventmessage(
    eventmsg: EventmessageCreate, db: Session = Depends(sql_db.get_db)
) -> EventmessageCreate:
    return sql_crud.create_eventmessage(db, eventmsg)


@typing.no_type_check
@router.get(
    "/api/v1/event_messages",
    response_class=PlainTextResponse,
    tags=[Tags.eventmessages],
)
def get_all_eventmessages(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> PlainTextResponse:
    # SQL sorts eventmessages by timestamp, so we don't need to sort them here
    eventmessages = sql_crud.get_eventmessages(db, skip=skip, limit=limit)
    cresult: List[OrderedDict[int, OrderedDict[int, List[Eventmessage]]]] = []

    cresult_idx = 0
    cresult.append(OrderedDict())
    for idx, msg in enumerate(eventmessages):
        # Use the group_type_to_label from config.py to get the group name and msg_type name
        group = group_type_to_label.get(msg.group, None)
        group_name = (
            str(group.get("name", None)) if group is not None else str(msg.group)
        )
        msg_type_name = (
            group.get(msg.msg_type, None) if group is not None else str(msg.msg_type)
        )

        # Get the name of the src and des entity from the database
        src_name = sql_crud.get_entity_by_did(db, msg.src_did)
        src_name = src_name if src_name is None else src_name.name
        des_name = sql_crud.get_entity_by_did(db, msg.des_did)
        des_name = des_name if des_name is None else des_name.name

        result = cresult[cresult_idx]

        if result.get("group_name") is None:
            # Initialize the result array and dictionary
            result["group_name"] = group_name
        elif result["group_name"] != group_name:
            # If the group name changed, create a new result array and dictionary
            cresult_idx += 1
            cresult.append(OrderedDict())
            result = cresult[cresult_idx]
            result["group_name"] = group_name

        if result.get("groups") is None:
            result["groups"] = OrderedDict()

        if result["groups"].get(msg.group_id) is None:
            result["groups"][msg.group_id] = []

        # Append the eventmessage to the result array
        result_arr = result["groups"][msg.group_id]
        result_arr.append(
            Eventmessage(
                id=msg.id,
                timestamp=msg.timestamp,
                group=msg.group,
                group_name=group_name,
                group_id=msg.group_id,
                msg_type=msg.msg_type,
                msg_type_name=msg_type_name,
                src_did=msg.src_did,
                src_name=src_name,
                des_did=msg.des_did,
                des_name=des_name,
                msg=msg.msg,
            ).dict()
        )

    return PlainTextResponse(content=json.dumps(cresult, indent=4), status_code=200)


##############################
#                            #
#   EMULATED API ENDPOINTS   #
#                            #
##############################
@router.get("/emulate", response_class=HTMLResponse)
def get_emulated_enpoints() -> HTMLResponse:
    html_content = f"""
    <html>
        <head>
            <title>Emulated API</title>
        </head>
        <body>
            <h1>Emulated API</h1>
            <p>Emulated API endpoints for testing purposes.</p>
            <p>DLG: <a href="{dlg_url}" >{dlg_url} </a></p>
            <p>AP: <a href="{ap_url}">{ap_url}</a></p>
            <p>C1: <a href="{c1_url}">{c1_url} </a></p>
            <p>C2: <a href="{c2_url}">{c2_url}</a></p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
