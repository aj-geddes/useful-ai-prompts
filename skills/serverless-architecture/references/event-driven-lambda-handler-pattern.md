# Event-Driven Lambda Handler Pattern

## Event-Driven Lambda Handler Pattern

```javascript
// src/handlers/processUserCreated.js
const AWS = require("aws-sdk");
const dynamodb = new AWS.DynamoDB.DocumentClient();

const userService = require("../services/userService");
const emailService = require("../services/emailService");

exports.handler = async (event, context) => {
  console.log("Processing user created event:", JSON.stringify(event));

  try {
    // Parse SNS message
    const records = event.Records;

    for (const record of records) {
      const message = JSON.parse(record.Sns.Message);
      const userId = message.userId;

      // Get user details
      const user = await userService.getUser(userId);

      // Send welcome email
      await emailService.sendWelcomeEmail(user);

      // Initialize user preferences
      await dynamodb
        .put({
          TableName: process.env.DYNAMODB_TABLE,
          Item: {
            id: userId,
            preferences: {
              newsletter: true,
              notifications: true,
            },
            createdAt: Date.now(),
          },
        })
        .promise();

      // Log success
      console.log(`Successfully processed user creation for ${userId}`);
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Processed" }),
    };
  } catch (error) {
    console.error("Error processing event:", error);
    throw error; // SNS will retry
  }
};

// src/handlers/processImageUpload.js
const AWS = require("aws-sdk");
const s3 = new AWS.S3();
const rekognition = new AWS.Rekognition();

exports.handler = async (event, context) => {
  try {
    for (const record of event.Records) {
      const bucket = record.s3.bucket.name;
      const key = record.s3.object.key;

      console.log(`Processing image: s3://${bucket}/${key}`);

      // Analyze image with Rekognition
      const labels = await rekognition
        .detectLabels({
          Image: {
            S3Object: {
              Bucket: bucket,
              Name: key,
            },
          },
          MaxLabels: 10,
          MinConfidence: 70,
        })
        .promise();

      // Create thumbnail
      await createThumbnail(bucket, key);

      // Index metadata
      await indexMetadata(bucket, key, labels);

      console.log(`Completed processing ${key}`);
    }
  } catch (error) {
    console.error("Error processing S3 event:", error);
    throw error;
  }
};

async function createThumbnail(bucket, key) {
  // Implementation
  return true;
}

async function indexMetadata(bucket, key, labels) {
  // Implementation
  return true;
}
```
