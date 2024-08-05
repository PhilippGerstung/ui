import { z } from "zod";

export const PlzSchema = z.object({
    plz: z.number(),
    city: z.string(),
    lat: z.number(),
    lon: z.number()
});

export type IPlz = z.infer<typeof PlzSchema>;