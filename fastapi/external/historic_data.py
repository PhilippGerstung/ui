from datetime import date, datetime, timedelta
from typing import Dict
import pathlib as pl
import glob

from external import environ
from external.duck_db import db
from models.prices import GasType

_STATIONS_ROOT_PATH = environ.TK_GIT_ROOT_PATH / "prices"


def get_prices_file_paths() -> Dict[date, pl.Path]:
    """
    Gets all file paths with their date as key and the pathlib path as value
    """
    station_files = {}
    csv_files = glob.glob(f"{_STATIONS_ROOT_PATH}/**/*-prices.csv", recursive=True)
    for file in csv_files:
        path = pl.Path(file)
        date_str = path.stem.replace("-prices", "")
        date_obj = date.fromisoformat(date_str)
        station_files[date_obj] = pl.Path(file)
    return station_files


def get_prices_for_station_between(station_uuid: str, gas_type: GasType, from_timestamp: datetime = None,
                                   to_timestamp: datetime = None) -> Dict[datetime, float]:
    """
    Gets all prices for a station between two timestamps. If no timestamps is given, the last week is taken
    """
    if from_timestamp is None:
        from_timestamp = datetime.now() - timedelta(days=7)
    if to_timestamp is None:
        to_timestamp = datetime.now()

    data = db.execute(f"""
        SELECT date, {gas_type.value} as price
        FROM historic_prices
        WHERE station_uuid = '{station_uuid}' AND 
            date BETWEEN '{from_timestamp}' AND '{to_timestamp}' AND 
            ({gas_type.value} IS NOT NULL or {gas_type.value} != 0)
    """).fetchall()
    converted = {
        row[0]: row[1]
        for row in data
    }
    return converted


if __name__ == "__main__":
    # print(get_prices_file_paths())
    print(get_prices_for_station_between("927d68a9-a8c3-4dbe-5c18-93aa8e8818c9", GasType.e5))
