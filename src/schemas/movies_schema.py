from typing import Optional, Sequence

from pydantic import Field

from src.utils.utils import CamelModel


class MovieBase(CamelModel):
    year: Optional[int] = Field(None)
    title: Optional[str] = Field(None)
    studios: Optional[str] = Field(None)
    producers: Optional[str] = Field(None)
    winner: Optional[bool] = Field(None)


class MovieCreate(MovieBase):
    year: int
    title: str
    studios: str
    producers: str
    winner: bool


class MovieUpdate(MovieBase):
    ...


class MovieInDBBase(MovieBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class Movie(MovieInDBBase):
    ...


class MovieResponse(CamelModel):
    result: Movie


class MovieListResponse(CamelModel):
    result: Sequence[Movie]
