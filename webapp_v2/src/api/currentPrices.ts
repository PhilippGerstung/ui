import { BACKEND_URL } from '@/config/envVars'
import { get } from '@/helper/fetchHelper';
import { LocationPricesSchema, type LocationPrices } from '@/types/currentPrices'

export async function getCurrentPricesForLocation(
  latitude: number,
  longitude: number
): Promise<LocationPrices> {
  return get(`${BACKEND_URL}/prices/current_prices?lat=${latitude}&lon=${longitude}`, LocationPricesSchema);
}
