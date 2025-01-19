// 100-seat.js
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// Set up the express app
const app = express();
const port = 1245;

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create a Kue queue
const queue = kue.createQueue();

// Initialize available seats and reservationEnabled
let reservationEnabled = true;
const initialSeats = 50;

// Function to reserve seats in Redis
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get current available seats from Redis
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats, 10) : 0;
}

// Set initial number of available seats
reserveSeat(initialSeats);

// Route: GET /available_seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

// Route: GET /reserve_seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create a job to reserve a seat in the queue
  const job = queue.create('reserve_seat', {})
    .save((err) => {
      if (err) {
        return res.json({ status: 'Reservation failed' });
      }
      return res.json({ status: 'Reservation in process' });
    });
});

// Route: GET /process
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue asynchronously
  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    
    // If no available seats, fail the job
    if (availableSeats <= 0) {
      return done(new Error('Not enough seats available'));
    }

    // Decrease the available seats
    availableSeats -= 1;
    await reserveSeat(availableSeats);

    // If no seats left, disable reservations
    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    console.log(`Seat reservation job ${job.id} completed`);
    done();
  });
});

// Listen on the specified port
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
