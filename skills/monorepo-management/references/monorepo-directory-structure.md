# Monorepo Directory Structure

## Monorepo Directory Structure

```bash
monorepo/
├── packages/
│   ├── core/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   ├── utils/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── shared/
│       ├── src/
│       ├── package.json
│       └── tsconfig.json
├── apps/
│   ├── web/
│   │   ├── pages/
│   │   ├── package.json
│   │   └── next.config.js
│   ├── api/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── mobile/
│       ├── src/
│       ├── package.json
│       └── app.json
├── tools/
│   ├── scripts/
│   └── generators/
├── lerna.json
├── turbo.json
├── nx.json
├── package.json
├── tsconfig.json
└── .github/workflows/
```
