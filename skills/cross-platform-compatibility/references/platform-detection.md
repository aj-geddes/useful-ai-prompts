# Platform Detection

## Platform Detection

### Node.js Platform Detection

```typescript
// platform-utils.ts
import os from "os";

export const Platform = {
  isWindows: process.platform === "win32",
  isMacOS: process.platform === "darwin",
  isLinux: process.platform === "linux",
  isUnix: process.platform !== "win32",

  get current(): "windows" | "macos" | "linux" | "unknown" {
    switch (process.platform) {
      case "win32":
        return "windows";
      case "darwin":
        return "macos";
      case "linux":
        return "linux";
      default:
        return "unknown";
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
  },
};

// Usage
if (Platform.isWindows) {
  // Windows-specific code
  console.log("Running on Windows");
} else if (Platform.isMacOS) {
  // macOS-specific code
  console.log("Running on macOS");
} else if (Platform.isLinux) {
  // Linux-specific code
  console.log("Running on Linux");
}

// Architecture detection
if (Platform.arch === "arm64") {
  console.log("Running on ARM architecture");
}
```

### Python Platform Detection

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
