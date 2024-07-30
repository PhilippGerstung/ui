import duckdb from 'duckdb';

console.log("Hello, DuckDB!");

const DB_FILE_PATH = 'C:/Users/mail/Development/GPV/data/gpv.db';
const db = new duckdb.Database(DB_FILE_PATH);
db.all('SELECT * from stations limit 3', function(err, res) {
    if (err) {
      console.warn(err);
      return;
    }
    console.log(res)
  });