import logging
import time
from typing import List, Optional

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends, Query
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

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
)
from ..tags import Tags

router = APIRouter()

log = logging.getLogger(__name__)


#########################
#                       #
#        Service        #
#                       #
#########################
@router.post("/api/v1/service", response_model=Service, tags=[Tags.services])
def create_service(
    service: ServiceCreate, db: Session = Depends(sql_db.get_db)
) -> Service:
    # todo checken ob schon da ...
    return sql_crud.create_service(db=db, service=service)


@router.get("/api/v1/services", response_model=List[Service], tags=[Tags.services])
def get_all_services(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Service]:
    services = sql_crud.get_services(db, skip=skip, limit=limit)
    return services


@router.get("/api/v1/service", response_model=List[Service], tags=[Tags.services])
def get_service_by_did(
    entity_did: str = "did:sov:test:120",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_by_entity_did(db, entity_did=entity_did)
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
@router.post("/api/v1/entity", response_model=Entity, tags=[Tags.entities])
def create_entity(
    entity: EntityCreate, db: Session = Depends(sql_db.get_db)
) -> sql_models.Entity:
    return sql_crud.create_entity(db, entity)


@router.get(
    "/api/v1/entity_by_name_or_did",
    response_model=Optional[Entity],
    tags=[Tags.entities],
)
def get_entity_by_name_or_did(
    entity_name_or_did: str = "C1", db: Session = Depends(sql_db.get_db)
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_name_or_did(db, name=entity_name_or_did)
    return entity


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


@router.get("/api/v1/entity", response_model=Optional[Entity], tags=[Tags.entities])
def get_entity_by_did(
    entity_did: str = "did:sov:test:120",
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
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
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    if entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")
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


#########################
#                       #
#      Resolution       #
#                       #
#########################
@router.get(
    "/api/v1/resolutions", response_model=List[Resolution], tags=[Tags.resolutions]
)
def get_all_resolutions(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[Resolution]:
    matching_entities = sql_crud.get_entity_by_role(db, roles=[Role("DLG")])
    if matching_entities is None:
        raise ClanError("No DLG found")
    if len(matching_entities) > 1:
        raise ClanError("More than one DLG found")
    dlg = matching_entities[0]

    url = f"http://{dlg.ip}/dlg_list_of_did_resolutions"
    try:
        response = httpx.get(url, timeout=2)
    except httpx.HTTPError as e:
        raise ClanError(f"DLG not reachable at {url}") from e

    if response.status_code != 200:
        raise ClanError(f"DLG returned {response.status_code}")

    resolutions = response.json()
    return resolutions


#########################
#                       #
#      Eventmessage     #
#                       #
#########################
@router.post(
    "/api/v1/event_message", response_model=Eventmessage, tags=[Tags.eventmessages]
)
def create_eventmessage(
    eventmsg: EventmessageCreate, db: Session = Depends(sql_db.get_db)
) -> EventmessageCreate:
    return sql_crud.create_eventmessage(db, eventmsg)


@router.get(
    "/api/v1/event_messages",
    response_model=List[Eventmessage],
    tags=[Tags.eventmessages],
)
def get_all_eventmessages(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Eventmessage]:
    eventmessages = sql_crud.get_eventmessages(db, skip=skip, limit=limit)
    return eventmessages


##############################
#                            #
#   EMULATED API ENDPOINTS   #
#                            #
##############################
@router.get("/emulate", response_class=HTMLResponse)
@router.get("/emu", response_class=HTMLResponse)
def get_emulated_enpoints() -> HTMLResponse:
    from clan_cli.config import ap_url, c1_url, c2_url, dlg_url

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
