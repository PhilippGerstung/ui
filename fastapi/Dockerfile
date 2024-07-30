FROM python:3.12.4-slim-bookworm
# Install poetry
ENV POETRY_VERSION 1.8.3
RUN set -ex; pip install --no-cache-dir poetry==$POETRY_VERSION;

COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-dev

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]