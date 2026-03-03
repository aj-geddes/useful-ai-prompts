# Secret Management

## Secret Management

### AWS Secrets Manager

```typescript
// secrets/aws-secrets-manager.ts
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

export class SecretManager {
  private client: SecretsManagerClient;
  private cache = new Map<string, { value: any; expiry: number }>();
  private cacheTtl = 300000; // 5 minutes

  constructor() {
    this.client = new SecretsManagerClient({ region: process.env.AWS_REGION });
  }

  async getSecret(secretName: string): Promise<any> {
    // Check cache
    const cached = this.cache.get(secretName);
    if (cached && cached.expiry > Date.now()) {
      return cached.value;
    }

    try {
      const command = new GetSecretValueCommand({ SecretId: secretName });
      const response = await this.client.send(command);

      const secret = JSON.parse(response.SecretString || "{}");

      // Cache the secret
      this.cache.set(secretName, {
        value: secret,
        expiry: Date.now() + this.cacheTtl,
      });

      return secret;
    } catch (error) {
      throw new Error(
        `Failed to retrieve secret ${secretName}: ${error.message}`,
      );
    }
  }

  async getDatabaseCredentials(): Promise<DatabaseCredentials> {
    return this.getSecret("prod/database/credentials");
  }

  async getApiKey(service: string): Promise<string> {
    const secrets = await this.getSecret("prod/api-keys");
    return secrets[service];
  }
}

// Usage
const secretManager = new SecretManager();

async function connectDatabase() {
  const credentials = await secretManager.getDatabaseCredentials();

  return createConnection({
    host: credentials.host,
    port: credentials.port,
    username: credentials.username,
    password: credentials.password,
    database: credentials.database,
  });
}
```

### HashiCorp Vault

```typescript
// secrets/vault.ts
import vault from "node-vault";

export class VaultClient {
  private client: any;

  constructor() {
    this.client = vault({
      apiVersion: "v1",
      endpoint: process.env.VAULT_ADDR || "http://localhost:8200",
      token: process.env.VAULT_TOKEN,
    });
  }

  async getSecret(path: string): Promise<any> {
    try {
      const result = await this.client.read(path);
      return result.data.data;
    } catch (error) {
      throw new Error(`Failed to read secret from ${path}: ${error.message}`);
    }
  }

  async getDatabaseConfig(): Promise<DatabaseConfig> {
    return this.getSecret("secret/data/database");
  }

  async getApiKeys(): Promise<Record<string, string>> {
    return this.getSecret("secret/data/api-keys");
  }

  // Dynamic database credentials (rotated automatically)
  async getDynamicDBCredentials(): Promise<Credentials> {
    const result = await this.client.read("database/creds/readonly");
    return {
      username: result.data.username,
      password: result.data.password,
      leaseId: result.lease_id,
      leaseDuration: result.lease_duration,
    };
  }
}
```

### Environment-Specific Secrets

```typescript
// secrets/secret-provider.ts
export interface SecretProvider {
  getSecret(key: string): Promise<string>;
}

// Development: Use .env file
export class EnvFileSecretProvider implements SecretProvider {
  async getSecret(key: string): Promise<string> {
    const value = process.env[key];
    if (!value) {
      throw new Error(`Secret ${key} not found in environment`);
    }
    return value;
  }
}

// Production: Use AWS Secrets Manager
export class AWSSecretProvider implements SecretProvider {
  private secretManager: SecretManager;

  constructor() {
    this.secretManager = new SecretManager();
  }

  async getSecret(key: string): Promise<string> {
    const secrets = await this.secretManager.getSecret("prod/secrets");
    return secrets[key];
  }
}

// Factory
export function createSecretProvider(): SecretProvider {
  if (process.env.NODE_ENV === "production") {
    return new AWSSecretProvider();
  }
  return new EnvFileSecretProvider();
}
```
