import { z } from 'zod';

export const CitySchema = z.object({
    post_code: z.string(),
    city: z.string(),
    lat: z.number(),
    lon: z.number(),
});

export type City = z.infer<typeof CitySchema>;