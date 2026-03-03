# Express.js Graceful Shutdown

## Express.js Graceful Shutdown

```typescript
import express from "express";
import http from "http";

class GracefulShutdownServer {
  private app: express.Application;
  private server: http.Server;
  private isShuttingDown = false;
  private activeConnections = new Set<any>();
  private shutdownTimeout = 30000; // 30 seconds

  constructor() {
    this.app = express();
    this.server = http.createServer(this.app);
    this.setupMiddleware();
    this.setupRoutes();
    this.setupShutdownHandlers();
  }

  private setupMiddleware(): void {
    // Track active connections
    this.app.use((req, res, next) => {
      if (this.isShuttingDown) {
        res.set("Connection", "close");
        return res.status(503).json({
          error: "Server is shutting down",
        });
      }

      this.activeConnections.add(res);

      res.on("finish", () => {
        this.activeConnections.delete(res);
      });

      res.on("close", () => {
        this.activeConnections.delete(res);
      });

      next();
    });
  }

  private setupRoutes(): void {
    this.app.get("/health", (req, res) => {
      if (this.isShuttingDown) {
        return res.status(503).json({ status: "shutting_down" });
      }
      res.json({ status: "ok" });
    });

    this.app.get("/api/data", async (req, res) => {
      // Simulate long-running request
      await new Promise((resolve) => setTimeout(resolve, 5000));
      res.json({ data: "response" });
    });
  }

  private setupShutdownHandlers(): void {
    const signals: NodeJS.Signals[] = ["SIGTERM", "SIGINT"];

    signals.forEach((signal) => {
      process.on(signal, () => {
        console.log(`Received ${signal}, starting graceful shutdown...`);
        this.gracefulShutdown(signal);
      });
    });

    // Handle uncaught exceptions
    process.on("uncaughtException", (error) => {
      console.error("Uncaught exception:", error);
      this.gracefulShutdown("UNCAUGHT_EXCEPTION");
    });

    process.on("unhandledRejection", (reason, promise) => {
      console.error("Unhandled rejection:", reason);
      this.gracefulShutdown("UNHANDLED_REJECTION");
    });
  }

  private async gracefulShutdown(signal: string): Promise<void> {
    if (this.isShuttingDown) {
      console.log("Shutdown already in progress");
      return;
    }

    this.isShuttingDown = true;
    console.log(`Starting graceful shutdown (${signal})`);

    // Set shutdown timeout
    const shutdownTimer = setTimeout(() => {
      console.error("Shutdown timeout reached, forcing exit");
      process.exit(1);
    }, this.shutdownTimeout);

    try {
      // 1. Stop accepting new connections
      await this.stopAcceptingConnections();

      // 2. Wait for active requests to complete
      await this.waitForActiveConnections();

      // 3. Close server
      await this.closeServer();

      // 4. Cleanup resources
      await this.cleanupResources();

      console.log("Graceful shutdown completed");
      clearTimeout(shutdownTimer);
      process.exit(0);
    } catch (error) {
      console.error("Error during shutdown:", error);
      clearTimeout(shutdownTimer);
      process.exit(1);
    }
  }

  private async stopAcceptingConnections(): Promise<void> {
    console.log("Stopping new connections...");
    return new Promise((resolve) => {
      this.server.close(() => {
        console.log("Server stopped accepting new connections");
        resolve();
      });
    });
  }

  private async waitForActiveConnections(): Promise<void> {
    console.log(
      `Waiting for ${this.activeConnections.size} active connections...`,
    );

    const checkInterval = 100;
    const maxWait = this.shutdownTimeout - 5000;
    let waited = 0;

    while (this.activeConnections.size > 0 && waited < maxWait) {
      await new Promise((resolve) => setTimeout(resolve, checkInterval));
      waited += checkInterval;

      if (waited % 1000 === 0) {
        console.log(
          `Still waiting for ${this.activeConnections.size} connections...`,
        );
      }
    }

    if (this.activeConnections.size > 0) {
      console.warn(
        `Force closing ${this.activeConnections.size} remaining connections`,
      );
      this.activeConnections.forEach((res: any) => {
        res.destroy();
      });
    }

    console.log("All connections closed");
  }

  private async closeServer(): Promise<void> {
    // Server already closed in stopAcceptingConnections
    console.log("Server closed");
  }

  private async cleanupResources(): Promise<void> {
    console.log("Cleaning up resources...");

    // Close database connections
    await this.closeDatabaseConnections();

    // Flush logs
    await this.flushLogs();

    // Close any other resources
    await this.closeOtherResources();

    console.log("Resources cleaned up");
  }

  private async closeDatabaseConnections(): Promise<void> {
    // Close database connections
    console.log("Closing database connections...");
    // await db.close();
  }

  private async flushLogs(): Promise<void> {
    // Flush any pending logs
    console.log("Flushing logs...");
  }

  private async closeOtherResources(): Promise<void> {
    // Close Redis, message queues, etc.
    console.log("Closing other resources...");
  }

  start(port: number): void {
    this.server.listen(port, () => {
      console.log(`Server listening on port ${port}`);
    });
  }
}

// Usage
const server = new GracefulShutdownServer();
server.start(3000);
```
