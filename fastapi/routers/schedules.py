from schedules.update_git import scheduled_git_pull
from helpers.schedule_logger import read_logs
from fastapi import APIRouter

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"],
)


@router.put("/trigger")
async def start_schedule():
    scheduled_git_pull()


@router.get("/logs")
async def get_schedule_logs():
    return read_logs()
