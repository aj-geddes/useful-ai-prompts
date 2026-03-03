# Strategy Pattern

## Strategy Pattern

Define family of algorithms and make them interchangeable.

```java
interface CompressionStrategy {
    byte[] compress(byte[] data);
}

class ZipCompression implements CompressionStrategy {
    public byte[] compress(byte[] data) {
        // ZIP compression logic
        return data;
    }
}

class GzipCompression implements CompressionStrategy {
    public byte[] compress(byte[] data) {
        // GZIP compression logic
        return data;
    }
}

class FileCompressor {
    private CompressionStrategy strategy;

    public FileCompressor(CompressionStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(CompressionStrategy strategy) {
        this.strategy = strategy;
    }

    public byte[] compressFile(byte[] data) {
        return strategy.compress(data);
    }
}

// Usage
FileCompressor compressor = new FileCompressor(new ZipCompression());
compressor.compressFile(fileData);

// Change strategy at runtime
compressor.setStrategy(new GzipCompression());
compressor.compressFile(fileData);
```
