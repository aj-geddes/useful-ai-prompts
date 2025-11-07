---
name: code-generation-template
description: Generate code from templates and patterns including scaffolding, boilerplate generation, AST-based code generation, and template engines. Use when generating code, scaffolding projects, creating boilerplate, or using templates.
---

# Code Generation & Templates

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

## Instructions

### 1. **Template Engines**

#### Handlebars Templates
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

```typescript
// generator.ts
import Handlebars from 'handlebars';
import fs from 'fs';

// Register helpers
Handlebars.registerHelper('pascalCase', (str: string) =>
  str.replace(/(\w)(\w*)/g, (_, first, rest) =>
    first.toUpperCase() + rest.toLowerCase()
  )
);

Handlebars.registerHelper('kebabCase', (str: string) =>
  str.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase()
);

// Load template
const templateSource = fs.readFileSync('templates/component.hbs', 'utf8');
const template = Handlebars.compile(templateSource);

// Generate code
const code = template({
  name: 'userProfile',
  props: [
    { name: 'userId', type: 'string', optional: false },
    { name: 'onUpdate', type: '() => void', optional: true }
  ]
});

fs.writeFileSync('src/components/UserProfile.tsx', code);
```

#### EJS Templates
```typescript
// templates/api-endpoint.ejs
import { Router } from 'express';
import { <%= modelName %>Service } from '../services/<%= kebabCase(modelName) %>.service';

const router = Router();
const service = new <%= modelName %>Service();

// GET /<%= pluralize(kebabCase(modelName)) %>
router.get('/', async (req, res) => {
  try {
    const items = await service.findAll();
    res.json(items);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// GET /<%= pluralize(kebabCase(modelName)) %>/:id
router.get('/:id', async (req, res) => {
  try {
    const item = await service.findById(req.params.id);
    if (!item) {
      return res.status(404).json({ error: 'Not found' });
    }
    res.json(item);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// POST /<%= pluralize(kebabCase(modelName)) %>
router.post('/', async (req, res) => {
  try {
    const item = await service.create(req.body);
    res.status(201).json(item);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

export default router;
```

```typescript
// Using EJS
import ejs from 'ejs';

const code = await ejs.renderFile('templates/api-endpoint.ejs', {
  modelName: 'User',
  kebabCase: (str: string) => str.replace(/([A-Z])/g, '-$1').toLowerCase().slice(1),
  pluralize: (str: string) => str + 's'
});
```

### 2. **AST-Based Code Generation**

#### Using Babel/TypeScript AST
```typescript
// ast-generator.ts
import * as ts from 'typescript';

export class TypeScriptGenerator {
  // Generate interface
  generateInterface(name: string, properties: Array<{ name: string; type: string; optional?: boolean }>) {
    const members = properties.map(prop =>
      ts.factory.createPropertySignature(
        undefined,
        ts.factory.createIdentifier(prop.name),
        prop.optional ? ts.factory.createToken(ts.SyntaxKind.QuestionToken) : undefined,
        ts.factory.createTypeReferenceNode(prop.type)
      )
    );

    const interfaceDecl = ts.factory.createInterfaceDeclaration(
      [ts.factory.createToken(ts.SyntaxKind.ExportKeyword)],
      ts.factory.createIdentifier(name),
      undefined,
      undefined,
      members
    );

    return this.printNode(interfaceDecl);
  }

  // Generate class
  generateClass(name: string, properties: Array<{ name: string; type: string }>) {
    const propertyDecls = properties.map(prop =>
      ts.factory.createPropertyDeclaration(
        [ts.factory.createToken(ts.SyntaxKind.PrivateKeyword)],
        ts.factory.createIdentifier(prop.name),
        undefined,
        ts.factory.createTypeReferenceNode(prop.type),
        undefined
      )
    );

    const constructor = ts.factory.createConstructorDeclaration(
      undefined,
      properties.map(prop =>
        ts.factory.createParameterDeclaration(
          undefined,
          undefined,
          ts.factory.createIdentifier(prop.name),
          undefined,
          ts.factory.createTypeReferenceNode(prop.type)
        )
      ),
      ts.factory.createBlock(
        properties.map(prop =>
          ts.factory.createExpressionStatement(
            ts.factory.createBinaryExpression(
              ts.factory.createPropertyAccessExpression(
                ts.factory.createThis(),
                prop.name
              ),
              ts.SyntaxKind.EqualsToken,
              ts.factory.createIdentifier(prop.name)
            )
          )
        ),
        true
      )
    );

    const classDecl = ts.factory.createClassDeclaration(
      [ts.factory.createToken(ts.SyntaxKind.ExportKeyword)],
      ts.factory.createIdentifier(name),
      undefined,
      undefined,
      [...propertyDecls, constructor]
    );

    return this.printNode(classDecl);
  }

  private printNode(node: ts.Node): string {
    const sourceFile = ts.createSourceFile(
      'temp.ts',
      '',
      ts.ScriptTarget.Latest,
      false,
      ts.ScriptKind.TS
    );

    const printer = ts.createPrinter({ newLine: ts.NewLineKind.LineFeed });
    return printer.printNode(ts.EmitHint.Unspecified, node, sourceFile);
  }
}

// Usage
const generator = new TypeScriptGenerator();

const interfaceCode = generator.generateInterface('User', [
  { name: 'id', type: 'string' },
  { name: 'email', type: 'string' },
  { name: 'name', type: 'string', optional: true }
]);

const classCode = generator.generateClass('UserService', [
  { name: 'repository', type: 'UserRepository' },
  { name: 'logger', type: 'Logger' }
]);
```

