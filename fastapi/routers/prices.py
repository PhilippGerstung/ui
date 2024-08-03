from fastapi import APIRouter

from external import tankerkoenig
from models.prices import LocationPrices

router = APIRouter(
    prefix="/prices",
    tags=["prices"],
)

@router.get("/compare")
async def compare_prices():
    pass


@router.get("/current_prices")
async def get_current_prices(lat: float = 48.1807, lon: float = 11.4609) -> LocationPrices:
    return await tankerkoenig.get_prices(lat, lon, 10)

