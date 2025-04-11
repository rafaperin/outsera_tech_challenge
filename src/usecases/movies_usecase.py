from src.schemas.movies_schema import MovieCreate, MovieUpdate, Movie
from src.interfaces.repositories.movies_repository_interface import IMoviesRepository
from src.interfaces.usecases.movies_usecase_interface import MoviesUseCaseInterface
from src.utils.data_sorting import get_prize_intervals


class MoviesUseCase(MoviesUseCaseInterface):
    def __init__(self, movie_repo: IMoviesRepository) -> None:
        self._movie_repo = movie_repo

    def get_by_id(self, movie_id: int):
        pass


    def get_all(self):
        pass

    def get_all_winners(self):
        result = self._movie_repo.get_all_winners()
        return get_prize_intervals(result)

    def create(self, input_dto: MovieCreate) -> Movie:
        pass


    def update(self, movie_id: int, input_dto: MovieUpdate) -> Movie:
        pass


    def remove(self, movie_id: int) -> None:
        pass
