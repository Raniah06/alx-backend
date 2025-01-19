import kue from 'kue';

// Create a queue named push_notification_code_2
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

// Define the function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);  // Set initial progress to 0%

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if phone number is blacklisted
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
    job.save();
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    console.log(`Notification job ${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
  } else {
    // Track progress to 50%
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    
    // Simulate job processing completion
    setTimeout(() => {
      job.complete();
      job.save();
      done();
      console.log(`Notification job ${job.id} completed`);
    }, 1000);  // Simulate job completion after 1 second
  }
}

// Queue processing with 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Example of adding jobs to the queue (you would already have these from job_creator.js)
queue.create('push_notification_code_2', {
  phoneNumber: '4153518780',
  message: 'This is the code 1234 to verify your account'
}).save();

queue.create('push_notification_code_2', {
  phoneNumber: '4153518781',
  message: 'This is the code 4562 to verify your account'
}).save();

queue.create('push_notification_code_2', {
  phoneNumber: '4153518743',
  message: 'This is the code 4321 to verify your account'
}).save();

queue.create('push_notification_code_2', {
  phoneNumber: '4153538781',
  message: 'This is the code 4562 to verify your account'
}).save();

// Add more jobs as needed...

console.log('Job processor is running...');
