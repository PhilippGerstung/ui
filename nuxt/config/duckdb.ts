import path from "path";
import duckdb, { type RowData } from 'duckdb';
import { DB_FILE_PATH } from '~/config/paths';

// Path to the CSV file
const csvFilePath = path.join('./data/plz.csv');


export const Db = new duckdb.Database(DB_FILE_PATH);

export async function initPlzTableIfNotExist(): Promise<void>{
    return new Promise((resolve, reject) => {
        Db.all("SHOW TABLE", (err, res) => {
            if(err){
                console.error(err);
                reject();
                return;
            }
            console.log("Tables", res);
            if(res.some((table: RowData) => table[0] === "plz")){
                resolve();
                return;
            }
            Db.all(`CREATE TABLE IF NOT EXISTS plz (
                plz VARCHAR,
                city VARCHAR,
                lat FLOAT,
                lon FLOAT
                ); COPY plz FROM '${csvFilePath}'`, function(err, res) {
                if(err) {
                    console.error(err);
                    reject();
                }
                else console.log("Table plz created", res);
                resolve();
            })
        });
    })
}

  