# AST-Based Code Generation

## AST-Based Code Generation

### Using Babel/TypeScript AST

```typescript
// ast-generator.ts
import * as ts from "typescript";

export class TypeScriptGenerator {
  // Generate interface
  generateInterface(
    name: string,
    properties: Array<{ name: string; type: string; optional?: boolean }>,
  ) {
    const members = properties.map((prop) =>
      ts.factory.createPropertySignature(
        undefined,
        ts.factory.createIdentifier(prop.name),
        prop.optional
          ? ts.factory.createToken(ts.SyntaxKind.QuestionToken)
          : undefined,
        ts.factory.createTypeReferenceNode(prop.type),
      ),
    );

    const interfaceDecl = ts.factory.createInterfaceDeclaration(
      [ts.factory.createToken(ts.SyntaxKind.ExportKeyword)],
      ts.factory.createIdentifier(name),
      undefined,
      undefined,
      members,
    );

    return this.printNode(interfaceDecl);
  }

  // Generate class
  generateClass(
    name: string,
    properties: Array<{ name: string; type: string }>,
  ) {
    const propertyDecls = properties.map((prop) =>
      ts.factory.createPropertyDeclaration(
        [ts.factory.createToken(ts.SyntaxKind.PrivateKeyword)],
        ts.factory.createIdentifier(prop.name),
        undefined,
        ts.factory.createTypeReferenceNode(prop.type),
        undefined,
      ),
    );

    const constructor = ts.factory.createConstructorDeclaration(
      undefined,
      properties.map((prop) =>
        ts.factory.createParameterDeclaration(
          undefined,
          undefined,
          ts.factory.createIdentifier(prop.name),
          undefined,
          ts.factory.createTypeReferenceNode(prop.type),
        ),
      ),
      ts.factory.createBlock(
        properties.map((prop) =>
          ts.factory.createExpressionStatement(
            ts.factory.createBinaryExpression(
              ts.factory.createPropertyAccessExpression(
                ts.factory.createThis(),
                prop.name,
              ),
              ts.SyntaxKind.EqualsToken,
              ts.factory.createIdentifier(prop.name),
            ),
          ),
        ),
        true,
      ),
    );

    const classDecl = ts.factory.createClassDeclaration(
      [ts.factory.createToken(ts.SyntaxKind.ExportKeyword)],
      ts.factory.createIdentifier(name),
      undefined,
      undefined,
      [...propertyDecls, constructor],
    );

    return this.printNode(classDecl);
  }

  private printNode(node: ts.Node): string {
    const sourceFile = ts.createSourceFile(
      "temp.ts",
      "",
      ts.ScriptTarget.Latest,
      false,
      ts.ScriptKind.TS,
    );

    const printer = ts.createPrinter({ newLine: ts.NewLineKind.LineFeed });
    return printer.printNode(ts.EmitHint.Unspecified, node, sourceFile);
  }
}

// Usage
const generator = new TypeScriptGenerator();

const interfaceCode = generator.generateInterface("User", [
  { name: "id", type: "string" },
  { name: "email", type: "string" },
  { name: "name", type: "string", optional: true },
]);

const classCode = generator.generateClass("UserService", [
  { name: "repository", type: "UserRepository" },
  { name: "logger", type: "Logger" },
]);
```
