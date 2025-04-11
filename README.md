# Golden Raspberry Awards API

This project is a RESTful web service built with FastAPI to expose information about the “Worst Picture” category of the Golden Raspberry Awards (a.k.a. Razzies). The API loads data from a CSV file at startup and allows querying producers with the longest and shortest intervals between awards.

Features
	•	Automatic CSV loading: The film data is loaded into an in-memory database when the application starts.
	•	RESTful API (Richardson Maturity Model Level 2): Resources are properly exposed using HTTP verbs and status codes.
	•	Producer interval analysis: Get the producer with the shortest and longest intervals between consecutive awards.
	•	Integration-tested: The system includes integration tests to ensure the results are accurate and consistent with the provided dataset.
	•	Zero-install database: Uses an in-memory SQLite database (embedded and self-contained).


# How to Run the Project

Prerequisites
	•	Python 3.12+
	•	poetry for dependency management
	•	Docker (alternative)

# Running Locally

## Install dependencies
poetry env activate
poetry install

## Setup Environment Variables
Rename example.env to .env

## Start the app
uvicorn src.app:app --port 8000 --reload

This will:
	•	Load the film data from the provided CSV
	•	Start the API server at http://localhost:8000

# Running with Docker

## Setup Environment Variables
Rename example.env to .env

## Building Container
sudo docker build -t golden-raspberry-api .

## Running Container
sudo docker run -p 8000:8000 golden-raspberry-api

# Running Tests
Simply use the command: pytest
