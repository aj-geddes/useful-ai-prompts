---
name: cross-platform-compatibility
description: Handle cross-platform compatibility including file paths, environment detection, platform-specific dependencies, and testing across Windows, macOS, and Linux. Use when dealing with platform-specific code or OS compatibility.
---

# Cross-Platform Compatibility

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

## Instructions

### 1. **File Path Handling**

#### Node.js Path Module
```typescript
// ❌ BAD: Hardcoded paths with platform-specific separators
const configPath = 'C:\\Users\\user\\config.json';  // Windows only
const dataPath = '/home/user/data.txt';             // Unix only

// ✅ GOOD: Use path module
import path from 'path';
import os from 'os';

// Platform-independent path construction
const configPath = path.join(os.homedir(), 'config', 'app.json');
const dataPath = path.join(process.cwd(), 'data', 'users.txt');

// Resolve relative paths
const absolutePath = path.resolve('./config/settings.json');

// Get path components
const dirname = path.dirname('/path/to/file.txt');    // '/path/to'
const basename = path.basename('/path/to/file.txt');  // 'file.txt'
const extname = path.extname('/path/to/file.txt');    // '.txt'

// Normalize paths (handle .. and .)
const normalized = path.normalize('/path/to/../file.txt');  // '/path/file.txt'
```

#### Python Path Handling
```python
# ❌ BAD: Hardcoded separators
config_path = 'C:\\Users\\user\\config.json'  # Windows only
data_path = '/home/user/data.txt'             # Unix only

# ✅ GOOD: Use pathlib
from pathlib import Path
import os

# Platform-independent path construction
config_path = Path.home() / 'config' / 'app.json'
data_path = Path.cwd() / 'data' / 'users.txt'

# Working with paths
if config_path.exists():
    content = config_path.read_text()

# Get path components
dirname = config_path.parent
filename = config_path.name
extension = config_path.suffix

# Resolve relative paths
absolute_path = Path('./config/settings.json').resolve()

# Create directories
output_dir = Path('output')
output_dir.mkdir(parents=True, exist_ok=True)
```

#### Go Path Handling
```go
package main

import (
    "os"
    "path/filepath"
)

func main() {
    // ❌ BAD: Hardcoded paths
    // configPath := "C:\\Users\\user\\config.json"

    // ✅ GOOD: Use filepath package
    homeDir, _ := os.UserHomeDir()
    configPath := filepath.Join(homeDir, "config", "app.json")

    // Get path components
    dir := filepath.Dir(configPath)
    base := filepath.Base(configPath)
    ext := filepath.Ext(configPath)

    // Clean and normalize paths
    cleaned := filepath.Clean("path/to/../file.txt")

    // Convert to absolute path
    absPath, _ := filepath.Abs("./config/settings.json")
}
```

### 2. **Platform Detection**

#### Node.js Platform Detection
```typescript
// platform-utils.ts
import os from 'os';

export const Platform = {
  isWindows: process.platform === 'win32',
  isMacOS: process.platform === 'darwin',
  isLinux: process.platform === 'linux',
  isUnix: process.platform !== 'win32',

  get current(): 'windows' | 'macos' | 'linux' | 'unknown' {
    switch (process.platform) {
      case 'win32': return 'windows';
      case 'darwin': return 'macos';
      case 'linux': return 'linux';
      default: return 'unknown';
    }
  },

  get arch(): string {
    return process.arch; // 'x64', 'arm64', etc.
  },

  get homeDir(): string {
    return os.homedir();
  },

  get tempDir(): string {
    return os.tmpdir();
  }
};

// Usage
if (Platform.isWindows) {
  // Windows-specific code
  console.log('Running on Windows');
} else if (Platform.isMacOS) {
  // macOS-specific code
  console.log('Running on macOS');
} else if (Platform.isLinux) {
  // Linux-specific code
  console.log('Running on Linux');
}

// Architecture detection
if (Platform.arch === 'arm64') {
  console.log('Running on ARM architecture');
}
```

