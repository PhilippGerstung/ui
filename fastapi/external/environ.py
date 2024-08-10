import os
import pathlib as pl
from datetime import timedelta

import dotenv

dotenv.load_dotenv()
TK_API_KEY = os.environ["TK_API_KEY"]
USE_FAKE_REDIS = os.environ.get("USE_FAKE_REDIS", "false").lower() == "true"
REDIS_URL = os.environ["REDIS_URL"]
REDIS_PORT = os.environ["REDIS_PORT"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
DUCK_DB_PATH = pl.Path(os.environ["DUCK_DB_FILE_PATH"]).resolve()
TK_GIT_ROOT_PATH = pl.Path(os.environ["TK_GIT_ROOT_PATH"]).resolve()
MAX_HISTORIC_DAYS = timedelta(days=int(os.environ["MAX_HISTORIC_DAYS"]))
