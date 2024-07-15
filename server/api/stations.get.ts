import { DuckDbError } from 'duckdb';
import { IStation } from '~/types/stations';

export default defineEventHandler(async (event): Promise<IStation[]> => {
  return new Promise((resolve, reject) => {
    event.context.duckdb.connection.all(
      'SELECT * FROM stations',
      (err: DuckDbError, res: IStation[]) => {
        if (err) {
          console.error(err);
          Promise.reject(err);
        } else {
          Promise.resolve(res);
        }
      }
    );
  });
});
