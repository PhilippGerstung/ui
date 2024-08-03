import time
from datetime import datetime

from loguru import logger
from external.duck_db import db
import uuid


def schedule_logger(func):
    """
    This decorator is used to log the execution times and exceptions of a function.
    Results are written to the duckdb database.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_ts = datetime.now()
        uuid_str = str(uuid.uuid4())
        db.execute("INSERT INTO schedules VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (uuid_str, str(func.__name__), start_ts, None, None, None, None))
        exception = None
        stacktrace = None
        success = True
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = None
            exception = str(e)
            stacktrace = str(e.__traceback__)
            success = False
            raise
        finally:
            end_time = time.time()
            logger.debug(f"Function {func.__name__} took {end_time - start_time} seconds.")
            # Update the row with the end time and success status
            db.execute("UPDATE schedules SET finished = ?, success = ?, message = ?, stacktrace = ? WHERE uuid = ?",
                       (datetime.now(), success, exception, stacktrace, uuid_str))
        return result

    return wrapper
