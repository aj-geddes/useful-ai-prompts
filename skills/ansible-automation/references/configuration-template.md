# Configuration Template

## Configuration Template

```jinja2
# roles/application/templates/.env.j2
# Environment Configuration
NODE_ENV={{ environment }}
LOG_LEVEL={{ log_level }}
PORT=8080

# Database Configuration
DATABASE_URL=postgresql://{{ db_user }}:{{ db_password }}@{{ db_host }}:5432/{{ db_name }}
DATABASE_POOL_SIZE=20
DATABASE_TIMEOUT=30000

# Cache Configuration
REDIS_URL=redis://{{ redis_host }}:6379
CACHE_TTL=3600

# Application Configuration
APP_NAME=MyApp
APP_VERSION={{ app_version }}
WORKERS={{ ansible_processor_vcpus }}

# API Configuration
API_TIMEOUT=30000
API_RATE_LIMIT=1000

# Monitoring
SENTRY_DSN={{ sentry_dsn | default('') }}
DATADOG_API_KEY={{ datadog_api_key | default('') }}
```
