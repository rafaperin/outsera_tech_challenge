from src.config.errors import RepositoryError
from src.repositories.movies_repository import MoviesRepository
from src.usecases.movies_usecase import MoviesUseCase


class MoviesController:

    @staticmethod
    async def get_all_winners() -> dict:
        movies_repository = MoviesRepository()

        try:
            result = MoviesUseCase(movies_repository).get_all_winners()
        except Exception:
            raise RepositoryError.get_operation_failed()

        return result