### 3. **Project Scaffolding**

#### Simple CLI Generator
```typescript
// cli/generate.ts
#!/usr/bin/env node
import { Command } from 'commander';
import inquirer from 'inquirer';
import fs from 'fs-extra';
import path from 'path';

const program = new Command();

program
  .name('generate')
  .description('Code generator CLI')
  .version('1.0.0');

program
  .command('component <name>')
  .description('Generate a React component')
  .option('-d, --dir <directory>', 'Output directory', 'src/components')
  .action(async (name, options) => {
    const answers = await inquirer.prompt([
      {
        type: 'list',
        name: 'type',
        message: 'Component type?',
        choices: ['functional', 'class']
      },
      {
        type: 'confirm',
        name: 'typescript',
        message: 'Use TypeScript?',
        default: true
      },
      {
        type: 'confirm',
        name: 'test',
        message: 'Generate test file?',
        default: true
      }
    ]);

    await generateComponent(name, options.dir, answers);
  });

program
  .command('api <resource>')
  .description('Generate API endpoint with controller, service, and model')
  .action(async (resource) => {
    await generateApiResource(resource);
  });

program.parse();

async function generateComponent(name: string, dir: string, options: any) {
  const componentName = pascalCase(name);
  const ext = options.typescript ? 'tsx' : 'jsx';

  const template = options.type === 'functional'
    ? getFunctionalComponentTemplate(componentName, options.typescript)
    : getClassComponentTemplate(componentName, options.typescript);

  const componentPath = path.join(dir, `${componentName}.${ext}`);

  await fs.ensureDir(dir);
  await fs.writeFile(componentPath, template);

  console.log(`✓ Created ${componentPath}`);

  if (options.test) {
    const testTemplate = getTestTemplate(componentName, options.typescript);
    const testPath = path.join(dir, `${componentName}.test.${ext}`);
    await fs.writeFile(testPath, testTemplate);
    console.log(`✓ Created ${testPath}`);
  }
}

function getFunctionalComponentTemplate(name: string, ts: boolean): string {
  if (ts) {
    return `import React from 'react';

export interface ${name}Props {
  // Add props here
}

export const ${name}: React.FC<${name}Props> = (props) => {
  return (
    <div className="${kebabCase(name)}">
      <h1>${name}</h1>
    </div>
  );
};
`;
  }

  return `import React from 'react';

export const ${name} = (props) => {
  return (
    <div className="${kebabCase(name)}">
      <h1>${name}</h1>
    </div>
  );
};
`;
}

async function generateApiResource(resource: string) {
  const name = pascalCase(resource);

  // Generate model
  const modelCode = `export interface ${name} {
  id: string;
  createdAt: Date;
  updatedAt: Date;
  // Add fields here
}
`;
  await fs.writeFile(`src/models/${kebabCase(resource)}.model.ts`, modelCode);

  // Generate service
  const serviceCode = `import { ${name} } from '../models/${kebabCase(resource)}.model';

export class ${name}Service {
  async findAll(): Promise<${name}[]> {
    // Implement
    return [];
  }

  async findById(id: string): Promise<${name} | null> {
    // Implement
    return null;
  }

  async create(data: Partial<${name}>): Promise<${name}> {
    // Implement
    throw new Error('Not implemented');
  }

  async update(id: string, data: Partial<${name}>): Promise<${name}> {
    // Implement
    throw new Error('Not implemented');
  }

