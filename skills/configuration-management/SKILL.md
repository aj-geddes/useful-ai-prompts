---
name: configuration-management
description: Manage application configuration including environment variables, settings management, configuration hierarchies, secret management, feature flags, and 12-factor app principles. Use for config, environment setup, or settings management.
---

# Configuration Management

## Overview

Comprehensive guide to managing application configuration across environments, including environment variables, configuration files, secrets, feature flags, and following 12-factor app methodology.

## When to Use

- Setting up configuration for different environments
- Managing secrets and credentials
- Implementing feature flags
- Creating configuration hierarchies
- Following 12-factor app principles
- Migrating configuration to cloud services
- Implementing dynamic configuration
- Managing multi-tenant configurations

## Instructions

### 1. **Environment Variables**

#### Basic Setup (.env files)
```bash
# .env.development
NODE_ENV=development
PORT=3000
DATABASE_URL=postgresql://localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379
LOG_LEVEL=debug
API_KEY=dev-api-key-12345

# .env.production
NODE_ENV=production
PORT=8080
DATABASE_URL=${DATABASE_URL}  # From environment
REDIS_URL=${REDIS_URL}
LOG_LEVEL=info
API_KEY=${API_KEY}  # From secret manager

# .env.test
NODE_ENV=test
DATABASE_URL=postgresql://localhost:5432/myapp_test
LOG_LEVEL=error
```

#### Loading Environment Variables
```typescript
// config/env.ts
import dotenv from 'dotenv';
import path from 'path';

// Load environment-specific .env file
const envFile = `.env.${process.env.NODE_ENV || 'development'}`;
dotenv.config({ path: path.resolve(process.cwd(), envFile) });

// Validate required variables
const required = ['DATABASE_URL', 'PORT', 'API_KEY'];
const missing = required.filter(key => !process.env[key]);

if (missing.length > 0) {
  throw new Error(`Missing required environment variables: ${missing.join(', ')}`);
}

// Export typed configuration
export const config = {
  env: process.env.NODE_ENV || 'development',
  port: parseInt(process.env.PORT || '3000', 10),
  database: {
    url: process.env.DATABASE_URL!,
    poolSize: parseInt(process.env.DB_POOL_SIZE || '10', 10)
  },
  redis: {
    url: process.env.REDIS_URL || 'redis://localhost:6379'
  },
  logging: {
    level: process.env.LOG_LEVEL || 'info'
  },
  api: {
    key: process.env.API_KEY!,
    timeout: parseInt(process.env.API_TIMEOUT || '5000', 10)
  }
} as const;
```

#### Python Configuration
```python
# config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_file = f'.env.{os.getenv("ENVIRONMENT", "development")}'
load_dotenv(Path(__file__).parent.parent / env_file)

class Config:
    """Base configuration"""
    ENV = os.getenv('ENVIRONMENT', 'development')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database
    DATABASE_URL = os.getenv('DATABASE_URL')
    DB_POOL_SIZE = int(os.getenv('DB_POOL_SIZE', 10))

    # Redis
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

    # API
    API_KEY = os.getenv('API_KEY')
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', 5000))

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = 'INFO'

class TestConfig(Config):
    """Test configuration"""
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'

# Configuration dictionary
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}

# Get active config
config = config_by_name[Config.ENV]()
```

### 2. **Configuration Hierarchies**

```typescript
// config/config.ts
import deepmerge from 'deepmerge';

// Base configuration (shared across all environments)
const baseConfig = {
  app: {
    name: 'MyApp',
    version: '1.0.0'
  },
  server: {
    timeout: 30000,
    bodyLimit: '100kb'
  },
  database: {
    poolSize: 10,
    idleTimeout: 30000
  },
  logging: {
    format: 'json',
    destination: 'stdout'
  }
};

// Environment-specific overrides
const developmentConfig = {
  server: {
    port: 3000
  },
  database: {
    url: 'postgresql://localhost:5432/myapp_dev',
    logging: true
  },
  logging: {
    level: 'debug',
    prettyPrint: true
  }
};

const productionConfig = {
  server: {
    port: 8080,
    trustProxy: true
  },
  database: {
    url: process.env.DATABASE_URL,
    ssl: true,
    logging: false
  },
  logging: {
    level: 'info',
    prettyPrint: false
  }
};

// Merge configurations
const configs = {
  development: deepmerge(baseConfig, developmentConfig),
  production: deepmerge(baseConfig, productionConfig),
  test: deepmerge(baseConfig, {
    database: { url: 'postgresql://localhost:5432/myapp_test' }
  })
};

export const config = configs[process.env.NODE_ENV || 'development'];
```

