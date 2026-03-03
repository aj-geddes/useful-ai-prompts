# Lambda Function with Node.js

## Lambda Function with Node.js

```javascript
// index.js
exports.handler = async (event) => {
  console.log("Event:", JSON.stringify(event));

  try {
    // Parse different event sources
    const body =
      typeof event.body === "string"
        ? JSON.parse(event.body)
        : event.body || {};

    // Process S3 event
    if (event.Records && event.Records[0].s3) {
      const bucket = event.Records[0].s3.bucket.name;
      const key = event.Records[0].s3.object.key;
      console.log(`Processing S3 object: ${bucket}/${key}`);
    }

    // Database query simulation
    const results = await queryDatabase(body);

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        message: "Success",
        data: results,
      }),
    };
  } catch (error) {
    console.error("Error:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};

async function queryDatabase(params) {
  // Simulate database call
  return { items: [] };
}
```
