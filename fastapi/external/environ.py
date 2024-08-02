import os
import pathlib as pl


TK_API_KEY = os.environ["TK_API_KEY"]
USE_FAKE_REDIS = os.environ.get("USE_FAKE_REDIS", "false").lower() == "true"
REDIS_URL = os.environ["REDIS_URL"]
DUCK_DB_PATH = pl.Path(os.environ["DUCK_DB_FILE_PATH"]).resolve()
