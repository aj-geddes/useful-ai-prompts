# Configuration Validation

## Configuration Validation

```typescript
// config/validation.ts
import Joi from "joi";

const configSchema = Joi.object({
  NODE_ENV: Joi.string()
    .valid("development", "production", "test")
    .default("development"),

  PORT: Joi.number().port().default(3000),

  DATABASE_URL: Joi.string().uri().required(),

  REDIS_URL: Joi.string().uri().default("redis://localhost:6379"),

  LOG_LEVEL: Joi.string()
    .valid("debug", "info", "warn", "error")
    .default("info"),

  API_KEY: Joi.string().min(32).required(),

  API_TIMEOUT: Joi.number().min(1000).max(30000).default(5000),

  ENABLE_METRICS: Joi.boolean().default(false),
});

export function validateConfig() {
  const { error, value } = configSchema.validate(process.env, {
    allowUnknown: true, // Allow other env vars
    stripUnknown: true, // Remove unknown vars
  });

  if (error) {
    throw new Error(`Configuration validation error: ${error.message}`);
  }

  return value;
}

// Usage
const validatedConfig = validateConfig();
```
