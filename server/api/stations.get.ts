import { IStation } from "~/types/stations"

export default defineEventHandler(async (event): Promise<IStation[]> => {
  await setTimeout(() => Promise.resolve(), 1000);
  return []
})
