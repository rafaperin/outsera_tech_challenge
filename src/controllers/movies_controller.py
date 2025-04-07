from src.schemas.movies_schema import MovieCreate, MovieUpdate
from src.config.errors import ResourceNotFound, RepositoryError
from src.repositories.movies_repository import MoviesRepository
from src.usecases.movies_usecase import MoviesUseCase


class MoviesController:

    @staticmethod
    async def get_all_movies() -> dict:
        movies_repository = MoviesRepository()

        try:
            result = MoviesUseCase(movies_repository).get_all()
        except Exception:
            raise RepositoryError.get_operation_failed()

        return {"result": result}

    @staticmethod
    async def get_movie_by_id(
        movie_id: int
    ) -> dict:
        movie_gateway = MoviesRepository()

        try:
            result = MoviesUseCase(movie_gateway).get_by_id(movie_id)
        except ResourceNotFound:
            raise ResourceNotFound.get_operation_failed(f"No movie with id: {movie_id}")
        except Exception:
            raise RepositoryError.get_operation_failed()

        return {"result": result}

    @staticmethod
    async def create_movie(
        request: MovieCreate
    ) -> dict:
        movie_gateway = MoviesRepository()

        try:
            result = MoviesUseCase(movie_gateway).create(request)
        except Exception as e:
            print(e)
            raise RepositoryError.save_operation_failed()

        return {"result": result}

    @staticmethod
    async def change_movie_data(
        movie_id: int,
        request: MovieUpdate
    ) -> dict:
        movie_gateway = MoviesRepository()

        try:
            result = MoviesUseCase(movie_gateway).update(movie_id, request)
        except Exception:
            raise RepositoryError.save_operation_failed()

        return {"result": result}

    @staticmethod
    async def remove_movie(
        movie_id: int
    ) -> dict:
        movie_gateway = MoviesRepository()

        try:
            MoviesUseCase(movie_gateway).remove(movie_id)
        except Exception:
            raise RepositoryError.save_operation_failed()

        return {"result": "Movie removed successfully"}
