from datetime import datetime

from external import environ
from external.duck_db import db
from external.historic_data import get_prices_file_paths
from helpers.schedule_logger import schedule_logger
from loguru import logger

@schedule_logger
def load_historic_prices():
    """Loads the historic prices data to the DUCKDB and removes the old data using a transaction."""

    start_date = datetime.now().date() - environ.MAX_HISTORIC_DAYS
    file_paths = [path.as_posix() for date, path in get_prices_file_paths().items() if date >= start_date]
    if len(file_paths) == 0:
        raise ValueError(f"No files found to load historic prices before {start_date}")
    db.execute(f"""
        BEGIN TRANSACTION;
        DROP TABLE IF EXISTS historic_prices;
        CREATE TABLE historic_prices AS FROM read_csv(['{"', '".join(file_paths)}']);
        COMMIT;
    """)
    logger.success("Historic prices loaded successfully")


if __name__ == "__main__":
    load_historic_prices()