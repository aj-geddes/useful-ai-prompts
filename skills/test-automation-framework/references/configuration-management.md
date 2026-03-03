# Configuration Management

## Configuration Management

```typescript
// framework/config/config.ts
import * as dotenv from "dotenv";

dotenv.config();

export interface TestConfig {
  baseUrl: string;
  apiUrl: string;
  timeout: number;
  headless: boolean;
  slowMo: number;
  screenshots: boolean;
  video: boolean;
  testUser: {
    email: string;
    password: string;
  };
}

const environments: Record<string, TestConfig> = {
  development: {
    baseUrl: "http://localhost:3000",
    apiUrl: "http://localhost:3001",
    timeout: 30000,
    headless: false,
    slowMo: 0,
    screenshots: true,
    video: false,
    testUser: {
      email: "dev@test.com",
      password: "devpass123",
    },
  },
  staging: {
    baseUrl: "https://staging.example.com",
    apiUrl: "https://api-staging.example.com",
    timeout: 60000,
    headless: true,
    slowMo: 0,
    screenshots: true,
    video: true,
    testUser: {
      email: process.env.STAGING_USER_EMAIL!,
      password: process.env.STAGING_USER_PASSWORD!,
    },
  },
  production: {
    baseUrl: "https://example.com",
    apiUrl: "https://api.example.com",
    timeout: 60000,
    headless: true,
    slowMo: 100,
    screenshots: true,
    video: true,
    testUser: {
      email: process.env.PROD_USER_EMAIL!,
      password: process.env.PROD_USER_PASSWORD!,
    },
  },
};

export const config: TestConfig =
  environments[process.env.TEST_ENV || "development"];
```
