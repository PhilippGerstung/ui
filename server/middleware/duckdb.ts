import duckdb from 'duckdb';
import { DB_FILE_PATH } from '~/config/paths';

const Db = new duckdb.Database(DB_FILE_PATH);

export default defineEventHandler(async (event) => {
  console.log("Adding duckdb middleware")
  event.context.duckdb = Db;
  console.log("DuckDB addded", event.context.duckdb)
});
