# BackstopJS Configuration

## BackstopJS Configuration

```javascript
// backstop.config.js
module.exports = {
  id: "visual_regression",
  viewports: [
    {
      label: "phone",
      width: 375,
      height: 667,
    },
    {
      label: "tablet",
      width: 768,
      height: 1024,
    },
    {
      label: "desktop",
      width: 1920,
      height: 1080,
    },
  ],
  scenarios: [
    {
      label: "Homepage",
      url: "http://localhost:3000",
      delay: 500,
      misMatchThreshold: 0.1,
      requireSameDimensions: true,
    },
    {
      label: "Product List",
      url: "http://localhost:3000/products",
      delay: 1000,
      removeSelectors: [".timestamp", ".ad-banner"],
    },
    {
      label: "Product Detail",
      url: "http://localhost:3000/products/123",
      clickSelector: ".size-guide-link",
      postInteractionWait: 500,
    },
    {
      label: "Hover State",
      url: "http://localhost:3000",
      hoverSelector: ".primary-button",
      postInteractionWait: 200,
    },
  ],
  paths: {
    bitmaps_reference: "backstop_data/bitmaps_reference",
    bitmaps_test: "backstop_data/bitmaps_test",
    html_report: "backstop_data/html_report",
  },
  engine: "puppeteer",
  engineOptions: {
    args: ["--no-sandbox"],
  },
  asyncCaptureLimit: 5,
  asyncCompareLimit: 50,
  debug: false,
  debugWindow: false,
};
```

```bash
# Create reference images
backstop reference

# Run test
backstop test

# Approve changes
backstop approve
```
