# Search & Discovery

## Search & Discovery

```javascript
// Enable multiple ways to find content

class DiscoverabilityStrategy {
  designSearchFunctionality() {
    return {
      search_box: {
        location: "Header, prominent placement",
        placeholder: "Clear example text",
        autocomplete: true,
        filters: ["Category", "Price", "Rating"],
      },
      search_results: {
        ranking: "Relevance + popularity + freshness",
        facets: "Allow filtering results",
        snippets: "Show preview and highlights",
      },
      zero_results: {
        suggestions: "Show did you mean, popular searches",
        related: "Show related categories",
      },
    };
  }

  designBrowsing() {
    return {
      category_pages: {
        structure: "Subcategories + featured items",
        sorting: "By popularity, newest, price",
        pagination: "Load more or paginate",
      },
      related_items: {
        placement: "Product page, cart page",
        logic: "Similar category, trending, recommended",
      },
    };
  }
}
```
