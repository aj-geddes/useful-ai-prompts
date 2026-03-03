# Project Scaffolding

## Project Scaffolding

### Simple CLI Generator

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
