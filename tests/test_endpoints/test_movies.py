from src.schemas.movies_schema import ProducerIntervalResponse
from unittest.mock import AsyncMock, patch
import pytest


@pytest.mark.asyncio
def test_movies_db_loaded(setup_mock_database):
    conn = setup_mock_database
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]

    assert count > 0, "Expected movies to be loaded from CSV"


@pytest.mark.asyncio
@pytest.mark.usefixtures("setup_mock_database")
async def test_get_all_winners_schema_validation(async_client):
    with patch("src.api.endpoints.movies_api.MoviesController.get_all_winners"):
        response = await async_client.get("/movies/winners")

    assert response.status_code == 200
    assert ProducerIntervalResponse(**response.json())


@pytest.mark.asyncio
async def test_get_all_winners_failure(async_client):
    with patch(
        "src.api.endpoints.movies_api.MoviesController.get_all_winners",
        new=AsyncMock(side_effect=Exception("Fail"))
    ):
        response = await async_client.get("/movies/winners")

    assert response.status_code == 500
    assert response.json()["message"] == "Oops! Something went wrong, please try again later..."
