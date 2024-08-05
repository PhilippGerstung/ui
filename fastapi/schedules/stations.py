from external import environ
from external.duck_db import db
from helpers.schedule_logger import schedule_logger
from loguru import logger


@schedule_logger
def load_stations():
    logger.debug("Loading stations")
    stations_file_path = environ.TK_GIT_ROOT_PATH / "stations/stations.csv"
    if not stations_file_path.exists():
        raise FileNotFoundError(f"{stations_file_path} does not exist. Exiting.")
    db.execute(f"""
        BEGIN TRANSACTION;
        DROP TABLE IF EXISTS stations;
        CREATE TABLE stations AS FROM '{stations_file_path.as_posix()}';
        COMMIT;
    """)
    logger.success("Stations loaded successfully")


if __name__ == "__main__":
    load_stations()