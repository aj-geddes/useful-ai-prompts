# Line Endings

## Line Endings

```typescript
// line-endings.ts
import os from "os";

export const LineEnding = {
  LF: "\n", // Unix/Linux/macOS
  CRLF: "\r\n", // Windows
  CR: "\r", // Old Mac (pre-OS X)

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
  },
};

// Usage
const fileContent = fs.readFileSync("file.txt", "utf8");

// Normalize to platform-specific line endings
const normalized = LineEnding.normalize(fileContent);

// Force Unix line endings (for git, etc.)
const unixContent = LineEnding.toUnix(fileContent);

// Write with platform-specific line endings
fs.writeFileSync("output.txt", normalized);
```
