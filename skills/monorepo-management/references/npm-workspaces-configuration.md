# Npm Workspaces Configuration

## Npm Workspaces Configuration

```json
{
  "name": "monorepo-root",
  "version": "1.0.0",
  "private": true,
  "workspaces": ["packages/*", "apps/*"],
  "devDependencies": {
    "lerna": "^7.0.0",
    "turbo": "^1.10.0"
  },
  "scripts": {
    "lint": "npm run lint -r",
    "test": "npm run test -r",
    "build": "npm run build -r",
    "clean": "npm run clean -r"
  }
}
```


## Lerna Configuration

```json
{
  "name": "monorepo-with-lerna",
  "version": "1.0.0",
  "private": true,
  "packages": ["packages/*", "apps/*"],
  "command": {
    "bootstrap": {
      "hoist": true,
      "ignore": "@myorg/infra"
    },
    "publish": {
      "conventionalCommits": true,
      "createRelease": "github",
      "message": "chore(release): publish"
    }
  }
}
```


## Turborepo Configuration

```json
{
  "turbo": {
    "globalDependencies": ["tsconfig.json"],
    "pipeline": {
      "build": {
        "dependsOn": ["^build"],
        "outputs": ["dist/**", ".next/**"],
        "cache": true
      },
      "test": {
        "dependsOn": ["^build"],
        "cache": true,
        "outputs": ["coverage/**"]
      },
      "lint": {
        "outputs": []
      },
      "dev": {
        "cache": false,
        "persistent": true
      }
    }
  }
}
```


## Nx Workspace Configuration

```json
{
  "version": 2,
  "projectNameAndRootFormat": "as-provided",
  "plugins": ["@nx/next/plugin", "@nx/react/plugin", "@nx/node/plugin"],
  "targetDefaults": {
    "build": {
      "cache": true,
      "inputs": ["production", "^production"]
    },
    "test": {
      "cache": true,
      "inputs": ["default", "^production"]
    }
  }
}
```
