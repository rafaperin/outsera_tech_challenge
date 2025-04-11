from fastapi import APIRouter, status

from src.api.errors.api_errors import APIErrorMessage
from src.config.errors import RepositoryError
from src.controllers.movies_controller import MoviesController
from src.schemas.movies_schema import ProducerIntervalResponse

router = APIRouter(tags=["Movies"])


@router.get(
    "/movies/winners",
    response_model=ProducerIntervalResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_winners() -> dict:
    try:
        result = await MoviesController.get_all_winners()
    except Exception:
        raise RepositoryError.get_operation_failed()

    return result
