import Redis from 'ioredis';

// Create a new Redis client instance
const redis = new Redis();

redis.on('connect', () => {
  console.log('Redis client connected to the server');
});

redis.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
