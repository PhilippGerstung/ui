from typing import List

from fastapi import APIRouter

from external.duck_db import db
from models.geo import City

router = APIRouter(
    prefix="/stations",
    tags=["stations"],
)


@router.get("/")
def get_stations():
    stations = db.execute("SELECT * FROM stations LIMIT 50").fetchall()
    return stations


@router.get("/{query}")
def search_cities_query(query: str) -> List[City]:
    if len(query) <= 2:
        return []
    cities = db.execute(f"""
        SELECT post_code, MIN(city), MIN(latitude), MIN(longitude) 
        FROM stations 
        WHERE post_code ILIKE '%{query}%' or city ILIKE '%{query}%'
        GROUP BY post_code 
        ORDER BY post_code
        LIMIT 15""").fetchall()
    cities: List[City] = [City(post_code=city[0], city=city[1], lat=city[2], lon=city[3]) for city in cities]
    return cities