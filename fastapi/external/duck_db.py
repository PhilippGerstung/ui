import duckdb
from loguru import logger

from external.environ import DUCK_DB_PATH


def create_db_if_not_exist():
    if not DUCK_DB_PATH.exists():
        DUCK_DB_PATH.parent.resolve().mkdir(exist_ok=True, parents=True)
        temp_db = duckdb.connect(database=DUCK_DB_PATH.as_posix(), read_only=False)
        temp_db.execute("CREATE TABLE CREATION_INFO (created_at TIMESTAMP)")
        temp_db.execute("INSERT INTO CREATION_INFO VALUES (NOW())")
        temp_db.close()
        duckdb.close()

    productive_db = duckdb.connect(database=DUCK_DB_PATH.as_posix(), read_only=False)
    productive_db.execute(
        "CREATE TABLE IF NOT EXISTS schedules (uuid VARCHAR NOT NULL UNIQUE, fun VARCHAR, started TIMESTAMP, finished TIMESTAMP, success BOOLEAN,  message VARCHAR, stacktrace VARCHAR)")
    return productive_db


db = create_db_if_not_exist()
