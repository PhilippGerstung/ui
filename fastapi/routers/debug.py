import glob
import os

from fastapi import APIRouter

import external.environ

router = APIRouter(
    prefix="/debug",
    tags=["debug"],
)


@router.get("/env_vars")
def print_all_env_vars():
    return {
        "TK_API_KEY": external.environ.TK_API_KEY,
        "USE_FAKE_REDIS": external.environ.USE_FAKE_REDIS,
        "REDIS_URL": external.environ.REDIS_URL,
        "DUCK_DB_PATH": external.environ.DUCK_DB_PATH,
        "TK_GIT_ROOT_PATH": external.environ.TK_GIT_ROOT_PATH,
        "MAX_HISTORIC_DAYS": external.environ.MAX_HISTORIC_DAYS,
    }


@router.get("os.environ")
def get_os_environ():
    return os.environ


@router.get("/list_files_in_path")
def list_files_in_path(path: str):
    return [f for f in glob.glob(path + "/**/*", recursive=True) if os.path.isfile(f)]
