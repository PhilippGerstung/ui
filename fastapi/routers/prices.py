from fastapi import APIRouter

from external import tankerkoenig, historic_data
from models.prices import LocationPrices, GasType, PriceComparisonResult
from services import prices

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


@router.post("/compare_to_average/{station_uuid}")
async def compare_to_average(station_uuid: str, gas_type: GasType, reference_price: float) -> PriceComparisonResult:
    comparison_data = historic_data.get_prices_for_station_between(station_uuid, gas_type)
    result = prices.compare_prices(reference_price, comparison_data)
    return result