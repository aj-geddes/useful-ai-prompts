# OpenAPI Client Generation

## OpenAPI Client Generation

```typescript
// openapi-client-generator.ts
import SwaggerParser from "@apidevtools/swagger-parser";
import { compile } from "json-schema-to-typescript";

export class OpenAPIClientGenerator {
  async generate(specPath: string, outputDir: string) {
    const api = await SwaggerParser.parse(specPath);

    // Generate TypeScript types from schemas
    if (api.components?.schemas) {
      for (const [name, schema] of Object.entries(api.components.schemas)) {
        const ts = await compile(schema as any, name, {
          bannerComment: "",
        });
        await fs.writeFile(path.join(outputDir, "types", `${name}.ts`), ts);
      }
    }

    // Generate API client methods
    for (const [path, pathItem] of Object.entries(api.paths)) {
      for (const [method, operation] of Object.entries(pathItem)) {
        if (["get", "post", "put", "delete", "patch"].includes(method)) {
          const clientMethod = this.generateClientMethod(
            method,
            path,
            operation as any,
          );
          // Write to file...
        }
      }
    }
  }

  private generateClientMethod(
    method: string,
    path: string,
    operation: any,
  ): string {
    const functionName =
      operation.operationId || this.pathToFunctionName(method, path);
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
      .map(
        (p) =>
          `${p.name}${p.required ? "" : "?"}: ${this.schemaToType(p.schema)}`,
      )
      .join(", ");
  }

  private getResponseType(operation: any): string {
    const successResponse =
      operation.responses["200"] || operation.responses["201"];
    if (!successResponse) return "any";

    const schema = successResponse.content?.["application/json"]?.schema;
    return schema ? this.schemaToType(schema) : "any";
  }

  private schemaToType(schema: any): string {
    if (schema.$ref) {
      return schema.$ref.split("/").pop();
    }
    if (schema.type === "string") return "string";
    if (schema.type === "number" || schema.type === "integer") return "number";
    if (schema.type === "boolean") return "boolean";
    if (schema.type === "array") return `${this.schemaToType(schema.items)}[]`;
    return "any";
  }

  private pathToFunctionName(method: string, path: string): string {
    const cleanPath = path
      .replace(/\{.*?\}/g, "By")
      .replace(/[^a-zA-Z0-9]/g, "");
    return `${method}${cleanPath}`;
  }
}
```
