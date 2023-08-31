FROM python:3.11.5

WORKDIR /app

COPY proxy .
COPY poetry.lock .
COPY pyproject.toml .

RUN python3 -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

EXPOSE 8080
CMD ["gunicorn","--bind","0.0.0.0:8080","proxy:app"]