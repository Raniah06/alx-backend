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

// Subscribe to the channel ALXchannel
redis.subscribe('ALXchannel', (err, count) => {
  if (err) {
    console.error(`Failed to subscribe: ${err.message}`);
  } else {
    console.log(`Subscribed to ${count} channel(s)`);
  }
});

// Listen for messages on the ALXchannel
redis.on('message', (channel, message) => {
  console.log(message); // Log the message

  // If the message is "KILL_SERVER", unsubscribe and quit
  if (message === 'KILL_SERVER') {
    redis.unsubscribe('ALXchannel', () => {
      console.log('Unsubscribed from ALXchannel');
      redis.quit(); // Close the Redis connection
    });
  }
});
