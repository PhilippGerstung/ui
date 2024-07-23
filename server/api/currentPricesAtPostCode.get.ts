import redis from "~/config/redis";
import { REDIS_CACHE_PRICES_EXPIRATION_SECS } from '~/config/constants';
import { getPricesForLocation } from "~/api/tk";
import { LocationPrices } from "~/types/currentPrices";


interface ExtendedStationPrices extends LocationPrices {
  cached: boolean;
}

export default defineEventHandler(async (event): Promise<ExtendedStationPrices> => {
  const lat = 49.480808
  const long = 8.441430

  const cached = await redis.get(`prices:${lat.toFixed(2)}:${long.toFixed(2)}`);
  if(cached){
    const res: ExtendedStationPrices = JSON.parse(cached);
    res.cached = true;
    return res;
  }

  else {
    const prices = await getPricesForLocation(lat, long, 10);
    await redis.set(`prices:${lat.toFixed(2)}:${long.toFixed(2)}`, JSON.stringify(prices), { EX: REDIS_CACHE_PRICES_EXPIRATION_SECS });
    const res: ExtendedStationPrices = {...prices, cached: false};
    return res;
  }
})
