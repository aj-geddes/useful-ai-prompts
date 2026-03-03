---
name: cross-platform-compatibility
description: >
  Handle cross-platform compatibility including file paths, environment
  detection, platform-specific dependencies, and testing across Windows, macOS,
  and Linux. Use when dealing with platform-specific code or OS compatibility.
---

# Cross-Platform Compatibility

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to writing code that works seamlessly across Windows, macOS, and Linux. Covers file path handling, environment detection, platform-specific features, and testing strategies.

## When to Use

- Building applications for multiple operating systems
- Handling file system operations
- Managing platform-specific dependencies
- Detecting operating system and architecture
- Working with environment variables
- Building cross-platform CLI tools
- Dealing with line endings and character encodings
- Managing platform-specific build processes

## Quick Start

Minimal working example:

```typescript
// ❌ BAD: Hardcoded paths with platform-specific separators
const configPath = "C:\\Users\\user\\config.json"; // Windows only
const dataPath = "/home/user/data.txt"; // Unix only

// ✅ GOOD: Use path module
import path from "path";
import os from "os";

// Platform-independent path construction
const configPath = path.join(os.homedir(), "config", "app.json");
const dataPath = path.join(process.cwd(), "data", "users.txt");

// Resolve relative paths
const absolutePath = path.resolve("./config/settings.json");

// Get path components
const dirname = path.dirname("/path/to/file.txt"); // '/path/to'
const basename = path.basename("/path/to/file.txt"); // 'file.txt'
const extname = path.extname("/path/to/file.txt"); // '.txt'

// Normalize paths (handle .. and .)
const normalized = path.normalize("/path/to/../file.txt"); // '/path/file.txt'
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [File Path Handling](references/file-path-handling.md) | File Path Handling |
| [Platform Detection](references/platform-detection.md) | Platform Detection |
| [Line Endings](references/line-endings.md) | Line Endings |
| [Environment Variables](references/environment-variables.md) | Environment Variables |
| [Shell Commands](references/shell-commands.md) | Shell Commands |
| [File Permissions](references/file-permissions.md) | File Permissions |
| [Process Management](references/process-management.md) | Process Management |
| [Platform-Specific Dependencies](references/platform-specific-dependencies.md) | Platform-Specific Dependencies |
| [Testing Across Platforms](references/testing-across-platforms.md) | Testing Across Platforms |
| [Character Encoding](references/character-encoding.md) | Character Encoding |
| [Build Configuration](references/build-configuration.md) | Build Configuration |

## Best Practices

### ✅ DO

- Use path.join() or path.resolve() for paths
- Use os.EOL for line endings
- Detect platform at runtime when needed
- Test on all target platforms
- Use optionalDependencies for platform-specific modules
- Handle file permissions gracefully
- Use shell escaping for user input
- Normalize line endings in text files
- Use UTF-8 encoding by default
- Document platform-specific behavior
- Provide fallbacks for platform-specific features
- Use CI/CD to test on multiple platforms

### ❌ DON'T

- Hardcode file paths with backslashes or forward slashes
- Assume Unix-only features (signals, permissions, symlinks)
- Ignore Windows-specific quirks (drive letters, UNC paths)
- Use platform-specific commands without fallbacks
- Assume case-sensitive file systems
- Forget about different line endings
- Use platform-specific APIs without checking
- Hardcode environment variable access patterns
- Ignore character encoding issues
