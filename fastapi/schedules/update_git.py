import time

from loguru import logger

import git
from external import environ
from helpers.schedule_logger import schedule_logger
from services.scheduler import scheduler


@scheduler.scheduled_job('interval', seconds=10)
@schedule_logger
def scheduled_git_pull():
    logger.debug("Trying to pull git repository")
    if not environ.TK_GIT_ROOT_PATH.exists():
        logger.error(f"{environ.TK_GIT_ROOT_PATH} does not exist. Exiting.")
        raise FileNotFoundError(f"{environ.TK_GIT_ROOT_PATH} does not exist. Exiting.")
    logger.debug("Pulling git repository")
    g = git.cmd.Git(environ.TK_GIT_ROOT_PATH.as_posix())
    g.pull()
    logger.success("Git repository pulled successfully")


# @scheduler.scheduled_job('interval', seconds=30)
# def sleeping_schedule():
#     # Sleep for 15 seconds
#     logger.debug("Sleeping for 15 seconds")
#     time.sleep(15)
#     logger.debug("Woke up from sleep")
#
# @scheduler.scheduled_job('interval', seconds=10)
# def sleeping_schedule():
#     # Sleep for 3 seconds
#     logger.debug("Sleeping for 3 seconds")
#     time.sleep(3)
#     logger.debug("Woke up from sleep")
#
#
# @scheduler.scheduled_job('interval', seconds=10)
# def heavy_calculations():
#     # Sleep for 3 seconds
#     logger.debug("Starting heavy calculation")
#     timer = time.time()
#     sum = 0
#     count = 0
#     avg = 0
#     for i in range(10**7):
#         sum += i
#         count = i + 1
#         avg = sum / count
#
#     logger.debug(f"Heavy calculation took {time.time() - timer} seconds. Result: {avg}")
