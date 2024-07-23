import { createClient } from 'redis';

const client = createClient({
  password: 'eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'
});
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect().then(() => console.log('Redis Connected'));

export default client;
