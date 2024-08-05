import { Db } from "~/config/duckdb";

export default defineEventHandler(async (event) => {
  // console.log("Adding duckdb middleware")
  // event.context.duckdb = Db;
  // console.log("DuckDB addded", event.context.duckdb)
});
