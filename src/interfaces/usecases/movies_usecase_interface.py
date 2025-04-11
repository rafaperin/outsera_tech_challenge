import uuid
from abc import ABC

from src.schemas.movies_schema import MovieCreate, Movie, MovieUpdate
from src.interfaces.repositories.movies_repository_interface import IMoviesRepository


class MoviesUseCaseInterface(ABC):
    def __init__(self, movie_repo: IMoviesRepository) -> None:
        raise NotImplementedError

    def get_by_id(self, customer_id: uuid.UUID):
        pass

    def get_all(self):
        pass

    def get_all_winners(self):
        pass

    def create(self, input_dto: MovieCreate) -> Movie:
        pass

    def update(self, movie_id: int, input_dto: MovieUpdate) -> Movie:
        pass

    def remove(self, movie_id: int) -> None:
        pass
