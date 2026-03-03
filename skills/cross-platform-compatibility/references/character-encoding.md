# Character Encoding

## Character Encoding

```typescript
// encoding-utils.ts
import iconv from "iconv-lite";

export class EncodingUtils {
  // Read file with specific encoding
  static readFile(filepath: string, encoding: string = "utf8"): string {
    const buffer = fs.readFileSync(filepath);

    if (encoding === "utf8") {
      // Remove BOM if present
      if (buffer[0] === 0xef && buffer[1] === 0xbb && buffer[2] === 0xbf) {
        return buffer.slice(3).toString("utf8");
      }
      return buffer.toString("utf8");
    }

    return iconv.decode(buffer, encoding);
  }

  // Write file with specific encoding
  static writeFile(
    filepath: string,
    content: string,
    encoding: string = "utf8",
  ): void {
    if (encoding === "utf8") {
      fs.writeFileSync(filepath, content, "utf8");
    } else {
      const buffer = iconv.encode(content, encoding);
      fs.writeFileSync(filepath, buffer);
    }
  }

  // Detect encoding
  static detectEncoding(filepath: string): string {
    const buffer = fs.readFileSync(filepath);

    // Check for BOM
    if (buffer[0] === 0xef && buffer[1] === 0xbb && buffer[2] === 0xbf) {
      return "utf8";
    }
    if (buffer[0] === 0xfe && buffer[1] === 0xff) {
      return "utf16be";
    }
    if (buffer[0] === 0xff && buffer[1] === 0xfe) {
      return "utf16le";
    }

    // Default to UTF-8
    return "utf8";
  }
}
```
