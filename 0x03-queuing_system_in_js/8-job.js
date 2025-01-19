import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Loop through the jobs array
  jobs.forEach((jobData) => {
    // Create a job in the queue
    const job = queue.create('push_notification_code_3', jobData)
      .save((err) => {
        if (err) {
          console.log(`Notification job failed: ${err}`);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Define what happens when the job is complete
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Define what happens when the job fails
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Define progress tracking
    job.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
