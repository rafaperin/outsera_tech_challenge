from fastapi import APIRouter, status

from src.api.errors.api_errors import APIErrorMessage
from src.config.errors import RepositoryError, ResourceNotFound
from src.controllers.movies_controller import MoviesController
from src.schemas.movies_schema import MovieCreate, MovieUpdate, \
    MovieResponse, MovieListResponse
from src.utils.sample_data import insert_csv_to_memory_db

router = APIRouter(tags=["Movies"])


@router.get(
    "/movies",
    response_model=MovieListResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_movies() -> dict:
    # try:
    #     result = await MoviesController.get_all_movies()
    # except Exception:
    #     raise RepositoryError.get_operation_failed()
    #
    # return result
    print("oi")
    insert_csv_to_memory_db()
    print("tchau")
    return 1

@router.get(
    "/movies/{movie_id}",
    response_model=MovieResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_movie_by_id(
    movie_id: int
) -> dict:
    try:
        result = await MoviesController.get_movie_by_id(movie_id)
    except ResourceNotFound:
        raise ResourceNotFound.get_operation_failed(f"No movie with id: {movie_id}")
    except Exception:
        raise RepositoryError.get_operation_failed()

    return result


@router.post(
    "/movies",
    response_model=MovieResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def create_movie(
    request: MovieCreate
) -> dict:
    try:
        result = await MoviesController.create_movie(request)
    except Exception as e:
        print(e)
        raise RepositoryError.save_operation_failed()

    return result


@router.put(
    "/movies/{movie_id}",
    response_model=MovieResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_movie_data(
    movie_id: int,
    request: MovieUpdate
) -> dict:
    try:
        result = await MoviesController.change_movie_data(movie_id, request)
    except Exception as e:
        print(e)
        raise RepositoryError.save_operation_failed()

    return result


@router.delete(
    "/movies/{movie_id}",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_movie(
    movie_id: int
) -> dict:
    try:
        await MoviesController.remove_movie(movie_id)
    except Exception as e:
        print(e)
        raise RepositoryError.save_operation_failed()

    return {"result": "Movie removed successfully"}
