import duckdb

from external.environ import DUCK_DB_PATH


def create_db_if_not_exist():
    if not DUCK_DB_PATH.exists():
        temp_db = duckdb.connect(database=DUCK_DB_PATH.as_posix(), read_only=False)
        temp_db.execute("CREATE TABLE CREATION_INFO (created_at TIMESTAMP)")
        temp_db.execute("INSERT INTO CREATION_INFO VALUES (NOW())")
        temp_db.close()
        duckdb.close()

    db_readonly = duckdb.connect(database=DUCK_DB_PATH.as_posix(), read_only=True)
    return db_readonly


db = create_db_if_not_exist()
