# GitHub Actions Deployment Workflow

## GitHub Actions Deployment Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: "Environment to deploy to"
        required: true
        default: "staging"
        type: choice
        options:
          - staging
          - production

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: ${{ github.event.inputs.environment || 'staging' }}
    permissions:
      contents: read
      packages: read

    steps:
      - uses: actions/checkout@v3

      - name: Determine target environment
        id: env
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "environment=staging" >> $GITHUB_OUTPUT
          else
            echo "environment=staging" >> $GITHUB_OUTPUT
          fi

      - name: Setup kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: "latest"

      - name: Configure kubectl
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > $HOME/.kube/config
          chmod 600 $HOME/.kube/config

      - name: Deploy with Helm
        run: |
          helm repo add myrepo ${{ secrets.HELM_REPO_URL }}
          helm repo update

          helm upgrade --install myapp myrepo/myapp \
            --namespace ${{ steps.env.outputs.environment }} \
            --create-namespace \
            --values helm/values-${{ steps.env.outputs.environment }}.yaml \
            --set image.tag=${{ github.sha }} \
            --wait \
            --timeout 5m

      - name: Verify deployment
        run: |
          kubectl rollout status deployment/myapp \
            -n ${{ steps.env.outputs.environment }} \
            --timeout=5m
```
