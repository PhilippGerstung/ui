import { PlzSchema, type IPlz } from "~/types/plz";
import plzData from "~/data/plz.json";

export function loadPlz(): IPlz[] {
    const parsed = PlzSchema.array().safeParse(plzData);
    if(!parsed.success) {
        console.error("Error parsing PLZ data", parsed.error);
        throw new Error("Error parsing PLZ data");
    }
    return parsed.data;
}