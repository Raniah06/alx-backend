import kue from 'kue';

// Create a queue instance named push_notification_code
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '+1234567890',
  message: 'Your notification message here',
};

// Create the job
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Failed to create job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// When the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// When the job fails
job.on('failed', (err) => {
  console.log('Notification job failed', err);
});

// Optional: When the job is removed (either completed or failed)
job.on('removed', () => {
  console.log(`Notification job ${job.id} removed from queue`);
});
