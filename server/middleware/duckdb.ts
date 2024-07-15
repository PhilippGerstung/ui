import duckdb from 'duckdb';
import { DB_FILE_PATH } from '~/config/paths';

const Db = new duckdb.Database(DB_FILE_PATH);

export default defineEventHandler(async (event) => {
  event.context.duckdb = {
    connection: Db.connect()
  };
});
