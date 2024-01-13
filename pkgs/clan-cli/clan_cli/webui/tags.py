from enum import Enum
from typing import Any, Dict, List


class Tags(Enum):
    services = "services"
    entities = "entities"
    repositories = "repositories"
    resolutions = "resolution"
    eventmessages = "eventmessages"

    def __str__(self) -> str:
        return self.value


tags_metadata: List[Dict[str, Any]] = [
    {
        "name": str(Tags.services),
        "description": "Operations on a service.",
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
    {
        "name": str(Tags.eventmessages),
        "description": "Operations for event messages.",
    },
]
