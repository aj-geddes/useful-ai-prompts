# File Path Handling

## File Path Handling

### Node.js Path Module

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

### Python Path Handling

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

### Go Path Handling

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
