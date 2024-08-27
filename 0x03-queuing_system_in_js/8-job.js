function createPushNotificationsJobs(jobs, queue) {
  if (!jobs instanceof Array) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(element => {
    const job = queue.create('push_notification_code_3', element).save();
    job.on('enqueue', () => {
      console.log('Notification job created: ', job.id);
    })
    .on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', () => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${job.id}, ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
