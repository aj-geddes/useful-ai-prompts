---
name: api-filtering-sorting
description: Implement advanced filtering and sorting capabilities for APIs with query parsing, field validation, and optimization. Use when building search features, complex queries, or flexible data retrieval endpoints.
---

# API Filtering & Sorting

## Overview

Build flexible filtering and sorting systems that handle complex queries efficiently with proper validation, security, and performance optimization.

## When to Use

- Building search and filter interfaces
- Implementing advanced query capabilities
- Creating flexible data retrieval endpoints
- Optimizing query performance
- Validating user input for queries
- Supporting complex filtering logic

## Instructions

### 1. **Query Parameter Filtering**

```javascript
// Node.js filtering implementation
app.get('/api/products', async (req, res) => {
  const filters = {};
  const sortOptions = {};

  // Parse filtering parameters
  const allowedFilters = ['category', 'minPrice', 'maxPrice', 'inStock', 'rating'];
  for (const key of allowedFilters) {
    if (req.query[key]) {
      filters[key] = req.query[key];
    }
  }

  // Build MongoDB query
  const mongoQuery = {};

  if (filters.category) {
    mongoQuery.category = filters.category;
  }

  if (filters.minPrice || filters.maxPrice) {
    mongoQuery.price = {};
    if (filters.minPrice) {
      mongoQuery.price.$gte = parseFloat(filters.minPrice);
    }
    if (filters.maxPrice) {
      mongoQuery.price.$lte = parseFloat(filters.maxPrice);
    }
  }

  if (filters.inStock !== undefined) {
    mongoQuery.stock = { $gt: filters.inStock === 'true' ? 0 : -1 };
  }

  if (filters.rating) {
    mongoQuery.rating = { $gte: parseFloat(filters.rating) };
  }

  // Parse sorting
  const sortField = req.query.sort || 'createdAt';
  const sortOrder = req.query.order === 'asc' ? 1 : -1;

  const validSortFields = ['price', 'rating', 'createdAt', 'popularity'];
  if (!validSortFields.includes(sortField)) {
    return res.status(400).json({ error: 'Invalid sort field' });
  }

  const page = parseInt(req.query.page) || 1;
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const offset = (page - 1) * limit;

  try {
    const [products, total] = await Promise.all([
      Product.find(mongoQuery)
        .sort({ [sortField]: sortOrder })
        .skip(offset)
        .limit(limit),
      Product.countDocuments(mongoQuery)
    ]);

    res.json({
      data: products,
      filters: {
        applied: filters,
        available: {
          categories: await getAvailableCategories(),
          priceRange: await getPriceRange(),
          ratings: [1, 2, 3, 4, 5]
        }
      },
      pagination: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit)
      }
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

### 2. **Advanced Filter Parser**

```javascript
// Parse complex filter queries
class FilterParser {
  static parse(queryString) {
    const filters = {};
    const params = new URLSearchParams(queryString);

    params.forEach((value, key) => {
      // Handle nested filters (e.g., user.email, address.city)
      if (key.includes('.')) {
        this.setNested(filters, key, value);
      } else {
        filters[key] = this.parseValue(value);
      }
    });

    return filters;
  }

  static setNested(obj, path, value) {
    const keys = path.split('.');
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
    if (typeof value !== 'string') return value;

    const operatorMatch = value.match(/^(eq|ne|gt|gte|lt|lte|in|nin|exists|regex):(.+)$/);
    if (operatorMatch) {
      const [, operator, operandValue] = operatorMatch;

      const operators = {
        eq: { $eq: operandValue },
        ne: { $ne: operandValue },
        gt: { $gt: parseFloat(operandValue) },
        gte: { $gte: parseFloat(operandValue) },
        lt: { $lt: parseFloat(operandValue) },
        lte: { $lte: parseFloat(operandValue) },
        in: { $in: operandValue.split(',') },
        nin: { $nin: operandValue.split(',') },
        exists: { $exists: operandValue === 'true' },
        regex: { $regex: operandValue, $options: 'i' }
      };

      return operators[operator];
    }

    // Parse booleans
    if (value === 'true') return true;
    if (value === 'false') return false;

    // Parse numbers
    if (!isNaN(value)) return parseFloat(value);

    return value;
  }
}

// Usage
app.get('/api/advanced-search', async (req, res) => {
  const filters = FilterParser.parse(req.url.split('?')[1]);

  const products = await Product.find(filters);
  res.json({ data: products });
});

// Example queries:
// /api/advanced-search?price=gte:100&price=lt:500&category=electronics
// /api/advanced-search?rating=gte:4&inStock=exists:true
// /api/advanced-search?tags=in:new,featured&name=regex:laptop
```

### 3. **Filter Builder Pattern**

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
      '=': '$eq',
      '!=': '$ne',
      '>': '$gt',
      '>=': '$gte',
      '<': '$lt',
      '<=': '$lte',
      'in': '$in',
      'regex': '$regex'
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
    this.query.$or = fields.map(field => ({
      [field]: { $regex: text, $options: 'i' }
    }));
    return this;
  }

  sort(field, direction = 'asc') {
    this.sortBy[field] = direction === 'asc' ? 1 : -1;
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
      this.model.find(this.query)
        .sort(this.sortBy)
        .skip(offset)
        .limit(this.pageSize),
      this.model.countDocuments(this.query)
    ]);

    return {
      data,
      pagination: {
        page: this.pageNum,
        limit: this.pageSize,
        total,
        totalPages: Math.ceil(total / this.pageSize)
      }
    };
  }
}

// Usage
const results = await new QueryBuilder(Product)
  .filter('category', '=', 'electronics')
  .range('price', 100, 500)
  .filter('inStock', '=', true)
  .sort('price', 'asc')
  .pagination(1, 20)
  .execute();
```

