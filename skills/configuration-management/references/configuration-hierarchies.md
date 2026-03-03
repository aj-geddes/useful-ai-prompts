# Configuration Hierarchies

## Configuration Hierarchies

```typescript
// config/config.ts
import deepmerge from "deepmerge";

// Base configuration (shared across all environments)
const baseConfig = {
  app: {
    name: "MyApp",
    version: "1.0.0",
  },
  server: {
    timeout: 30000,
    bodyLimit: "100kb",
  },
  database: {
    poolSize: 10,
    idleTimeout: 30000,
  },
  logging: {
    format: "json",
    destination: "stdout",
  },
};

// Environment-specific overrides
const developmentConfig = {
  server: {
    port: 3000,
  },
  database: {
    url: "postgresql://localhost:5432/myapp_dev",
    logging: true,
  },
  logging: {
    level: "debug",
    prettyPrint: true,
  },
};

const productionConfig = {
  server: {
    port: 8080,
    trustProxy: true,
  },
  database: {
    url: process.env.DATABASE_URL,
    ssl: true,
    logging: false,
  },
  logging: {
    level: "info",
    prettyPrint: false,
  },
};

// Merge configurations
const configs = {
  development: deepmerge(baseConfig, developmentConfig),
  production: deepmerge(baseConfig, productionConfig),
  test: deepmerge(baseConfig, {
    database: { url: "postgresql://localhost:5432/myapp_test" },
  }),
};

export const config = configs[process.env.NODE_ENV || "development"];
```

### YAML Configuration Files

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
import yaml from "js-yaml";
import fs from "fs";
import path from "path";

function loadYamlConfig(env: string) {
  const defaultConfig = yaml.load(
    fs.readFileSync(path.join(__dirname, "config/default.yml"), "utf8"),
  );

  const envConfig = yaml.load(
    fs.readFileSync(path.join(__dirname, `config/${env}.yml`), "utf8"),
  );

  return deepmerge(defaultConfig, envConfig);
}

export const config = loadYamlConfig(process.env.NODE_ENV || "development");
```
