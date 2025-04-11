import csv
import sqlite3
import pytest

from httpx import AsyncClient, ASGITransport
from src.app import app
from src.config.environment import settings
from src.utils.data_sorting import CSV_PATH


@pytest.fixture
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
def setup_mock_database():
    conn = sqlite3.connect(settings.SQLITE3_DB_URI)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE movies (year INTEGER, title TEXT, studios TEXT, producers TEXT, winner TEXT)")

    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = [
            (int(row['year']), row['title'], row['studios'], row['producers'], row['winner'])
            for row in reader
        ]
        cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", rows)

    conn.commit()

    yield conn

    conn.close()