#### Python Platform Detection
```python
# platform_utils.py
import platform
import sys

class Platform:
    @staticmethod
    def is_windows():
        return sys.platform.startswith('win')

    @staticmethod
    def is_macos():
        return sys.platform == 'darwin'

    @staticmethod
    def is_linux():
        return sys.platform.startswith('linux')

    @staticmethod
    def is_unix():
        return not Platform.is_windows()

    @staticmethod
    def current():
        if Platform.is_windows():
            return 'windows'
        elif Platform.is_macos():
            return 'macos'
        elif Platform.is_linux():
            return 'linux'
        return 'unknown'

    @staticmethod
    def arch():
        return platform.machine()  # 'x86_64', 'arm64', etc.

    @staticmethod
    def version():
        return platform.version()

# Usage
if Platform.is_windows():
    # Windows-specific code
    print('Running on Windows')
elif Platform.is_macos():
    # macOS-specific code
    print('Running on macOS')
elif Platform.is_linux():
    # Linux-specific code
    print('Running on Linux')
```

### 3. **Line Endings**

```typescript
// line-endings.ts
import os from 'os';

export const LineEnding = {
  LF: '\n',      // Unix/Linux/macOS
  CRLF: '\r\n',  // Windows
  CR: '\r',      // Old Mac (pre-OS X)

  get platform(): string {
    return os.EOL; // Returns platform-specific line ending
  },

  normalize(text: string, target: string = os.EOL): string {
    // Normalize all line endings to target
    return text.replace(/\r\n|\r|\n/g, target);
  },

  toUnix(text: string): string {
    return this.normalize(text, this.LF);
  },

  toWindows(text: string): string {
    return this.normalize(text, this.CRLF);
  }
};

// Usage
const fileContent = fs.readFileSync('file.txt', 'utf8');

// Normalize to platform-specific line endings
const normalized = LineEnding.normalize(fileContent);

// Force Unix line endings (for git, etc.)
const unixContent = LineEnding.toUnix(fileContent);

// Write with platform-specific line endings
fs.writeFileSync('output.txt', normalized);
```

### 4. **Environment Variables**

```typescript
// env-utils.ts
export class EnvUtils {
  // Get environment variable with fallback
  static get(key: string, defaultValue?: string): string | undefined {
    return process.env[key] || defaultValue;
  }

  // Get PATH separator (: on Unix, ; on Windows)
  static get pathSeparator(): string {
    return process.platform === 'win32' ? ';' : ':';
  }

  // Split PATH into array
  static getPaths(): string[] {
    const pathVar = process.env.PATH || '';
    return pathVar.split(this.pathSeparator);
  }

  // Get common paths
  static get home(): string {
    return process.env.HOME || process.env.USERPROFILE || '';
  }

  static get user(): string {
    return process.env.USER || process.env.USERNAME || '';
  }

  // Check if running in CI
  static get isCI(): boolean {
    return !!(
      process.env.CI ||
      process.env.CONTINUOUS_INTEGRATION ||
      process.env.GITHUB_ACTIONS ||
      process.env.GITLAB_CI
    );
  }
}
```

### 5. **Shell Commands**

```typescript
// shell-utils.ts
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export class ShellUtils {
  // Execute command with platform-specific handling
  static async execute(command: string): Promise<string> {
    try {
      const { stdout, stderr } = await execAsync(command, {
        shell: this.getShell()
      });
      if (stderr) console.error(stderr);
      return stdout.trim();
    } catch (error) {
      throw new Error(`Command failed: ${error.message}`);
    }
  }

  // Get platform-specific shell
  static getShell(): string {
    if (process.platform === 'win32') {
      return 'cmd.exe';
    }
    return process.env.SHELL || '/bin/sh';
  }

  // Platform-specific commands
  static async listFiles(directory: string): Promise<string> {
    if (process.platform === 'win32') {
      return this.execute(`dir "${directory}"`);
    }
    return this.execute(`ls -la "${directory}"`);
  }

  static async clearScreen(): Promise<void> {
    if (process.platform === 'win32') {
      await this.execute('cls');
    } else {
      await this.execute('clear');
    }
  }

  static async openFile(filepath: string): Promise<void> {
    if (process.platform === 'win32') {
      await this.execute(`start "" "${filepath}"`);
    } else if (process.platform === 'darwin') {
      await this.execute(`open "${filepath}"`);
    } else {
      await this.execute(`xdg-open "${filepath}"`);
    }
  }
}
```

### 6. **File Permissions**

