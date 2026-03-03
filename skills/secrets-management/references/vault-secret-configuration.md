# Vault Secret Configuration

## Vault Secret Configuration

```bash
#!/bin/bash
# vault-setup.sh - Configure Vault for applications

set -euo pipefail

VAULT_ADDR="https://vault:8200"
VAULT_TOKEN="${VAULT_TOKEN}"

export VAULT_ADDR
export VAULT_TOKEN

echo "Setting up Vault secrets..."

# Enable secret engines
vault secrets enable -version=2 kv
vault secrets enable -path=database database

# Create database credentials
vault write database/config/mydb \
  plugin_name=postgresql-database-plugin \
  allowed_roles="readonly,readwrite" \
  connection_url="postgresql://{{username}}:{{password}}@postgres:5432/mydb" \
  username="vault_admin" \
  password="vault_password"

# Create database roles
vault write database/roles/readonly \
  db_name=mydb \
  creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';" \
  revocation_statements="DROP ROLE IF EXISTS \"{{name}}\";" \
  default_ttl="1h" \
  max_ttl="24h"

# Create API secrets
vault kv put secret/api/keys \
  github_token="ghp_xxxxxxxxxxx" \
  aws_access_key="AKIAIOSFODNN7EXAMPLE" \
  aws_secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
  slack_webhook="https://hooks.slack.com/services/..."

# Create TLS certificates
vault write -f pki/root/generate/internal \
  common_name="my-root-ca" \
  ttl="87600h"

vault write pki/roles/my-domain \
  allowed_domains="*.myapp.com,myapp.com" \
  allow_subdomains=true \
  max_ttl="720h"

# Setup auto-unseal
vault write sys/seal/migrate/start \
  migrate_from_seal_type="shamir"

echo "Vault setup completed"
```
