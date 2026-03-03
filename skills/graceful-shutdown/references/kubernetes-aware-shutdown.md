# Kubernetes-Aware Shutdown

## Kubernetes-Aware Shutdown

```typescript
class KubernetesGracefulShutdown {
  private isReady = true;
  private isLive = true;
  private shutdownDelay = 5000; // K8s propagation delay

  setupProbes(app: express.Application): void {
    // Readiness probe
    app.get("/health/ready", (req, res) => {
      if (this.isReady) {
        res.status(200).json({ status: "ready" });
      } else {
        res.status(503).json({ status: "not_ready" });
      }
    });

    // Liveness probe
    app.get("/health/live", (req, res) => {
      if (this.isLive) {
        res.status(200).json({ status: "alive" });
      } else {
        res.status(503).json({ status: "not_alive" });
      }
    });
  }

  async shutdown(): Promise<void> {
    console.log("Kubernetes graceful shutdown initiated");

    // 1. Mark as not ready (fail readiness probe)
    this.isReady = false;
    console.log("Marked as not ready");

    // 2. Wait for K8s to remove pod from service endpoints
    console.log(`Waiting ${this.shutdownDelay}ms for endpoint propagation...`);
    await new Promise((resolve) => setTimeout(resolve, this.shutdownDelay));

    // 3. Continue with normal graceful shutdown
    // ... rest of shutdown logic
  }
}
```
