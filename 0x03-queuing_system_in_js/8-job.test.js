import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import sinon from 'sinon';

describe('createPushNotificationsJobs', () => {
  let queue;
  let consoleLogStub;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode = true;  // Set Kue to test mode
    consoleLogStub = sinon.stub(console, 'log');  // Stub console.log to capture logs
  });

  afterEach(() => {
    // Clear the queue after each test
    queue.testMode = false;
    queue.removeJobs('*', () => {});  // Remove all jobs
    consoleLogStub.restore();  // Restore the original console.log
  });

  it('should display an error message if jobs is not an array', () => {
    try {
      createPushNotificationsJobs('not an array', queue);
    } catch (err) {
      expect(err.message).to.equal('Jobs is not an array');
    }
  });

  it('should create jobs in the queue and log job creation messages', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Check that the jobs were created
    expect(queue.testMode).to.be.true;  // Ensure we're in test mode
    expect(queue.length()).to.equal(2);  // Ensure there are two jobs in the queue

    // Verify the console log output for job creation
    expect(consoleLogStub.callCount).to.equal(2);  // Should log job creation twice
    expect(consoleLogStub.getCall(0).args[0]).to.include('Notification job created');
    expect(consoleLogStub.getCall(1).args[0]).to.include('Notification job created');
  });

  it('should handle job completion', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518782',
        message: 'This is the code 7890 to verify your account'
      }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Simulate the job processing
    queue.process('push_notification_code_3', (job, done) => {
      job.progress(100);  // Mark job as completed
      done();
    });

    // Run the queue and check the result
    queue.testMode = false;
    queue.process('push_notification_code_3', (err, job) => {
      if (err) return done(err);
      expect(consoleLogStub.callCount).to.equal(2);  // Job created + Job completed
      expect(consoleLogStub.getCall(1).args[0]).to.include('Notification job completed');
      done();
    });
  });

  it('should handle job failure', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518783',
        message: 'This is the code 1111 to verify your account'
      }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Simulate a job failure
    queue.process('push_notification_code_3', (job, done) => {
      done(new Error('Job failed'));
    });

    // Run the queue and check the result
    queue.testMode = false;
    queue.process('push_notification_code_3', (err, job) => {
      if (err) return done(err);
      expect(consoleLogStub.callCount).to.equal(2);  // Job created + Job failed
      expect(consoleLogStub.getCall(1).args[0]).to.include('Notification job failed');
      done();
    });
  });
});