```typescript
// permissions.ts
import fs from 'fs';
import path from 'path';

export class FilePermissions {
  // Make file executable (Unix only)
  static makeExecutable(filepath: string): void {
    if (process.platform !== 'win32') {
      fs.chmodSync(filepath, 0o755);
    }
  }

  // Check if file is executable
  static isExecutable(filepath: string): boolean {
    if (process.platform === 'win32') {
      // On Windows, check file extension
      const ext = path.extname(filepath).toLowerCase();
      return ['.exe', '.bat', '.cmd', '.com'].includes(ext);
    }

    try {
      fs.accessSync(filepath, fs.constants.X_OK);
      return true;
    } catch {
      return false;
    }
  }

  // Create file with specific permissions (Unix)
  static createWithPermissions(
    filepath: string,
    content: string,
    mode: number = 0o644
  ): void {
    fs.writeFileSync(filepath, content, { mode });
  }
}
```

### 7. **Process Management**

```typescript
// process-utils.ts
import { spawn, ChildProcess } from 'child_process';

export class ProcessUtils {
  // Kill process by PID with platform-specific signal
  static kill(pid: number, signal?: string): void {
    if (process.platform === 'win32') {
      // Windows doesn't support signals, use taskkill
      spawn('taskkill', ['/pid', pid.toString(), '/f', '/t']);
    } else {
      process.kill(pid, signal || 'SIGTERM');
    }
  }

  // Spawn process with platform-specific handling
  static spawnCommand(
    command: string,
    args: string[] = []
  ): ChildProcess {
    if (process.platform === 'win32') {
      // Windows requires cmd.exe to run commands
      return spawn('cmd', ['/c', command, ...args], {
        stdio: 'inherit',
        shell: true
      });
    }

    return spawn(command, args, {
      stdio: 'inherit',
      shell: true
    });
  }

  // Find process by name
  static async findProcess(name: string): Promise<number[]> {
    if (process.platform === 'win32') {
      const { stdout } = await execAsync(`tasklist /FI "IMAGENAME eq ${name}"`);
      // Parse Windows tasklist output
      const pids: number[] = [];
      const lines = stdout.split('\n');
      for (const line of lines) {
        const match = line.match(/\s+(\d+)\s+/);
        if (match) pids.push(parseInt(match[1]));
      }
      return pids;
    } else {
      const { stdout } = await execAsync(`pgrep ${name}`);
      return stdout.split('\n').filter(Boolean).map(Number);
    }
  }
}
```

### 8. **Platform-Specific Dependencies**

```json
// package.json
{
  "name": "my-app",
  "dependencies": {
    "common-dep": "^1.0.0"
  },
  "optionalDependencies": {
    "fsevents": "^2.3.2"
  },
  "devDependencies": {
    "@types/node": "^18.0.0"
  }
}
```

```typescript
// platform-specific-module.ts
export async function loadPlatformModule() {
  if (process.platform === 'win32') {
    return await import('./windows/module');
  } else if (process.platform === 'darwin') {
    return await import('./macos/module');
  } else {
    return await import('./linux/module');
  }
}

// Graceful fallback for optional dependencies
export function useFSEvents() {
  try {
    // fsevents is macOS only
    if (process.platform === 'darwin') {
      const fsevents = require('fsevents');
      return fsevents;
    }
  } catch (error) {
    console.warn('fsevents not available, using fallback');
  }

  // Fallback to chokidar or fs.watch
  return require('chokidar');
}
```

### 9. **Testing Across Platforms**

#### GitHub Actions Matrix
```yaml
# .github/workflows/test.yml
name: Cross-Platform Tests

on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [16, 18, 20]

    runs-on: ${{ matrix.os }}

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Platform-specific tests
        if: runner.os == 'Windows'
        run: npm run test:windows

      - name: Platform-specific tests
        if: runner.os == 'macOS'
        run: npm run test:macos

      - name: Platform-specific tests
        if: runner.os == 'Linux'
        run: npm run test:linux
```

