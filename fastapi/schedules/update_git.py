import time

from loguru import logger

import git
from external import environ
from helpers.schedule_logger import schedule_logger
from schedules.historic_prices import load_historic_prices
from schedules.stations import load_stations
from services.scheduler import scheduler


# @scheduler.scheduled_job('interval', seconds=10)
@scheduler.scheduled_job('interval', hours=6)
@schedule_logger
def scheduled_git_pull():
    logger.debug("Trying to pull git repository")
    if not environ.TK_GIT_ROOT_PATH.exists():
        logger.warning(f"{environ.TK_GIT_ROOT_PATH} does not exist. Creating a new git repository")
        # TODO create git repository and clone from TK_GIT_REPO_URL
        raise FileNotFoundError(f"{environ.TK_GIT_ROOT_PATH} does not exist. Exiting.")
    logger.debug("Pulling git repository")
    g = git.cmd.Git(environ.TK_GIT_ROOT_PATH.as_posix())
    g.pull()
    logger.success("Git repository pulled successfully")

    load_stations()
    load_historic_prices()


