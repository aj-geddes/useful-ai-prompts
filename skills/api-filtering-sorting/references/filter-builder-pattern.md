# Filter Builder Pattern

## Filter Builder Pattern

```javascript
// Fluent filter builder
class QueryBuilder {
  constructor(model) {
    this.model = model;
    this.query = {};
    this.sortBy = {};
    this.pageSize = 20;
    this.pageNum = 1;
  }

  filter(field, operator, value) {
    const operators = {
      "=": "$eq",
      "!=": "$ne",
      ">": "$gt",
      ">=": "$gte",
      "<": "$lt",
      "<=": "$lte",
      in: "$in",
      regex: "$regex",
    };

    const mongoOp = operators[operator];
    if (!mongoOp) throw new Error(`Invalid operator: ${operator}`);

    this.query[field] = { [mongoOp]: value };
    return this;
  }

  range(field, min, max) {
    this.query[field] = { $gte: min, $lte: max };
    return this;
  }

  search(text, fields) {
    this.query.$or = fields.map((field) => ({
      [field]: { $regex: text, $options: "i" },
    }));
    return this;
  }

  sort(field, direction = "asc") {
    this.sortBy[field] = direction === "asc" ? 1 : -1;
    return this;
  }

  pagination(page = 1, limit = 20) {
    this.pageNum = page;
    this.pageSize = Math.min(limit, 100);
    return this;
  }

  async execute() {
    const offset = (this.pageNum - 1) * this.pageSize;

    const [data, total] = await Promise.all([
      this.model
        .find(this.query)
        .sort(this.sortBy)
        .skip(offset)
        .limit(this.pageSize),
      this.model.countDocuments(this.query),
    ]);

    return {
      data,
      pagination: {
        page: this.pageNum,
        limit: this.pageSize,
        total,
        totalPages: Math.ceil(total / this.pageSize),
      },
    };
  }
}

// Usage
const results = await new QueryBuilder(Product)
  .filter("category", "=", "electronics")
  .range("price", 100, 500)
  .filter("inStock", "=", true)
  .sort("price", "asc")
  .pagination(1, 20)
  .execute();
```
