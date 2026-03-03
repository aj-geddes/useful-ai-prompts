# Terraform Deployment Script

## Terraform Deployment Script

```bash
#!/bin/bash
# deploy-terraform.sh - Terraform deployment automation

set -euo pipefail

ENVIRONMENT="${1:-dev}"
ACTION="${2:-plan}"
TF_DIR="terraform"

echo "Terraform $ACTION for environment: $ENVIRONMENT"

cd "$TF_DIR"

# Initialize Terraform
echo "Initializing Terraform..."
terraform init -upgrade

# Format and validate
echo "Validating Terraform configuration..."
terraform fmt -recursive -check .
terraform validate

# Create/select workspace
echo "Creating/selecting workspace: $ENVIRONMENT"
terraform workspace select -or-create "$ENVIRONMENT"

# Plan or apply
case "$ACTION" in
  plan)
    echo "Creating Terraform plan..."
    terraform plan \
      -var-file="environments/$ENVIRONMENT.tfvars" \
      -out="tfplan-$ENVIRONMENT"
    ;;
  apply)
    echo "Applying Terraform changes..."
    terraform apply \
      -var-file="environments/$ENVIRONMENT.tfvars" \
      -auto-approve
    ;;
  destroy)
    echo "WARNING: Destroying infrastructure in $ENVIRONMENT"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
      terraform destroy \
        -var-file="environments/$ENVIRONMENT.tfvars" \
        -auto-approve
    fi
    ;;
  *)
    echo "Unknown action: $ACTION"
    exit 1
    ;;
esac

echo "Terraform $ACTION complete!"
```
