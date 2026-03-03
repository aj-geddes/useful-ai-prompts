# Client Implementation

## Client Implementation

```javascript
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

const packageDef = protoLoader.loadSync(path.join(__dirname, "user.proto"));

const userProto = grpc.loadPackageDefinition(packageDef).user.service;
const client = new userProto.UserService(
  "localhost:50051",
  grpc.credentials.createInsecure(),
);

// Unary call
client.getUser({ id: "123" }, (err, user) => {
  if (err) console.error(err);
  console.log("User:", user);
});

// Server streaming
const stream = client.streamUsers({});
stream.on("data", (user) => {
  console.log("Received user:", user);
});
stream.on("end", () => {
  console.log("Stream ended");
});

// Client streaming
const writeStream = client.bulkCreateUsers((err, response) => {
  if (err) console.error(err);
  console.log("Created users:", response.users.length);
});

writeStream.write({
  email: "user1@example.com",
  first_name: "John",
  last_name: "Doe",
});
writeStream.write({
  email: "user2@example.com",
  first_name: "Jane",
  last_name: "Smith",
});
writeStream.end();
```