#### Platform-Specific Tests
```typescript
// tests/platform.test.ts
import { Platform } from '../src/platform-utils';

describe('Platform-specific tests', () => {
  describe('File paths', () => {
    it('should handle paths correctly', () => {
      const configPath = path.join(os.homedir(), 'config.json');

      if (Platform.isWindows) {
        expect(configPath).toMatch(/^[A-Z]:\\/);
      } else {
        expect(configPath).toMatch(/^\//);
      }
    });
  });

  describe.skipIf(Platform.isWindows)('Unix-only tests', () => {
    it('should work with symlinks', () => {
      // Symlink tests
    });

    it('should handle file permissions', () => {
      // Permission tests
    });
  });

  describe.skipIf(!Platform.isWindows)('Windows-only tests', () => {
    it('should work with UNC paths', () => {
      // UNC path tests
    });

    it('should handle drive letters', () => {
      // Drive letter tests
    });
  });
});
```

### 10. **Character Encoding**

```typescript
// encoding-utils.ts
import iconv from 'iconv-lite';

export class EncodingUtils {
  // Read file with specific encoding
  static readFile(filepath: string, encoding: string = 'utf8'): string {
    const buffer = fs.readFileSync(filepath);

    if (encoding === 'utf8') {
      // Remove BOM if present
      if (buffer[0] === 0xEF && buffer[1] === 0xBB && buffer[2] === 0xBF) {
        return buffer.slice(3).toString('utf8');
      }
      return buffer.toString('utf8');
    }

    return iconv.decode(buffer, encoding);
  }

  // Write file with specific encoding
  static writeFile(
    filepath: string,
    content: string,
    encoding: string = 'utf8'
  ): void {
    if (encoding === 'utf8') {
      fs.writeFileSync(filepath, content, 'utf8');
    } else {
      const buffer = iconv.encode(content, encoding);
      fs.writeFileSync(filepath, buffer);
    }
  }

  // Detect encoding
  static detectEncoding(filepath: string): string {
    const buffer = fs.readFileSync(filepath);

    // Check for BOM
    if (buffer[0] === 0xEF && buffer[1] === 0xBB && buffer[2] === 0xBF) {
      return 'utf8';
    }
    if (buffer[0] === 0xFE && buffer[1] === 0xFF) {
      return 'utf16be';
    }
    if (buffer[0] === 0xFF && buffer[1] === 0xFE) {
      return 'utf16le';
    }

    // Default to UTF-8
    return 'utf8';
  }
}
```

### 11. **Build Configuration**

```typescript
// rollup.config.js
export default {
  input: 'src/index.ts',
  output: [
    {
      file: 'dist/index.js',
      format: 'cjs'
    },
    {
      file: 'dist/index.esm.js',
      format: 'esm'
    }
  ],
  external: [
    // Mark platform-specific modules as external
    'fsevents'
  ],
  plugins: [
    // Replace platform checks at build time for better tree-shaking
    replace({
      'process.platform': JSON.stringify(process.platform),
      preventAssignment: true
    })
  ]
};
```

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

## Common Patterns

### Pattern 1: Platform Factory
```typescript
export interface PlatformHandler {
  openFile(path: string): Promise<void>;
  getConfigPath(): string;
}

class WindowsHandler implements PlatformHandler {
  async openFile(path: string) {
    await exec(`start "" "${path}"`);
  }
  getConfigPath() {
    return path.join(process.env.APPDATA!, 'myapp', 'config.json');
  }
}

class UnixHandler implements PlatformHandler {
  async openFile(path: string) {
    await exec(`xdg-open "${path}"`);
  }
  getConfigPath() {
    return path.join(os.homedir(), '.config', 'myapp', 'config.json');
  }
}

export function createPlatformHandler(): PlatformHandler {
  return process.platform === 'win32'
    ? new WindowsHandler()
    : new UnixHandler();
}
```

### Pattern 2: Conditional Imports
```typescript
const platformModule = await (async () => {
  switch (process.platform) {
    case 'win32':
      return import('./platforms/windows');
    case 'darwin':
      return import('./platforms/macos');
    default:
      return import('./platforms/linux');
  }
})();
```

## Tools & Resources

- **cross-env**: Set environment variables cross-platform
- **cross-spawn**: Cross-platform spawn
- **rimraf**: Cross-platform rm -rf
- **mkdirp**: Cross-platform mkdir -p
- **cpy**: Cross-platform file copying
- **del**: Cross-platform file deletion
- **execa**: Better child_process
- **pkg**: Package Node.js apps for all platforms