  async delete(id: string): Promise<void> {
    // Implement
  }
}
`;
  await fs.writeFile(`src/services/${kebabCase(resource)}.service.ts`, serviceCode);

  // Generate controller
  const controllerCode = `import { Router } from 'express';
import { ${name}Service } from '../services/${kebabCase(resource)}.service';

const router = Router();
const service = new ${name}Service();

router.get('/', async (req, res) => {
  const items = await service.findAll();
  res.json(items);
});

router.get('/:id', async (req, res) => {
  const item = await service.findById(req.params.id);
  if (!item) return res.status(404).json({ error: 'Not found' });
  res.json(item);
});

router.post('/', async (req, res) => {
  const item = await service.create(req.body);
  res.status(201).json(item);
});

router.put('/:id', async (req, res) => {
  const item = await service.update(req.params.id, req.body);
  res.json(item);
});

router.delete('/:id', async (req, res) => {
  await service.delete(req.params.id);
  res.status(204).send();
});

export default router;
`;
  await fs.writeFile(`src/controllers/${kebabCase(resource)}.controller.ts`, controllerCode);

  console.log(`✓ Generated API resource: ${name}`);
}
```

### 4. **OpenAPI Client Generation**

```typescript
// openapi-client-generator.ts
import SwaggerParser from '@apidevtools/swagger-parser';
import { compile } from 'json-schema-to-typescript';

export class OpenAPIClientGenerator {
  async generate(specPath: string, outputDir: string) {
    const api = await SwaggerParser.parse(specPath);

    // Generate TypeScript types from schemas
    if (api.components?.schemas) {
      for (const [name, schema] of Object.entries(api.components.schemas)) {
        const ts = await compile(schema as any, name, {
          bannerComment: ''
        });
        await fs.writeFile(
          path.join(outputDir, 'types', `${name}.ts`),
          ts
        );
      }
    }

    // Generate API client methods
    for (const [path, pathItem] of Object.entries(api.paths)) {
      for (const [method, operation] of Object.entries(pathItem)) {
        if (['get', 'post', 'put', 'delete', 'patch'].includes(method)) {
          const clientMethod = this.generateClientMethod(
            method,
            path,
            operation as any
          );
          // Write to file...
        }
      }
    }
  }

  private generateClientMethod(
    method: string,
    path: string,
    operation: any
  ): string {
    const functionName = operation.operationId || this.pathToFunctionName(method, path);
    const parameters = operation.parameters || [];

    return `
async ${functionName}(${this.generateParameters(parameters)}): Promise<${this.getResponseType(operation)}> {
  const response = await this.request('${method.toUpperCase()}', '${path}', {
    ${this.generateRequestOptions(parameters)}
  });
  return response.json();
}
`;
  }

  private generateParameters(parameters: any[]): string {
    return parameters
      .map(p => `${p.name}${p.required ? '' : '?'}: ${this.schemaToType(p.schema)}`)
      .join(', ');
  }

  private getResponseType(operation: any): string {
    const successResponse = operation.responses['200'] || operation.responses['201'];
    if (!successResponse) return 'any';

    const schema = successResponse.content?.['application/json']?.schema;
    return schema ? this.schemaToType(schema) : 'any';
  }

  private schemaToType(schema: any): string {
    if (schema.$ref) {
      return schema.$ref.split('/').pop();
    }
    if (schema.type === 'string') return 'string';
    if (schema.type === 'number' || schema.type === 'integer') return 'number';
    if (schema.type === 'boolean') return 'boolean';
    if (schema.type === 'array') return `${this.schemaToType(schema.items)}[]`;
    return 'any';
  }

  private pathToFunctionName(method: string, path: string): string {
    const cleanPath = path.replace(/\{.*?\}/g, 'By').replace(/[^a-zA-Z0-9]/g, '');
    return `${method}${cleanPath}`;
  }
}
```

### 5. **Database Model Generation**

```typescript
// prisma-schema-generator.ts
export class PrismaSchemaGenerator {
  generateModel(table: DatabaseTable): string {
    return `model ${pascalCase(table.name)} {
${table.columns.map(col => this.generateField(col)).join('\n')}

${this.generateRelations(table.relations)}
${this.generateIndexes(table.indexes)}
}
`;
  }

  private generateField(column: Column): string {
    const optional = !column.required ? '?' : '';
    const unique = column.unique ? ' @unique' : '';
    const defaultValue = column.default ? ` @default(${column.default})` : '';

    return `  ${column.name} ${this.mapType(column.type)}${optional}${unique}${defaultValue}`;
  }

  private mapType(sqlType: string): string {
    const typeMap: Record<string, string> = {
      'varchar': 'String',
      'text': 'String',
      'integer': 'Int',
      'bigint': 'BigInt',
      'boolean': 'Boolean',
      'timestamp': 'DateTime',
      'date': 'DateTime',
      'json': 'Json'
    };
    return typeMap[sqlType.toLowerCase()] || 'String';
  }

  private generateRelations(relations: Relation[]): string {
    return relations.map(rel => {
      if (rel.type === 'hasMany') {
        return `  ${rel.name} ${rel.model}[]`;
      } else if (rel.type === 'belongsTo') {
        return `  ${rel.name} ${rel.model} @relation(fields: [${rel.foreignKey}], references: [id])`;
      }
      return '';
    }).join('\n');
  }
}
```

