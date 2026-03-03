# Node.js gRPC Server Implementation

## Node.js gRPC Server Implementation

```javascript
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

const packageDef = protoLoader.loadSync(path.join(__dirname, "user.proto"), {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const userProto = grpc.loadPackageDefinition(packageDef).user.service;

const users = new Map();
let userIdCounter = 1;

const userServiceImpl = {
  getUser: (call, callback) => {
    const user = users.get(call.request.id);
    if (!user) {
      return callback({
        code: grpc.status.NOT_FOUND,
        details: "User not found",
      });
    }
    callback(null, user);
  },

  listUsers: (call, callback) => {
    const page = call.request.page || 1;
    const limit = call.request.limit || 20;
    const offset = (page - 1) * limit;

    const userArray = Array.from(users.values());
    const paginatedUsers = userArray.slice(offset, offset + limit);

    callback(null, {
      users: paginatedUsers,
      total: userArray.length,
      page: page,
    });
  },

  createUser: (call, callback) => {
    const id = String(userIdCounter++);
    const user = {
      id,
      email: call.request.email,
      first_name: call.request.first_name,
      last_name: call.request.last_name,
      role: call.request.role,
      created_at: Date.now(),
      updated_at: Date.now(),
    };
    users.set(id, user);
    callback(null, user);
  },

  updateUser: (call, callback) => {
    const user = users.get(call.request.id);
    if (!user) {
      return callback({
        code: grpc.status.NOT_FOUND,
        details: "User not found",
      });
    }

    Object.assign(user, {
      email: call.request.email || user.email,
      first_name: call.request.first_name || user.first_name,
      last_name: call.request.last_name || user.last_name,
      updated_at: Date.now(),
    });

    callback(null, user);
  },

  deleteUser: (call, callback) => {
    users.delete(call.request.id);
    callback(null, {});
  },

  streamUsers: (call) => {
    Array.from(users.values()).forEach((user) => {
      call.write(user);
    });
    call.end();
  },

  bulkCreateUsers: (call, callback) => {
    const createdUsers = [];

    call.on("data", (request) => {
      const id = String(userIdCounter++);
      const user = {
        id,
        email: request.email,
        first_name: request.first_name,
        last_name: request.last_name,
        role: request.role,
        created_at: Date.now(),
        updated_at: Date.now(),
      };
      users.set(id, user);
      createdUsers.push(user);
    });

    call.on("end", () => {
      callback(null, {
        users: createdUsers,
        total: createdUsers.length,
        page: 1,
      });
    });

    call.on("error", (err) => {
      callback(err);
    });
  },
};

const server = new grpc.Server();
server.addService(userProto.UserService.service, userServiceImpl);

server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  () => {
    console.log("gRPC server running on port 50051");
    server.start();
  },
);
```
