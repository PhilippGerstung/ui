import redis from "~/config/redis";
import { REDIS_CACHE_PRICES_EXPIRATION_SECS } from '~/config/constants';
import { getPricesForLocation } from "~/api/tk";
import { LocationPrices } from "~/types/currentPrices";


export interface ExtendedStationPrices extends LocationPrices {
  cached: boolean;
}

export default defineEventHandler(async (event): Promise<ExtendedStationPrices> => {
  const query = getQuery(event);
  if (!query.lat || !query.lon) {
    throw new Error('Missing lat or lon query parameter');
  }

  const lat = parseFloat(query.lat.toString());
  const long = parseFloat(query.lon.toString());

  const redisKey = `prices:${lat.toFixed(2)}:${long.toFixed(2)}`;

  const cached = await redis.get(redisKey);
  if (cached) {
    const res: ExtendedStationPrices = JSON.parse(cached);
    res.cached = true;
    return res;
  }

  else {
    const prices = await getPricesForLocation(lat, long, 10);
    await redis.set(redisKey, JSON.stringify(prices), { EX: REDIS_CACHE_PRICES_EXPIRATION_SECS });
    const res: ExtendedStationPrices = { ...prices, cached: false };
    return res;
  }
})
