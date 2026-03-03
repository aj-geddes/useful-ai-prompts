# Advanced Filter Parser

## Advanced Filter Parser

```javascript
// Parse complex filter queries
class FilterParser {
  static parse(queryString) {
    const filters = {};
    const params = new URLSearchParams(queryString);

    params.forEach((value, key) => {
      // Handle nested filters (e.g., user.email, address.city)
      if (key.includes(".")) {
        this.setNested(filters, key, value);
      } else {
        filters[key] = this.parseValue(value);
      }
    });

    return filters;
  }

  static setNested(obj, path, value) {
    const keys = path.split(".");
    let current = obj;

    for (let i = 0; i < keys.length - 1; i++) {
      const key = keys[i];
      if (!current[key]) current[key] = {};
      current = current[key];
    }

    current[keys[keys.length - 1]] = this.parseValue(value);
  }

  static parseValue(value) {
    // Handle operator syntax: gt:100, lt:200, in:a,b,c
    if (typeof value !== "string") return value;

    const operatorMatch = value.match(
      /^(eq|ne|gt|gte|lt|lte|in|nin|exists|regex):(.+)$/,
    );
    if (operatorMatch) {
      const [, operator, operandValue] = operatorMatch;

      const operators = {
        eq: { $eq: operandValue },
        ne: { $ne: operandValue },
        gt: { $gt: parseFloat(operandValue) },
        gte: { $gte: parseFloat(operandValue) },
        lt: { $lt: parseFloat(operandValue) },
        lte: { $lte: parseFloat(operandValue) },
        in: { $in: operandValue.split(",") },
        nin: { $nin: operandValue.split(",") },
        exists: { $exists: operandValue === "true" },
        regex: { $regex: operandValue, $options: "i" },
      };

      return operators[operator];
    }

    // Parse booleans
    if (value === "true") return true;
    if (value === "false") return false;

    // Parse numbers
    if (!isNaN(value)) return parseFloat(value);

    return value;
  }
}

// Usage
app.get("/api/advanced-search", async (req, res) => {
  const filters = FilterParser.parse(req.url.split("?")[1]);

  const products = await Product.find(filters);
  res.json({ data: products });
});

// Example queries:
// /api/advanced-search?price=gte:100&price=lt:500&category=electronics
// /api/advanced-search?rating=gte:4&inStock=exists:true
// /api/advanced-search?tags=in:new,featured&name=regex:laptop
```
