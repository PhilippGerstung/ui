import dotenv
dotenv.load_dotenv()

import datetime
from fastapi import FastAPI
import uvicorn

from external.duck_db import db
from external import tankerkoenig
from helpers.geo import calculate_square
from models.prices import GasType, RecommendedWeekday, LocationPrices

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/stations")
async def get_stations():
    stations = db.execute("SELECT * FROM stations LIMIT 50").fetchall()
    return stations


@app.get("/recommendations/weekdays")
async def get_best_weekday(lat: float = 48.1807, lon: float = 11.4609, gas_type: GasType = "e5") -> RecommendedWeekday:
    geo_square = calculate_square(lat, lon, 20)

    query = f"""
    SELECT uuid FROM stations
    WHERE latitude BETWEEN {geo_square.min_lat} AND {geo_square.max_lat} AND 
        longitude BETWEEN {geo_square.min_lon} AND {geo_square.max_lon}
    """
    uuids = db.execute(query).fetchall()
    uuids = [uuid[0] for uuid in uuids]
    if not uuids:
        raise ValueError("No stations found in the area")

    avg_prices_weekday_query = f"""
        SELECT weekday, AVG(median_{gas_type.value}) from main.gas_prices_view
        WHERE station_uuid IN ('{"','".join(uuids)}') 
        GROUP BY weekday
    """

    avg_prices_weekday = db.execute(avg_prices_weekday_query).fetchall()

    weekday_prices = RecommendedWeekday(weekday_prices={}, best_weekday=-1, current_weekday=datetime.datetime.now().weekday())
    lowest_price = float('inf')
    for row in avg_prices_weekday:
        weekday_prices.weekday_prices[row[0]] = row[1]
        if row[1] < lowest_price:
            lowest_price = row[1]
            weekday_prices.best_weekday = row[0]

    return weekday_prices


@app.get("/current_prices")
async def get_current_prices(lat: float = 48.1807, lon: float = 11.4609) -> LocationPrices:
    return await tankerkoenig.get_prices(lat, lon, 10)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
