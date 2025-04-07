import uuid
from typing import List, Optional

from src.schemas.movies_schema import Movie
from src.models.movies_orm import Movies
from src.interfaces.repositories.movies_repository_interface import IMoviesRepository


class MoviesRepository(IMoviesRepository):
    def get_by_id(self, movie_id: int) -> Optional[Movies]:
        pass
        # result = db.query(Movies).filter(Movies.Movie_id == Movie_id).first()

    def get_all(self) -> List[Movies]:
        pass
        # Movies = []
        #
        # with SessionLocal() as db:
        #     result = db.query(Movies).all()
        #
        # for Movie in result:
        #     Movies.append(self.to_entity(Movie))
        #
        # return Movies

    def create(self, obj_in: Movie) -> Movies:
        pass
        # obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        # db_obj = Movies(**obj_in_data)  # type: ignore
        #
        # with SessionLocal() as db:
        #     db.add(db_obj)
        #     db.commit()
        #     db.refresh(db_obj)
        #
        # new_Movie = self.to_entity(db_obj)  # type: ignore
        # return new_Movie

    def update(self, Movie_id: uuid.UUID, obj_in: Movie) -> Movies:
        pass
        # Movie_in = vars(obj_in)
        # with SessionLocal() as db:
        #     db_obj = db.query(Movies).filter(Movies.Movie_id == Movie_id).first()
        #     obj_data = jsonable_encoder(db_obj, by_alias=False)
        #     for field in obj_data:
        #         if field in Movie_in:
        #             setattr(db_obj, field, Movie_in[field])
        #     db.add(db_obj)
        #     db.commit()
        #     db.refresh(db_obj)
        # updated_Movie = self.to_entity(db_obj)
        # return updated_Movie

    def remove(self, Movie_id: uuid.UUID) -> None:
        pass
        # db_obj = db.query(Movies).filter(Movies.Movie_id == Movie_id).first()
        # db.delete(db_obj)
        # db.commit()
