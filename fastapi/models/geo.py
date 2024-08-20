from pydantic import BaseModel


class GeoSquare(BaseModel):
    min_lat: float
    max_lat: float
    min_lon: float
    max_lon: float


class City(BaseModel):
    post_code: str
    city: str
    lat: float
    lon: float
