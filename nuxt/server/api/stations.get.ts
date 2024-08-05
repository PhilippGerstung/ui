import {Database, DuckDbError } from 'duckdb';
import { IStation } from '~/types/stations';
import { DB_FILE_PATH } from '~/config/paths';

export default defineEventHandler(async (event): Promise<IStation[]> => {
  return new Promise((resolve, reject) => {
    
    event.context.duckdb.all('SELECT * from stations limit 5', function(err: any, res: IStation[]) {
      if (err) {
        console.warn(err);
        reject(err);
        return;
      }
      resolve(res);
    });
  });
});
