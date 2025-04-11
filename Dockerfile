FROM python:3.12

RUN addgroup --system app && adduser --system --group app

WORKDIR /src/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TESTING=0

RUN curl -sSL --insecure https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml ./poetry.lock* /

ARG INSTALL_DEV=false

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root ; fi"

COPY ./src /src
COPY .env /src
COPY ./csv /src/csv

ENV PYTHONPATH=/

RUN chown -R app:app /src

USER app

CMD ["uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
