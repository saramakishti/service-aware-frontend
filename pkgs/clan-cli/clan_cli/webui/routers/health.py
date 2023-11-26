from fastapi import APIRouter

from ..api_outputs import Machine, Status

router = APIRouter()


@router.get("/health", include_in_schema=True)
async def health() -> Machine:  # str:
    return Machine(name="test", status=Status.ONLINE)


#    return "OK"
