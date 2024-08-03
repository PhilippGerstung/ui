from fastapi import APIRouter

from external.duck_db import db

router = APIRouter(
    prefix="/stations",
    tags=["stations"],
)

@router.get("/")
async def get_stations():
    stations = db.execute("SELECT * FROM stations LIMIT 50").fetchall()
    return stations