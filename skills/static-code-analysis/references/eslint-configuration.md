# ESLint Configuration

## ESLint Configuration

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:security/recommended",
  ],
  plugins: ["@typescript-eslint", "security", "import"],
  rules: {
    "no-console": ["warn", { allow: ["error", "warn"] }],
    "no-unused-vars": "error",
    "prefer-const": "error",
    eqeqeq: ["error", "always"],
    "no-eval": "error",
    "security/detect-object-injection": "warn",
    "security/detect-non-literal-regexp": "warn",
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/explicit-function-return-type": "error",
    "import/order": [
      "error",
      {
        groups: [
          "builtin",
          "external",
          "internal",
          "parent",
          "sibling",
          "index",
        ],
        "newlines-between": "always",
      },
    ],
  },
};
```
