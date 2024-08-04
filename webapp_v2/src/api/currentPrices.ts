import { LocationPricesSchema, type LocationPrices } from "@/types/currentPrices";


export async function getCurrentPricesForLocation(latitude: number, longitude: number): Promise<LocationPrices> {
    const response = await fetch(`http://localhost:8000/prices/current_prices?lat=${latitude}&lon=${longitude}`);
    const data = await response.json();
    return LocationPricesSchema.parse(data);
}