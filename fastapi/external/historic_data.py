from datetime import date
from typing import Dict
import pathlib as pl
import glob

from external import environ

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


if __name__ == "__main__":
    print(get_prices_file_paths())