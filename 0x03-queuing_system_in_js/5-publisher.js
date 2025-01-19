import Redis from 'ioredis';

// Create a Redis client instance
const redis = new Redis();

// Event listener for successful Redis connection
redis.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for Redis errors
redis.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    redis.publish('ALXchannel', message); // Publish the message to the ALXchannel
  }, time);
}

// Publish messages with different delays
publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
