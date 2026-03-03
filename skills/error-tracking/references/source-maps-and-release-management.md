# Source Maps and Release Management

## Source Maps and Release Management

```javascript
// webpack.config.js
const SentryCliPlugin = require("@sentry/webpack-plugin");

module.exports = {
  plugins: [
    new SentryCliPlugin({
      include: "./dist",
      urlPrefix: "https://example.com/",
      release: process.env.APP_VERSION || "1.0.0",
      org: process.env.SENTRY_ORG,
      project: process.env.SENTRY_PROJECT,
      authToken: process.env.SENTRY_AUTH_TOKEN,
    }),
  ],
};
```


## CI/CD Release Creation

```bash
#!/bin/bash
VERSION=$(cat package.json | grep version | head -1 | awk -F: '{ print $2 }' | sed 's/[",]//g')

# Create release
sentry-cli releases -o my-org -p my-project create $VERSION

# Upload source maps
sentry-cli releases -o my-org -p my-project files $VERSION upload-sourcemaps ./dist

# Finalize release
sentry-cli releases -o my-org -p my-project finalize $VERSION

# Deploy
sentry-cli releases -o my-org -p my-project deploys $VERSION new -e production
```
