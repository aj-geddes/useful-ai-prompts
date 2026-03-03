# Node.js with Bull Queue

## Node.js with Bull Queue

```javascript
// queue.js
const Queue = require("bull");
const redis = require("redis");

const redisClient = redis.createClient({
  host: process.env.REDIS_HOST || "localhost",
  port: process.env.REDIS_PORT || 6379,
});

// Create job queues
const emailQueue = new Queue("emails", {
  redis: {
    host: process.env.REDIS_HOST || "localhost",
    port: process.env.REDIS_PORT || 6379,
  },
});

const reportQueue = new Queue("reports", {
  redis: {
    host: process.env.REDIS_HOST || "localhost",
    port: process.env.REDIS_PORT || 6379,
  },
});

const batchQueue = new Queue("batch", {
  redis: {
    host: process.env.REDIS_HOST || "localhost",
    port: process.env.REDIS_PORT || 6379,
  },
});

// Process email jobs
emailQueue.process(5, async (job) => {
  const { userId, subject, body } = job.data;

  try {
    const user = await User.findById(userId);
    if (!user) {
      throw new Error(`User ${userId} not found`);
    }

    await sendEmailHelper(user.email, subject, body);

    return { status: "success", userId };
  } catch (error) {
    // Retry with exponential backoff
    throw error;
  }
});

// Process report jobs with progress
reportQueue.process(async (job) => {
  const { reportType, filters } = job.data;
  const totalRecords = await countRecords(filters);

  for (let i = 0; i < totalRecords; i += 1000) {
    const batch = await fetchRecordsBatch(filters, i, 1000);
    await processBatch(batch, reportType);

    // Update progress
    job.progress(Math.round((i / totalRecords) * 100));
  }

  return { status: "success", totalRecords };
});

// Process batch jobs
batchQueue.process(async (job) => {
  const { items } = job.data;
  const results = [];

  for (const item of items) {
    try {
      const result = await processItem(item);
      results.push(result);
    } catch (error) {
      results.push({ status: "failed", error: error.message });
    }
  }

  return { processed: results.length, results };
});

// Event listeners
emailQueue.on("completed", (job) => {
  console.log(`Email job ${job.id} completed`);
});

emailQueue.on("failed", (job, err) => {
  console.error(`Email job ${job.id} failed:`, err.message);
});

emailQueue.on("progress", (job, progress) => {
  console.log(`Email job ${job.id} ${progress}% complete`);
});

module.exports = {
  emailQueue,
  reportQueue,
  batchQueue,
};

// routes.js
const express = require("express");
const { emailQueue, reportQueue } = require("./queue");

const router = express.Router();

// Trigger email job
router.post("/send-email", async (req, res) => {
  const { userId, subject, body } = req.body;

  const job = await emailQueue.add(
    { userId, subject, body },
    {
      attempts: 3,
      backoff: {
        type: "exponential",
        delay: 2000,
      },
      removeOnComplete: true,
    },
  );

  res.status(202).json({ jobId: job.id });
});

// Get job status
router.get("/jobs/:jobId/status", async (req, res) => {
  const job = await emailQueue.getJob(req.params.jobId);

  if (!job) {
    return res.status(404).json({ error: "Job not found" });
  }

  const progress = await job.progress();
  const state = await job.getState();
  const attempts = job.attemptsMade;

  res.json({
    jobId: job.id,
    state,
    progress,
    attempts,
    data: job.data,
  });
});

module.exports = router;
```