### 6. **GraphQL Code Generation**

```typescript
// graphql-codegen.config.ts
import type { CodegenConfig } from '@graphql-codegen/cli';

const config: CodegenConfig = {
  schema: 'http://localhost:4000/graphql',
  documents: ['src/**/*.tsx', 'src/**/*.ts'],
  generates: {
    './src/generated/graphql.ts': {
      plugins: [
        'typescript',
        'typescript-operations',
        'typescript-react-apollo'
      ],
      config: {
        withHooks: true,
        withComponent: false,
        withHOC: false
      }
    },
    './src/generated/introspection.json': {
      plugins: ['introspection']
    }
  }
};

export default config;
```

### 7. **Plop.js Generator**

```typescript
// plopfile.ts
import { NodePlopAPI } from 'plop';

export default function (plop: NodePlopAPI) {
  // Component generator
  plop.setGenerator('component', {
    description: 'React component',
    prompts: [
      {
        type: 'input',
        name: 'name',
        message: 'Component name:'
      },
      {
        type: 'list',
        name: 'type',
        message: 'Component type:',
        choices: ['functional', 'class']
      }
    ],
    actions: [
      {
        type: 'add',
        path: 'src/components/{{pascalCase name}}/{{pascalCase name}}.tsx',
        templateFile: 'templates/component.hbs'
      },
      {
        type: 'add',
        path: 'src/components/{{pascalCase name}}/{{pascalCase name}}.test.tsx',
        templateFile: 'templates/component.test.hbs'
      },
      {
        type: 'add',
        path: 'src/components/{{pascalCase name}}/index.ts',
        template: "export { {{pascalCase name}} } from './{{pascalCase name}}';\n"
      }
    ]
  });

  // API generator
  plop.setGenerator('api', {
    description: 'API endpoint with full stack',
    prompts: [
      {
        type: 'input',
        name: 'name',
        message: 'Resource name (e.g., user, post):'
      }
    ],
    actions: [
      {
        type: 'add',
        path: 'src/models/{{kebabCase name}}.model.ts',
        templateFile: 'templates/model.hbs'
      },
      {
        type: 'add',
        path: 'src/services/{{kebabCase name}}.service.ts',
        templateFile: 'templates/service.hbs'
      },
      {
        type: 'add',
        path: 'src/controllers/{{kebabCase name}}.controller.ts',
        templateFile: 'templates/controller.hbs'
      },
      {
        type: 'add',
        path: 'src/routes/{{kebabCase name}}.routes.ts',
        templateFile: 'templates/routes.hbs'
      }
    ]
  });
}
```

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

## Common Patterns

### Pattern 1: CRUD Generator
```typescript
export function generateCRUD(entityName: string) {
  return {
    model: generateModel(entityName),
    service: generateService(entityName),
    controller: generateController(entityName),
    routes: generateRoutes(entityName),
    tests: generateTests(entityName)
  };
}
```

### Pattern 2: Migration Generator
```typescript
export function generateMigration(name: string, changes: SchemaChange[]) {
  return {
    up: generateUpMigration(changes),
    down: generateDownMigration(changes)
  };
}
```

### Pattern 3: Factory Generator
```typescript
export function generateFactory(model: Model) {
  return `export const create${model.name} = (overrides?: Partial<${model.name}>): ${model.name} => ({
  ${model.fields.map(f => `${f.name}: ${getDefaultValue(f)}`).join(',\n  ')},
  ...overrides
});`;
}
```

## Tools & Resources

- **Plop**: Micro-generator framework
- **Yeoman**: Scaffolding tool
- **Hygen**: Code generator with templates
- **GraphQL Code Generator**: Generate code from GraphQL
- **Prisma**: Database ORM with code generation
- **OpenAPI Generator**: Generate clients from OpenAPI
- **json-schema-to-typescript**: Generate TS types
- **TypeScript Compiler API**: AST manipulation
