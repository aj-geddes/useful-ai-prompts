# Keyset Pagination

## Keyset Pagination

```javascript
// Keyset pagination (most efficient for large datasets)
app.get("/api/products/keyset", async (req, res) => {
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const lastId = req.query.lastId;
  const sortBy = req.query.sort || "price"; // price or createdAt

  try {
    const query = {};

    // Build query based on sort field
    if (lastId) {
      const lastProduct = await Product.findById(lastId);

      if (sortBy === "price") {
        query.$or = [
          { price: { $lt: lastProduct.price } },
          { price: lastProduct.price, _id: { $lt: lastId } },
        ];
      } else {
        query.$or = [
          { createdAt: { $lt: lastProduct.createdAt } },
          { createdAt: lastProduct.createdAt, _id: { $lt: lastId } },
        ];
      }
    }

    const products = await Product.find(query)
      .sort({ [sortBy]: -1, _id: -1 })
      .limit(limit + 1);

    const hasMore = products.length > limit;
    const data = hasMore ? products.slice(0, limit) : products;

    res.json({
      data,
      pageInfo: {
        hasMore,
        lastId: data.length > 0 ? data[data.length - 1]._id : null,
      },
      links: {
        next:
          hasMore && data.length > 0
            ? `/api/products/keyset?lastId=${data[data.length - 1]._id}&sort=${sortBy}&limit=${limit}`
            : null,
      },
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```
