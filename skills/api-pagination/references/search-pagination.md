# Search Pagination

## Search Pagination

```javascript
// Full-text search with pagination
app.get("/api/search", async (req, res) => {
  const query = req.query.q;
  const page = parseInt(req.query.page) || 1;
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const offset = (page - 1) * limit;

  if (!query) {
    return res.status(400).json({ error: "Search query required" });
  }

  try {
    // MongoDB text search example
    const [results, total] = await Promise.all([
      Product.find(
        { $text: { $search: query } },
        { score: { $meta: "textScore" } },
      )
        .sort({ score: { $meta: "textScore" } })
        .skip(offset)
        .limit(limit),
      Product.countDocuments({ $text: { $search: query } }),
    ]);

    const totalPages = Math.ceil(total / limit);

    res.json({
      query,
      results,
      pagination: {
        page,
        limit,
        total,
        totalPages,
      },
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Elasticsearch pagination
async function searchElasticsearch(query, page = 1, limit = 20) {
  const from = (page - 1) * limit;

  const response = await esClient.search({
    index: "products",
    body: {
      from,
      size: limit,
      query: {
        multi_match: {
          query,
          fields: ["name^2", "description", "category"],
        },
      },
    },
  });

  return {
    results: response.hits.hits.map((hit) => hit._source),
    pagination: {
      page,
      limit,
      total: response.hits.total.value,
      totalPages: Math.ceil(response.hits.total.value / limit),
    },
  };
}
```
