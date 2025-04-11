from src.external.sqlite3_db import conn
from src.schemas.movies_schema import Movie
from src.interfaces.repositories.movies_repository_interface import IMoviesRepository


class MoviesRepository(IMoviesRepository):
    def get_by_id(self, movie_id: int):
        pass

    def get_all(self):
        pass

    def get_all_winners(self):
        cursor = conn.cursor()
        cursor.execute("SELECT year, producers FROM movies WHERE winner = 'yes'")
        rows = cursor.fetchall()

        return rows

    def create(self, obj_in: Movie):
        pass

    def update(self, movie_id: int, obj_in: Movie):
        pass

    def remove(self, movie_id: int) -> None:
        pass
