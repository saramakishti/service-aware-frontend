from enum import Enum
from typing import Any, Dict, List


class Tags(Enum):
    services = "services"
    clients = "clients"
    entities = "entities"
    repositories = "repositories"
    resolutions = "resolution"

    def __str__(self) -> str:
        return self.value


tags_metadata: List[Dict[str, Any]] = [
    {
        "name": str(Tags.services),
        "description": "Operations on a service.",
    },
    {
        "name": str(Tags.clients),
        "description": "Operations on a client.",
    },
    {
        "name": str(Tags.entities),
        "description": "Operations on an entity.",
    },
    {
        "name": str(Tags.repositories),
        "description": "Operations on a repository.",
    },
    {
        "name": str(Tags.resolutions),
        "description": "Operations on a resolution.",
    },
]
