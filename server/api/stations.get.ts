import { IStation } from "~/types/stations"

export default defineEventHandler(async (event): Promise<IStation[]> => {
  await setTimeout(() => Promise.resolve(), 1000);
  return [
    { uuid: "1", name: "Station 1" },
    { uuid: "2", name: "Station 2" },
    { uuid: "3", name: "Station 3" }
  ]
})
