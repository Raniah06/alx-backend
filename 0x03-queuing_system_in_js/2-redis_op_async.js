import Redis from 'ioredis';
import { promisify } from 'util';

// Create a new Redis client instance
const redis = new Redis();

// Promisify the redis.get method to use with async/await
const getAsync = promisify(redis.get).bind(redis);

// Event listener for successful Redis connection
redis.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for Redis errors
redis.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
  redis.set(schoolName, value, redis.print);  // `redis.print` will print a confirmation message
}

// Function to display the value of a school from Redis (now using async/await)
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);  // Output the value stored for the given school name
  } catch (err) {
    console.error(`Error fetching school value: ${err.message}`);
  }
}

// Operations to call in sequence
displaySchoolValue('ALX');                  // Attempt to display value for 'ALX'
setNewSchool('ALXSanFrancisco', '100');     // Set value for 'ALXSanFrancisco'
displaySchoolValue('ALXSanFrancisco');     // Display value for 'ALXSanFrancco'