#### YAML Configuration Files
```yaml
# config/default.yml
app:
  name: MyApp
  version: 1.0.0

server:
  timeout: 30000
  bodyLimit: 100kb

database:
  poolSize: 10
  idleTimeout: 30000

# config/development.yml
server:
  port: 3000

database:
  url: postgresql://localhost:5432/myapp_dev
  logging: true

logging:
  level: debug
  prettyPrint: true

# config/production.yml
server:
  port: 8080
  trustProxy: true

database:
  url: ${DATABASE_URL}
  ssl: true
  logging: false

logging:
  level: info
  prettyPrint: false
```

```typescript
// Load YAML config
import yaml from 'js-yaml';
import fs from 'fs';
import path from 'path';

function loadYamlConfig(env: string) {
  const defaultConfig = yaml.load(
    fs.readFileSync(path.join(__dirname, 'config/default.yml'), 'utf8')
  );

  const envConfig = yaml.load(
    fs.readFileSync(path.join(__dirname, `config/${env}.yml`), 'utf8')
  );

  return deepmerge(defaultConfig, envConfig);
}

export const config = loadYamlConfig(process.env.NODE_ENV || 'development');
```

### 3. **Secret Management**

#### AWS Secrets Manager
```typescript
// secrets/aws-secrets-manager.ts
import { SecretsManagerClient, GetSecretValueCommand } from '@aws-sdk/client-secrets-manager';

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

      const secret = JSON.parse(response.SecretString || '{}');

      // Cache the secret
      this.cache.set(secretName, {
        value: secret,
        expiry: Date.now() + this.cacheTtl
      });

      return secret;
    } catch (error) {
      throw new Error(`Failed to retrieve secret ${secretName}: ${error.message}`);
    }
  }

  async getDatabaseCredentials(): Promise<DatabaseCredentials> {
    return this.getSecret('prod/database/credentials');
  }

  async getApiKey(service: string): Promise<string> {
    const secrets = await this.getSecret('prod/api-keys');
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
    database: credentials.database
  });
}
```

#### HashiCorp Vault
```typescript
// secrets/vault.ts
import vault from 'node-vault';

export class VaultClient {
  private client: any;

  constructor() {
    this.client = vault({
      apiVersion: 'v1',
      endpoint: process.env.VAULT_ADDR || 'http://localhost:8200',
      token: process.env.VAULT_TOKEN
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
    return this.getSecret('secret/data/database');
  }

  async getApiKeys(): Promise<Record<string, string>> {
    return this.getSecret('secret/data/api-keys');
  }

  // Dynamic database credentials (rotated automatically)
  async getDynamicDBCredentials(): Promise<Credentials> {
    const result = await this.client.read('database/creds/readonly');
    return {
      username: result.data.username,
      password: result.data.password,
      leaseId: result.lease_id,
      leaseDuration: result.lease_duration
    };
  }
}
```

#### Environment-Specific Secrets
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
    const secrets = await this.secretManager.getSecret('prod/secrets');
    return secrets[key];
  }
}

// Factory
export function createSecretProvider(): SecretProvider {
  if (process.env.NODE_ENV === 'production') {
    return new AWSSecretProvider();
  }
  return new EnvFileSecretProvider();
}
```

### 4. **Feature Flags**

#### Simple Feature Flag Implementation
```typescript
// feature-flags/feature-flag.ts
export interface FeatureFlag {
  enabled: boolean;
  rolloutPercentage?: number;
  allowedUsers?: string[];
  allowedEnvironments?: string[];
}

export class FeatureFlagManager {
  private flags: Map<string, FeatureFlag>;

  constructor(flags: Record<string, FeatureFlag>) {
    this.flags = new Map(Object.entries(flags));
  }

