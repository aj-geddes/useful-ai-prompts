# Ansible Deployment Script

## Ansible Deployment Script

```bash
#!/bin/bash
# ansible-deploy.sh - Deploy using Ansible

set -euo pipefail

ENVIRONMENT="${1:-dev}"
PLAYBOOK="${2:-site.yml}"
INVENTORY="inventory/hosts.ini"
LIMIT="${3:-all}"

echo "Deploying with Ansible: $PLAYBOOK"
echo "Environment: $ENVIRONMENT"
echo "Limit: $LIMIT"

# Syntax check
echo "Checking Ansible syntax..."
ansible-playbook --syntax-check \
  -i "$INVENTORY" \
  -e "environment=$ENVIRONMENT" \
  "$PLAYBOOK"

# Dry run
echo "Running dry-run..."
ansible-playbook \
  -i "$INVENTORY" \
  -e "environment=$ENVIRONMENT" \
  -l "$LIMIT" \
  --check \
  "$PLAYBOOK"

# Ask for confirmation
read -p "Continue with deployment? (y/n): " -r
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Deployment cancelled"
  exit 1
fi

# Execute playbook
echo "Executing playbook..."
ansible-playbook \
  -i "$INVENTORY" \
  -e "environment=$ENVIRONMENT" \
  -l "$LIMIT" \
  -v \
  "$PLAYBOOK"

echo "Deployment complete!"

# Run verification
echo "Running post-deployment verification..."
ansible-playbook \
  -i "$INVENTORY" \
  -e "environment=$ENVIRONMENT" \
  -l "$LIMIT" \
  verify.yml
```
