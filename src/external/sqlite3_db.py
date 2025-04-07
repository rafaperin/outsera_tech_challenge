from typing import Any, Dict, Generator
from sqlalchemy import create_engine, JSON
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config.environment import settings


class Base(DeclarativeBase):
    type_annotation_map = {
        Dict[str, Any]: JSON
    }


engine = create_engine(settings.SQLITE3_DB_URI)
Base.metadata.create_all(engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
