import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const PORT = 1245;

async function reserveSeat(number) {
  return promisify(client.SET).bind(client)('available_seats', number);
};

async function getCurrentAvailableSeats() {
  return promisify(client.GET).bind(client)('available_seats');
};

app.listen(PORT, () => {
  console.log(`app listening at http://localhost:${PORT}`);
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  reserveSeat(50);
  reservationEnabled = true;
});

app.get('/available_seats', (_, res) => {
  getCurrentAvailableSeats()
    .then((numberOfAvailableSeats) => {
      res.json({ numberOfAvailableSeats })
    });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  try {
    const job = queue.create('reserve_seat');

    job.on('failed', (err) => {
      console.log(`Seat reservation job ${job.id}, failed: ${err}`);
    });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.save();
    res.json({ status: 'Reservation in process' });
  } catch {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', (_job, done) => {
    getCurrentAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((availableSeats) => {
        reservationEnabled = availableSeats <= 1 ? false : reservationEnabled;
        if (availableSeats >= 1) {
          reserveSeat(availableSeats - 1)
            .then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
      });
  });
});

export default app;
