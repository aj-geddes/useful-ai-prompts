# Elasticsearch Filtering

## Elasticsearch Filtering

```javascript
async function searchWithFilters(
  searchQuery,
  filters,
  sort,
  page = 1,
  limit = 20,
) {
  const from = (page - 1) * limit;

  const must = [];
  const should = [];

  // Full-text search
  if (searchQuery) {
    must.push({
      multi_match: {
        query: searchQuery,
        fields: ["name^2", "description", "category"],
      },
    });
  }

  // Apply filters
  if (filters.category) {
    must.push({ term: { "category.keyword": filters.category } });
  }

  if (filters.minPrice || filters.maxPrice) {
    const range = {};
    if (filters.minPrice) range.gte = filters.minPrice;
    if (filters.maxPrice) range.lte = filters.maxPrice;
    must.push({ range: { price: range } });
  }

  if (filters.tags) {
    should.push({
      terms: { "tags.keyword": filters.tags },
    });
  }

  const response = await esClient.search({
    index: "products",
    body: {
      from,
      size: limit,
      query: {
        bool: {
          must,
          ...(should.length && { should, minimum_should_match: 1 }),
        },
      },
      sort: sort ? [sort] : ["_score", { createdAt: "desc" }],
      aggs: {
        categories: {
          terms: { field: "category.keyword", size: 50 },
        },
        priceRange: {
          stats: { field: "price" },
        },
      },
    },
  });

  return {
    results: response.hits.hits.map((hit) => hit._source),
    total: response.hits.total.value,
    facets: {
      categories: response.aggregations.categories.buckets,
      priceRange: response.aggregations.priceRange,
    },
  };
}
```
