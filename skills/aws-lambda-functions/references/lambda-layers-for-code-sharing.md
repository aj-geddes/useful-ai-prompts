# Lambda Layers for Code Sharing

## Lambda Layers for Code Sharing

```bash
# Create layer directory structure
mkdir -p layer/nodejs/node_modules
cd layer/nodejs

# Install dependencies
npm install lodash axios moment

# Go back and create zip
cd ..
zip -r layer.zip .

# Upload layer
aws lambda publish-layer-version \
  --layer-name shared-utils \
  --zip-file fileb://layer.zip \
  --compatible-runtimes nodejs18.x
```
