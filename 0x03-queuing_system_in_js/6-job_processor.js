import kue from 'kue';

// Create a queue instance named push_notification_code
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen for new jobs of type 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message);

  // Mark the job as complete
  done();
});

// Optional: Log when the queue is ready to process jobs
queue.on('ready', () => {
  console.log('Job processor is ready and listening for new jobs...');
});
