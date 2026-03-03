# Environment Variables

## Environment Variables

### Basic Setup (.env files)

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

### Loading Environment Variables

```typescript
// config/env.ts
import dotenv from "dotenv";
import path from "path";

// Load environment-specific .env file
const envFile = `.env.${process.env.NODE_ENV || "development"}`;
dotenv.config({ path: path.resolve(process.cwd(), envFile) });

// Validate required variables
const required = ["DATABASE_URL", "PORT", "API_KEY"];
const missing = required.filter((key) => !process.env[key]);

if (missing.length > 0) {
  throw new Error(
    `Missing required environment variables: ${missing.join(", ")}`,
  );
}

// Export typed configuration
export const config = {
  env: process.env.NODE_ENV || "development",
  port: parseInt(process.env.PORT || "3000", 10),
  database: {
    url: process.env.DATABASE_URL!,
    poolSize: parseInt(process.env.DB_POOL_SIZE || "10", 10),
  },
  redis: {
    url: process.env.REDIS_URL || "redis://localhost:6379",
  },
  logging: {
    level: process.env.LOG_LEVEL || "info",
  },
  api: {
    key: process.env.API_KEY!,
    timeout: parseInt(process.env.API_TIMEOUT || "5000", 10),
  },
} as const;
```

### Python Configuration

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
