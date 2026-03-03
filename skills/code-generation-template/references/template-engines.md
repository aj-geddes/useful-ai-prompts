# Template Engines

## Template Engines

### Handlebars Templates

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
import Handlebars from "handlebars";
import fs from "fs";

// Register helpers
Handlebars.registerHelper("pascalCase", (str: string) =>
  str.replace(
    /(\w)(\w*)/g,
    (_, first, rest) => first.toUpperCase() + rest.toLowerCase(),
  ),
);

Handlebars.registerHelper("kebabCase", (str: string) =>
  str.replace(/([a-z])([A-Z])/g, "$1-$2").toLowerCase(),
);

// Load template
const templateSource = fs.readFileSync("templates/component.hbs", "utf8");
const template = Handlebars.compile(templateSource);

// Generate code
const code = template({
  name: "userProfile",
  props: [
    { name: "userId", type: "string", optional: false },
    { name: "onUpdate", type: "() => void", optional: true },
  ],
});

fs.writeFileSync("src/components/UserProfile.tsx", code);
```

### EJS Templates

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
import ejs from "ejs";

const code = await ejs.renderFile("templates/api-endpoint.ejs", {
  modelName: "User",
  kebabCase: (str: string) =>
    str
      .replace(/([A-Z])/g, "-$1")
      .toLowerCase()
      .slice(1),
  pluralize: (str: string) => str + "s",
});
```
