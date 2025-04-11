import pathlib

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    SQLITE3_DB_URI: str
    ENVIRONMENT: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
