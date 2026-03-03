---
name: code-generation-template
description: >
  Generate code from templates and patterns including scaffolding, boilerplate
  generation, AST-based code generation, and template engines. Use when
  generating code, scaffolding projects, creating boilerplate, or using
  templates.
---

# Code Generation & Templates

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to code generation techniques including template engines, AST manipulation, code scaffolding, and automated boilerplate generation for increased productivity and consistency.

## When to Use

- Scaffolding new projects or components
- Generating repetitive boilerplate code
- Creating CRUD operations automatically
- Generating API clients from OpenAPI specs
- Building code from templates
- Creating database models from schemas
- Generating TypeScript types from JSON Schema
- Building custom CLI generators

## Quick Start

Minimal working example:

```typescript
// templates/component.hbs
import React from 'react';

export interface {{pascalCase name}}Props {
  {{#each props}}
  {{this.name}}{{#if this.optional}}?{{/if}}: {{this.type}};
  {{/each}}
}

export const {{pascalCase name}}: React.FC<{{pascalCase name}}Props> = ({
  {{#each props}}{{this.name}},{{/each}}
}) => {
  return (
    <div className="{{kebabCase name}}">
      {/* Component implementation */}
    </div>
  );
};
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Template Engines](references/template-engines.md) | Template Engines |
| [AST-Based Code Generation](references/ast-based-code-generation.md) | AST-Based Code Generation |
| [Project Scaffolding](references/project-scaffolding.md) | Project Scaffolding |
| [OpenAPI Client Generation](references/openapi-client-generation.md) | OpenAPI Client Generation |
| [Database Model Generation](references/database-model-generation.md) | Database Model Generation |
| [GraphQL Code Generation](references/graphql-code-generation.md) | GraphQL Code Generation |
| [Plop.js Generator](references/plopjs-generator.md) | Plop.js Generator |

## Best Practices

### ✅ DO

- Use templates for repetitive code patterns
- Generate TypeScript types from schemas
- Include tests in generated code
- Follow project conventions in templates
- Add comments to explain generated code
- Version control your templates
- Make templates configurable
- Generate documentation alongside code
- Validate inputs before generating
- Use consistent naming conventions
- Keep templates simple and maintainable
- Provide CLI for easy generation

### ❌ DON'T

- Over-generate (avoid unnecessary complexity)
- Generate code that's hard to maintain
- Forget to validate generated code
- Hardcode values in templates
- Generate code without documentation
- Create generators for one-off use cases
- Mix business logic in templates
- Generate code without formatting
- Skip error handling in generators
- Create overly complex templates
