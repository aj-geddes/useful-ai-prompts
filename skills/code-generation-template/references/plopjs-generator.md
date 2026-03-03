# Plop.js Generator

## Plop.js Generator

```typescript
// plopfile.ts
import { NodePlopAPI } from "plop";

export default function (plop: NodePlopAPI) {
  // Component generator
  plop.setGenerator("component", {
    description: "React component",
    prompts: [
      {
        type: "input",
        name: "name",
        message: "Component name:",
      },
      {
        type: "list",
        name: "type",
        message: "Component type:",
        choices: ["functional", "class"],
      },
    ],
    actions: [
      {
        type: "add",
        path: "src/components/{{pascalCase name}}/{{pascalCase name}}.tsx",
        templateFile: "templates/component.hbs",
      },
      {
        type: "add",
        path: "src/components/{{pascalCase name}}/{{pascalCase name}}.test.tsx",
        templateFile: "templates/component.test.hbs",
      },
      {
        type: "add",
        path: "src/components/{{pascalCase name}}/index.ts",
        template:
          "export { {{pascalCase name}} } from './{{pascalCase name}}';\n",
      },
    ],
  });

  // API generator
  plop.setGenerator("api", {
    description: "API endpoint with full stack",
    prompts: [
      {
        type: "input",
        name: "name",
        message: "Resource name (e.g., user, post):",
      },
    ],
    actions: [
      {
        type: "add",
        path: "src/models/{{kebabCase name}}.model.ts",
        templateFile: "templates/model.hbs",
      },
      {
        type: "add",
        path: "src/services/{{kebabCase name}}.service.ts",
        templateFile: "templates/service.hbs",
      },
      {
        type: "add",
        path: "src/controllers/{{kebabCase name}}.controller.ts",
        templateFile: "templates/controller.hbs",
      },
      {
        type: "add",
        path: "src/routes/{{kebabCase name}}.routes.ts",
        templateFile: "templates/routes.hbs",
      },
    ],
  });
}
```
