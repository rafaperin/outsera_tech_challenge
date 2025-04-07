import csv

from src.external.sqlite3_db import session
from src.models.movies_orm import Movies


def insert_csv_to_memory_db():
    with open("csv/movielist.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            movie = Movies(
                year=int(row['year']),
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=row['winner'].strip().lower() == 'yes'
            )
            session.add(movie)

    session.commit()

    return session