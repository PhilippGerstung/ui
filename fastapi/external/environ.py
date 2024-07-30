import os

TK_API_KEY = os.environ["TK_API_KEY"]
USE_FAKE_REDIS = os.environ.get("USE_FAKE_REDIS", "false").lower() == "true"
REDIS_URL = os.environ["REDIS_URL"]
