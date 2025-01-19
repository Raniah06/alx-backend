import Redis from 'ioredis';

// Create a new Redis client instance
const redis = new Redis();

// Event listener for successful Redis connection
redis.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for Redis errors
redis.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to set multiple fields in a hash
function createHash() {
  redis.hset('ALX', 'Portland', 50, redis.print);
  redis.hset('ALX', 'Seattle', 80, redis.print);
  redis.hset('ALX', 'New York', 20, redis.print);
  redis.hset('ALX', 'Bogota', 20, redis.print);
  redis.hset('ALX', 'Cali', 40, redis.print);
  redis.hset('ALX', 'Paris', 2, redis.print);
}

// Function to display the hash stored in Redis
function displayHash() {
  redis.hgetall('ALX', (err, result) => {
    if (err) {
      console.error(`Error fetching hash: ${err.message}`);
      return;
    }
    console.log(result);  // Output the full hash object
  });
}

// Operations to execute
createHash();   // Create and store the hash
displayHash();  // Retrieve and display the hash
