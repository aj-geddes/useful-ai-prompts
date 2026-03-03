# Query Parameter Filtering

## Query Parameter Filtering

```javascript
// Node.js filtering implementation
app.get("/api/products", async (req, res) => {
  const filters = {};
  const sortOptions = {};

  // Parse filtering parameters
  const allowedFilters = [
    "category",
    "minPrice",
    "maxPrice",
    "inStock",
    "rating",
  ];
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
    mongoQuery.stock = { $gt: filters.inStock === "true" ? 0 : -1 };
  }

  if (filters.rating) {
    mongoQuery.rating = { $gte: parseFloat(filters.rating) };
  }

  // Parse sorting
  const sortField = req.query.sort || "createdAt";
  const sortOrder = req.query.order === "asc" ? 1 : -1;

  const validSortFields = ["price", "rating", "createdAt", "popularity"];
  if (!validSortFields.includes(sortField)) {
    return res.status(400).json({ error: "Invalid sort field" });
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
      Product.countDocuments(mongoQuery),
    ]);

    res.json({
      data: products,
      filters: {
        applied: filters,
        available: {
          categories: await getAvailableCategories(),
          priceRange: await getPriceRange(),
          ratings: [1, 2, 3, 4, 5],
        },
      },
      pagination: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit),
      },
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```
