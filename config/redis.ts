import { createClient } from 'redis';
import path from "path";
import fs from "fs";
import csv from 'csv-parser';

const client = createClient({
  password: 'eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'
});
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect().then(() => {
  console.log('Redis Connected');
    // Path to the CSV file
const csvFilePath = path.join('./data/plz.csv');

// Read and process the CSV file
  fs.createReadStream(csvFilePath)
    .pipe(csv({ separator: ';' }))
    .on('data', (row) => {
      const key = `plz_${row["plz"]}`; // Use the first cell as the key with prefix 'plz_'
      client.set(key, JSON.stringify(row));
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      client.quit();
    });
  }
);

export default client;
