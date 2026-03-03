# Dynamic Configuration (Remote Config)

## Dynamic Configuration (Remote Config)

```typescript
// config/remote-config.ts
export class RemoteConfigService {
  private config: Map<string, any> = new Map();
  private pollInterval: NodeJS.Timeout | null = null;

  constructor(private configServiceUrl: string) {}

  async initialize() {
    await this.fetchConfig();
    this.startPolling();
  }

  private async fetchConfig() {
    try {
      const response = await fetch(`${this.configServiceUrl}/config`);
      const config = await response.json();

      for (const [key, value] of Object.entries(config)) {
        const oldValue = this.config.get(key);
        if (oldValue !== value) {
          console.log(`Config changed: ${key} = ${value}`);
          this.config.set(key, value);
        }
      }
    } catch (error) {
      console.error("Failed to fetch remote config:", error);
    }
  }

  private startPolling() {
    // Poll every 60 seconds
    this.pollInterval = setInterval(() => {
      this.fetchConfig();
    }, 60000);
  }

  get(key: string, defaultValue?: any): any {
    return this.config.get(key) ?? defaultValue;
  }

  stop() {
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
    }
  }
}

// Usage
const remoteConfig = new RemoteConfigService(
  "https://config-service.example.com",
);
await remoteConfig.initialize();

app.get("/api/users", (req, res) => {
  const pageSize = remoteConfig.get("api.users.pageSize", 20);
  const enableCache = remoteConfig.get("api.users.enableCache", false);

  // Use dynamic config values
});
```