  isEnabled(
    flagName: string,
    context?: { userId?: string; environment?: string }
  ): boolean {
    const flag = this.flags.get(flagName);
    if (!flag) return false;

    // Check if disabled globally
    if (!flag.enabled) return false;

    // Check environment restriction
    if (flag.allowedEnvironments && context?.environment) {
      if (!flag.allowedEnvironments.includes(context.environment)) {
        return false;
      }
    }

    // Check user whitelist
    if (flag.allowedUsers && context?.userId) {
      if (flag.allowedUsers.includes(context.userId)) {
        return true;
      }
    }

    // Check rollout percentage
    if (flag.rolloutPercentage !== undefined && context?.userId) {
      const hash = this.hashUserId(context.userId);
      return (hash % 100) < flag.rolloutPercentage;
    }

    return true;
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = ((hash << 5) - hash) + userId.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }
}

// Configuration
const featureFlags = {
  'new-dashboard': {
    enabled: true,
    rolloutPercentage: 50 // 50% of users
  },
  'experimental-feature': {
    enabled: true,
    allowedUsers: ['user-123', 'user-456'],
    allowedEnvironments: ['development', 'staging']
  },
  'beta-api': {
    enabled: true,
    rolloutPercentage: 10
  }
};

const flagManager = new FeatureFlagManager(featureFlags);

// Usage
app.get('/api/dashboard', (req, res) => {
  if (flagManager.isEnabled('new-dashboard', {
    userId: req.user.id,
    environment: process.env.NODE_ENV
  })) {
    return res.json(getNewDashboard());
  }

  return res.json(getOldDashboard());
});
```

#### LaunchDarkly Integration
```typescript
// feature-flags/launchdarkly.ts
import LaunchDarkly from 'launchdarkly-node-server-sdk';

export class LaunchDarklyClient {
  private client: LaunchDarkly.LDClient;

  async initialize() {
    this.client = LaunchDarkly.init(process.env.LAUNCHDARKLY_SDK_KEY!);
    await this.client.waitForInitialization();
  }

  async isEnabled(flagKey: string, user: LaunchDarkly.LDUser): Promise<boolean> {
    return this.client.variation(flagKey, user, false);
  }

  async getVariation<T>(
    flagKey: string,
    user: LaunchDarkly.LDUser,
    defaultValue: T
  ): Promise<T> {
    return this.client.variation(flagKey, user, defaultValue);
  }

  close() {
    this.client.close();
  }
}

// Usage
const ldClient = new LaunchDarklyClient();
await ldClient.initialize();

app.get('/api/dashboard', async (req, res) => {
  const user = {
    key: req.user.id,
    email: req.user.email,
    custom: {
      groups: req.user.groups
    }
  };

  const showNewDashboard = await ldClient.isEnabled('new-dashboard', user);

  if (showNewDashboard) {
    return res.json(getNewDashboard());
  }

  return res.json(getOldDashboard());
});
```

### 5. **12-Factor App Configuration**

```typescript
// config/twelve-factor.ts

/**
 * 12-Factor App Configuration Principles
 *
 * III. Config - Store config in the environment
 * - Strict separation of config from code
 * - Config varies between deploys, code does not
 * - Store in environment variables
 */

// ✅ Good: Configuration from environment
export const config = {
  database: {
    url: process.env.DATABASE_URL!,
    poolMin: parseInt(process.env.DB_POOL_MIN || '2', 10),
    poolMax: parseInt(process.env.DB_POOL_MAX || '10', 10)
  },
  redis: {
    url: process.env.REDIS_URL!
  },
  s3: {
    bucket: process.env.S3_BUCKET!,
    region: process.env.AWS_REGION!
  },
  sendgrid: {
    apiKey: process.env.SENDGRID_API_KEY!
  }
};

// ❌ Bad: Hardcoded configuration
const badConfig = {
  database: {
    host: 'prod-db.example.com',  // Hardcoded!
    password: 'secretpassword'     // Secret in code!
  }
};

/**
 * Backing Services - Treat backing services as attached resources
 * - Database, cache, message queue, etc. are accessed via URLs
 * - Should be swappable without code changes
 */

// ✅ Good: Backing service as URL
const db = createConnection(process.env.DATABASE_URL);
const cache = createClient(process.env.REDIS_URL);

