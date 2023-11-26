from enum import Enum
from typing import Any, Dict, List


class Tags(Enum):
    producers = "producers"
    consumers = "consumers"
    entities = "entities"
    repositories = "repositories"

    def __str__(self) -> str:
        return self.value


tags_metadata: List[Dict[str, Any]] = [
    {
        "name": str(Tags.producers),
        "description": "Operations on a producer.",
    },
    {
        "name": str(Tags.consumers),
        "description": "Operations on a consumer.",
    },
    {
        "name": str(Tags.entities),
        "description": "Operations on an entity.",
    },
    {
        "name": str(Tags.repositories),
        "description": "Operations on a repository.",
    },
]
