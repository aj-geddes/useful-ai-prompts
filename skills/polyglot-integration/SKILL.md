---
name: polyglot-integration
description: >
  Integrate multiple programming languages using FFI, native bindings, gRPC, or
  language bridges. Use when combining strengths of different languages or
  integrating legacy systems.
---

# Polyglot Integration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Integrate code written in different programming languages to leverage their unique strengths and ecosystems.

## When to Use

- Performance-critical code in C/C++/Rust
- ML models in Python from other languages
- Legacy system integration
- Leveraging language-specific libraries
- Microservices polyglot architecture

## Quick Start

Minimal working example:

```cpp
// addon.cc
#include <node.h>

namespace demo {

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::String;
using v8::Value;
using v8::Number;

void Add(const FunctionCallbackInfo<Value>& args) {
  Isolate* isolate = args.GetIsolate();

  if (args.Length() < 2) {
    isolate->ThrowException(v8::Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong number of arguments")));
    return;
  }

  if (!args[0]->IsNumber() || !args[1]->IsNumber()) {
    isolate->ThrowException(v8::Exception::TypeError(
        String::NewFromUtf8(isolate, "Arguments must be numbers")));
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Native Addons (C++)](references/nodejs-native-addons-c.md) | Node.js Native Addons (C++) |
| [Python from Node.js](references/python-from-nodejs.md) | Python from Node.js |
| [Rust from Python (PyO3)](references/rust-from-python-pyo3.md) | Rust from Python (PyO3) |
| [gRPC Polyglot Communication](references/grpc-polyglot-communication.md) | gRPC Polyglot Communication |
| [Java from Python (Py4J)](references/java-from-python-py4j.md) | Java from Python (Py4J) |

## Best Practices

### ✅ DO

- Use appropriate IPC mechanism
- Handle serialization carefully
- Implement proper error handling
- Consider performance overhead
- Use type-safe interfaces
- Document integration points

### ❌ DON'T

- Pass complex objects across boundaries
- Ignore memory management
- Skip error handling
- Use blocking calls in async code
