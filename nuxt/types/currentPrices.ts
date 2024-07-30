import { z } from "zod";

// Define the schema for a station object
const StationSchema = z.object({
  id: z.string().uuid(),
  name: z.string(),
  brand: z.string(),
  street: z.string(),
  place: z.string(),
  lat: z.number(),
  lng: z.number(),
  dist: z.number(),
  diesel: z.number(),
  e5: z.number(),
  e10: z.number(),
  isOpen: z.boolean(),
  houseNumber: z.string(),
  postCode: z.number()
});

// Define the schema for the main JSON structure
export const LocationPricesSchema = z.object({
  ok: z.boolean(),
  license: z.string(),
  data: z.string(),
  status: z.string(),
  stations: z.array(StationSchema)
});

// TypeScript types can be inferred from the schema
export type Station = z.infer<typeof StationSchema>;
export type LocationPrices = z.infer<typeof LocationPricesSchema>;

