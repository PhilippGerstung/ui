import { Db, initPlzTableIfNotExist } from "~/config/duckdb";
import redis from "~/config/redis";

export default defineEventHandler(async (event) => {
  return new Promise(async (resolve, reject) => {
    const query = getQuery(event);
    await initPlzTableIfNotExist();
    Db.all(`SELECT * FROM plz WHERE city LIKE '%${query.search}%' or plz.plz like '%${query.search}%'`, function(err, res) {
      if(err) {
        console.error("Error getting PLZ from duckdb", err);
        reject(err);
      }
      else {
        console.log("PLZ search result", res);
        resolve(res);
      }
    });
  });
})
