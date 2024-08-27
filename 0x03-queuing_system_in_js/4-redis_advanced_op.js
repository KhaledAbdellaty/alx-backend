import { createClient, print } from "redis";

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
}).on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const hashObj = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};

for (const [key, value] of Object.entries(hashObj)) {
  client.hset('HolbertonSchools', key, value, print);
}

client.hgetall('HolbertonSchools', (_err, res) => {
  console.log(res);
});
