import httpx
from loguru import logger

from external.environ import TK_API_KEY
from helpers.cacher import redis_cache
from models.prices import LocationPrices


@redis_cache(ttl=60, cachekey=lambda latitude, longitude, radius: f"prices-{latitude:.4f}-{longitude:.4f}-{radius:.1f}")
async def get_prices(latitude: float, longitude: float, radius: float) -> LocationPrices:
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"https://creativecommons.tankerkoenig.de/json/list.php?lat={latitude}&lng={longitude}&rad={radius}&sort=dist&type=all&apikey={TK_API_KEY}"
        )

    if res.status_code != 200:
        raise logger.error(f"Failed to fetch prices: {res.text}")

    parsed = LocationPrices(**res.json())
    if not parsed.ok:
        raise logger.error(f"Failed to fetch prices: {parsed.status}")

    return parsed
