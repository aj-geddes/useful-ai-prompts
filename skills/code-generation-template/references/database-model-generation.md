# Database Model Generation

## Database Model Generation

```typescript
// prisma-schema-generator.ts
export class PrismaSchemaGenerator {
  generateModel(table: DatabaseTable): string {
    return `model ${pascalCase(table.name)} {
${table.columns.map((col) => this.generateField(col)).join("\n")}

${this.generateRelations(table.relations)}
${this.generateIndexes(table.indexes)}
}
`;
  }

  private generateField(column: Column): string {
    const optional = !column.required ? "?" : "";
    const unique = column.unique ? " @unique" : "";
    const defaultValue = column.default ? ` @default(${column.default})` : "";

    return `  ${column.name} ${this.mapType(column.type)}${optional}${unique}${defaultValue}`;
  }

  private mapType(sqlType: string): string {
    const typeMap: Record<string, string> = {
      varchar: "String",
      text: "String",
      integer: "Int",
      bigint: "BigInt",
      boolean: "Boolean",
      timestamp: "DateTime",
      date: "DateTime",
      json: "Json",
    };
    return typeMap[sqlType.toLowerCase()] || "String";
  }

  private generateRelations(relations: Relation[]): string {
    return relations
      .map((rel) => {
        if (rel.type === "hasMany") {
          return `  ${rel.name} ${rel.model}[]`;
        } else if (rel.type === "belongsTo") {
          return `  ${rel.name} ${rel.model} @relation(fields: [${rel.foreignKey}], references: [id])`;
        }
        return "";
      })
      .join("\n");
  }
}
```