// Can swap services by changing environment variable
// DATABASE_URL=postgresql://localhost/dev  (local dev)
// DATABASE_URL=postgresql://prod-db/app     (production)

/**
 * Disposability - Fast startup and graceful shutdown
 */
function startServer() {
  const server = app.listen(config.port, () => {
    console.log(`Server started on port ${config.port}`);
  });

  // Graceful shutdown
  process.on('SIGTERM', async () => {
    console.log('SIGTERM received, shutting down gracefully');

    server.close(() => {
      console.log('HTTP server closed');
    });

    await db.close();
    await cache.quit();

    process.exit(0);
  });
}
```

### 6. **Configuration Validation**

```typescript
// config/validation.ts
import Joi from 'joi';

const configSchema = Joi.object({
  NODE_ENV: Joi.string()
    .valid('development', 'production', 'test')
    .default('development'),

  PORT: Joi.number()
    .port()
    .default(3000),

  DATABASE_URL: Joi.string()
    .uri()
    .required(),

  REDIS_URL: Joi.string()
    .uri()
    .default('redis://localhost:6379'),

  LOG_LEVEL: Joi.string()
    .valid('debug', 'info', 'warn', 'error')
    .default('info'),

  API_KEY: Joi.string()
    .min(32)
    .required(),

  API_TIMEOUT: Joi.number()
    .min(1000)
    .max(30000)
    .default(5000),

  ENABLE_METRICS: Joi.boolean()
    .default(false)
});

export function validateConfig() {
  const { error, value } = configSchema.validate(process.env, {
    allowUnknown: true,  // Allow other env vars
    stripUnknown: true   // Remove unknown vars
  });

  if (error) {
    throw new Error(`Configuration validation error: ${error.message}`);
  }

  return value;
}

// Usage
const validatedConfig = validateConfig();
```

### 7. **Dynamic Configuration (Remote Config)**

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
      console.error('Failed to fetch remote config:', error);
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
const remoteConfig = new RemoteConfigService('https://config-service.example.com');
await remoteConfig.initialize();

app.get('/api/users', (req, res) => {
  const pageSize = remoteConfig.get('api.users.pageSize', 20);
  const enableCache = remoteConfig.get('api.users.enableCache', false);

  // Use dynamic config values
});
```

## Best Practices

### ✅ DO
- Store configuration in environment variables
- Use different config files per environment
- Validate configuration on startup
- Use secret managers for sensitive data
- Never commit secrets to version control
- Provide sensible defaults
- Document all configuration options
- Use type-safe configuration objects
- Implement configuration hierarchy (base + overrides)
- Use feature flags for gradual rollouts
- Follow 12-factor app principles
- Implement graceful degradation for missing config
- Cache secrets to reduce API calls

### ❌ DON'T
- Hardcode configuration in source code
- Commit .env files with real secrets
- Use different config formats across services
- Store secrets in plain text
- Expose configuration through APIs
- Use production credentials in development
- Ignore configuration validation errors
- Access process.env directly everywhere
- Store configuration in databases (circular dependency)
- Mix configuration with business logic

## Common Patterns

### Pattern 1: Config Service
```typescript
export class ConfigService {
  private static instance: ConfigService;
  private config: Config;

  private constructor() {
    this.config = loadAndValidateConfig();
  }

  static getInstance(): ConfigService {
    if (!ConfigService.instance) {
      ConfigService.instance = new ConfigService();
    }
    return ConfigService.instance;
  }

  get<K extends keyof Config>(key: K): Config[K] {
    return this.config[key];
  }
}
```

### Pattern 2: Configuration Builder
```typescript
export class ConfigBuilder {
  private config: Partial<Config> = {};

  withDatabase(url: string): this {
    this.config.database = { url };
    return this;
  }

  withRedis(url: string): this {
    this.config.redis = { url };
    return this;
  }

  build(): Config {
    return this.config as Config;
  }
}
```

## Tools & Resources

- **dotenv**: Load environment variables from .env files
- **convict**: Configuration management with validation
- **config**: Hierarchical configurations for Node.js
- **AWS Secrets Manager**: Cloud-based secret storage
- **HashiCorp Vault**: Secret and encryption management
- **LaunchDarkly**: Feature flag management
- **ConfigCat**: Feature flag and configuration service
- **Consul**: Service configuration and discovery
