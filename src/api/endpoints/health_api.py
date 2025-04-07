from fastapi import APIRouter
from starlette import status

router = APIRouter(tags=["Health Check"])


@router.get("/health-check",
            status_code=status.HTTP_200_OK)
def health_check() -> dict:
    return {"result": "Service is online"}
