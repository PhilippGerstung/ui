FROM python:3.12.4-slim-bookworm
# Install poetry
ENV POETRY_VERSION 1.8.3

ENV TK_GIT_ROOT_PATH="/data/tk_git_root"
ENV DUCK_DB_FILE_PATH="/data/duck_db.db"

RUN set -ex; pip install --no-cache-dir poetry==$POETRY_VERSION;
RUN apt-get update && apt-get install -y git

COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-dev

COPY . .

RUN export TK_GIT_ROOT_PATH="/data/tk_git_root"
RUN export DUCK_DB_FILE_PATH="/data/duck_db.db"

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
