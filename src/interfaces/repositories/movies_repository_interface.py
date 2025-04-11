from abc import ABC, abstractmethod
from typing import List

import sqlalchemy

from src.schemas.movies_schema import Movie


class IMoviesRepository(ABC):
    @abstractmethod
    def get_by_id(self, movie_id: int) -> Movie:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass

    def get_all_winners(self) -> List[sqlalchemy.Row]:
        pass

    @abstractmethod
    def create(self, movie_in: Movie) -> Movie:
        pass

    @abstractmethod
    def update(self, movie_id:int, movie_in: Movie) -> Movie:
        pass

    @abstractmethod
    def remove(self, movie_id: int) -> None:
        pass
