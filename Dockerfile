FROM python:3.11.5

WORKDIR /app

COPY app .
COPY poetry.lock .
COPY pyproject.toml .

RUN python3 -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENTRYPOINT [ "gunicorn --bind 0.0.0.0:8080 app:app" ]