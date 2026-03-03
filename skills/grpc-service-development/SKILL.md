---
name: grpc-service-development
description: >
  Build high-performance gRPC services with Protocol Buffers, bidirectional
  streaming, and microservice communication. Use when building gRPC servers,
  defining service contracts, or implementing inter-service communication.
---

# gRPC Service Development

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Develop efficient gRPC services using Protocol Buffers for service definition, with support for unary calls, client streaming, server streaming, and bidirectional streaming patterns.

## When to Use

- Building microservices that require high performance
- Defining service contracts with Protocol Buffers
- Implementing real-time bidirectional communication
- Creating internal service-to-service APIs
- Optimizing bandwidth-constrained environments
- Building polyglot service architectures

## Quick Start

Minimal working example:

```protobuf
syntax = "proto3";

package user.service;

message User {
  string id = 1;
  string email = 2;
  string first_name = 3;
  string last_name = 4;
  string role = 5;
  int64 created_at = 6;
  int64 updated_at = 7;
}

message CreateUserRequest {
  string email = 1;
  string first_name = 2;
  string last_name = 3;
  string role = 4;
}

message UpdateUserRequest {
  string id = 1;
  string email = 2;
  string first_name = 3;
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Protocol Buffer Service Definition](references/protocol-buffer-service-definition.md) | Protocol Buffer Service Definition |
| [Node.js gRPC Server Implementation](references/nodejs-grpc-server-implementation.md) | Node.js gRPC Server Implementation |
| [Python gRPC Server (grpcio)](references/python-grpc-server-grpcio.md) | Python gRPC Server (grpcio) |
| [Client Implementation](references/client-implementation.md) | Client Implementation |

## Best Practices

### ✅ DO

- Use clear message and service naming
- Implement proper error handling with gRPC status codes
- Add metadata for logging and tracing
- Version your protobuf definitions
- Use streaming for large datasets
- Implement timeouts and deadlines
- Monitor gRPC metrics

### ❌ DON'T

- Use gRPC for browser-based clients (use gRPC-Web)
- Expose sensitive data in proto definitions
- Create deeply nested messages
- Ignore error status codes
- Send uncompressed large payloads
- Skip security with TLS in production
