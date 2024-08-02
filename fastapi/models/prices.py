from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GasType(str, Enum):
    diesel = "diesel"
    e5 = "e5"
    e10 = "e10"


class RecommendedWeekday(BaseModel):
    weekday_prices: dict[int, float]
    best_weekday: int
    current_weekday: int


class Station(BaseModel):
    id: str
    name: str
    brand: str
    street: str
    place: str
    lat: float
    lng: float
    dist: float
    diesel: Optional[float]
    e5: Optional[float]
    e10: Optional[float]
    isOpen: bool  # noqa: N815
    houseNumber: str  # noqa: N815
    postCode: int  # noqa: N815


class LocationPrices(BaseModel):
    ok: bool
    license: str
    data: str
    status: str
    stations: List[Station]
