import { BACKEND_URL } from "@/config/envVars";
import { get } from "@/helper/fetchHelper";
import { CitySchema, type City } from "@/types/stations";

export async function getCities(
    query: string
): Promise<City[]> {
    return get(`${BACKEND_URL}/stations/${query}`, CitySchema.array());
}