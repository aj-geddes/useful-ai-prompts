# Query Validation

## Query Validation

```javascript
// Prevent injection and invalid queries
const validateFilter = (field, value) => {
  const allowedFields = ["category", "price", "rating", "inStock"];

  if (!allowedFields.includes(field)) {
    throw new Error(`Field ${field} is not filterable`);
  }

  // Validate field-specific values
  const validations = {
    category: (v) => typeof v === "string" && v.length <= 50,
    price: (v) => !isNaN(v) && v >= 0,
    rating: (v) => !isNaN(v) && v >= 0 && v <= 5,
    inStock: (v) => v === "true" || v === "false",
  };

  if (!validations[field](value)) {
    throw new Error(`Invalid value for ${field}`);
  }

  return true;
};
```
