import { z } from 'zod';

const PeriodSchema = z.object({
  startp: z.string(), // "HH:mm" format
  endp: z.string() // "HH:mm" format
});

const OpeningTimeSchema = z.object({
  applicable_days: z.number(), // Bitfield representing applicable days
  periods: PeriodSchema.array()
});

const OverrideSchema = z.object({
  startp: z.string(), // "YYYY-MM-DD HH:mm" format
  endp: z.string(), // "YYYY-MM-DD HH:mm" format
  is_close: z.boolean()
});

const OtJsonSchema = z.object({
  openingTimes: OpeningTimeSchema.array().optional(),
  overrides: OverrideSchema.array().optional()
});

export const StationSchema = z.object({
  uuid: z.string(),
  name: z.string(),
  brand: z.string(),
  street: z.string(),
  house_number: z.string(),
  post_codde: z.string(),
  city: z.string(),
  longitude: z.number(),
  latitude: z.number(),
  first_active: z.string(),
  openingtimes_json: OtJsonSchema
});

export type IStation = z.infer<typeof StationSchema>;
export type IOtJson = z.infer<typeof OtJsonSchema>;
