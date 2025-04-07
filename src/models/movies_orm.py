from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import Mapped

from src.external.sqlite3_db import Base


class Movies(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = Column(Integer, primary_key=True)
    year: Mapped[int] = Column(Integer)
    title: Mapped[str] = Column(String)
    studios: Mapped[str] = Column(String)
    producers: Mapped[str] = Column(String)
    winner: Mapped[bool] = Column(Boolean)
