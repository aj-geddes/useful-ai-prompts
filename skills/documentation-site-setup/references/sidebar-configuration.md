# Sidebar Configuration

## Sidebar Configuration

```javascript
// sidebars.js
module.exports = {
  docs: [
    "intro",
    {
      type: "category",
      label: "Getting Started",
      items: [
        "getting-started/installation",
        "getting-started/quick-start",
        "getting-started/configuration",
      ],
    },
    {
      type: "category",
      label: "Guides",
      items: ["guides/authentication", "guides/database", "guides/deployment"],
    },
    {
      type: "category",
      label: "API Reference",
      items: ["api/overview", "api/endpoints", "api/errors"],
    },
  ],
};
```