### 4. **Python Filtering (SQLAlchemy)**

```python
from sqlalchemy import and_, or_, func
from sqlalchemy.orm import Query

class FilterSpecification:
    def __init__(self, field, operator, value):
        self.field = field
        self.operator = operator
        self.value = value

    def to_sql(self, model):
        column = getattr(model, self.field)
        operators = {
            'eq': lambda c, v: c == v,
            'ne': lambda c, v: c != v,
            'gt': lambda c, v: c > v,
            'gte': lambda c, v: c >= v,
            'lt': lambda c, v: c < v,
            'lte': lambda c, v: c <= v,
            'in': lambda c, v: c.in_(v),
            'like': lambda c, v: c.ilike(f'%{v}%'),
            'between': lambda c, v: c.between(v[0], v[1])
        }

        operation = operators.get(self.operator)
        if not operation:
            raise ValueError(f'Invalid operator: {self.operator}')

        return operation(column, self.value)

@app.route('/api/products', methods=['GET'])
def list_products():
    category = request.args.get('category')
    min_price = request.args.get('minPrice', type=float)
    max_price = request.args.get('maxPrice', type=float)
    sort_by = request.args.get('sort', 'created_at')
    sort_order = request.args.get('order', 'desc')
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('limit', 20, type=int), 100)

    query = Product.query

    # Apply filters
    if category:
        query = query.filter(Product.category == category)

    if min_price:
        query = query.filter(Product.price >= min_price)

    if max_price:
        query = query.filter(Product.price <= max_price)

    # Apply sorting
    sort_field = getattr(Product, sort_by, Product.created_at)
    if sort_order == 'asc':
        query = query.order_by(sort_field.asc())
    else:
        query = query.order_by(sort_field.desc())

    # Paginate
    pagination = query.paginate(page=page, per_page=per_page)

    return jsonify({
        'data': [p.to_dict() for p in pagination.items],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': pagination.total,
            'pages': pagination.pages
        }
    }), 200
```

### 5. **Elasticsearch Filtering**

```javascript
async function searchWithFilters(searchQuery, filters, sort, page = 1, limit = 20) {
  const from = (page - 1) * limit;

  const must = [];
  const should = [];

  // Full-text search
  if (searchQuery) {
    must.push({
      multi_match: {
        query: searchQuery,
        fields: ['name^2', 'description', 'category']
      }
    });
  }

  // Apply filters
  if (filters.category) {
    must.push({ term: { 'category.keyword': filters.category } });
  }

  if (filters.minPrice || filters.maxPrice) {
    const range = {};
    if (filters.minPrice) range.gte = filters.minPrice;
    if (filters.maxPrice) range.lte = filters.maxPrice;
    must.push({ range: { price: range } });
  }

  if (filters.tags) {
    should.push({
      terms: { 'tags.keyword': filters.tags }
    });
  }

  const response = await esClient.search({
    index: 'products',
    body: {
      from,
      size: limit,
      query: {
        bool: {
          must,
          ...(should.length && { should, minimum_should_match: 1 })
        }
      },
      sort: sort ? [sort] : ['_score', { createdAt: 'desc' }],
      aggs: {
        categories: {
          terms: { field: 'category.keyword', size: 50 }
        },
        priceRange: {
          stats: { field: 'price' }
        }
      }
    }
  });

  return {
    results: response.hits.hits.map(hit => hit._source),
    total: response.hits.total.value,
    facets: {
      categories: response.aggregations.categories.buckets,
      priceRange: response.aggregations.priceRange
    }
  };
}
```

### 6. **Query Validation**

```javascript
// Prevent injection and invalid queries
const validateFilter = (field, value) => {
  const allowedFields = ['category', 'price', 'rating', 'inStock'];

  if (!allowedFields.includes(field)) {
    throw new Error(`Field ${field} is not filterable`);
  }

  // Validate field-specific values
  const validations = {
    category: (v) => typeof v === 'string' && v.length <= 50,
    price: (v) => !isNaN(v) && v >= 0,
    rating: (v) => !isNaN(v) && v >= 0 && v <= 5,
    inStock: (v) => v === 'true' || v === 'false'
  };

  if (!validations[field](value)) {
    throw new Error(`Invalid value for ${field}`);
  }

  return true;
};
```

## Best Practices

### ✅ DO
- Whitelist allowed filter fields
- Validate all input parameters
- Index fields used for filtering
- Support common operators
- Provide faceted navigation
- Cache filter options
- Limit filter complexity
- Document filter syntax
- Use database-native operators
- Optimize queries with indexes

### ❌ DON'T
- Allow arbitrary field filtering
- Support unlimited operators
- Ignore SQL injection risks
- Create complex filter logic
- Expose internal field names
- Filter on unindexed fields
- Allow deeply nested filters
- Skip input validation
- Combine all filters with OR
- Ignore performance impact

## Performance Optimization

- Create composite indexes for common filters
- Use query hints in databases
- Cache frequent filter combinations
- Limit aggregation complexity
- Monitor query performance
- Use database statistics
- Consider denormalization
- Implement query result caching
