import { LocationPricesSchema, type LocationPrices } from "~/types/currentPrices";

export async function getPricesForLocation(latitude: number, longitude: number, radius: number = 1.5): Promise<LocationPrices> {
    return new Promise((resolve, reject) => {
        fetch(`https://creativecommons.tankerkoenig.de/json/list.php?lat=${latitude}&lng=${longitude}&rad=${radius}&sort=dist&type=all&apikey=${process.env.TK_API_KEY}`)
        .then(async (res)=>{
            const result = await res.json();
            const parsed = LocationPricesSchema.safeParse(result);
            if (!parsed.success) {
                throw new Error("Invalid response from Tankerkoenig API", parsed.error);
            }
            resolve(parsed.data);
        }).catch((e) => console.error(e));
    });
}