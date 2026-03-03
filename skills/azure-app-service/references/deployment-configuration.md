# Deployment Configuration

## Deployment Configuration

```yaml
# .github/workflows/deploy.yml
name: Deploy to App Service

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build

      - name: Deploy to Azure
        uses: azure/webapps-deploy@v2
        with:
          app-name: myapp-web-prod
          publish-profile: ${{ secrets.AZURE_PUBLISH_PROFILE }}
          package: .

      - name: Swap slots
        uses: azure/CLI@v1
        with:
          azcliversion: 2.0.76
          inlineScript: |
            az webapp deployment slot swap \
              --resource-group myapp-rg-prod \
              --name myapp-web-prod \
              --slot staging
```
