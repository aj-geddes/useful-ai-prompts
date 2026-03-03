# Database Queries and Optimization

## Database Queries and Optimization

```python
# products/queries.py
from django.db.models import Q, Count, Avg, F, Case, When, Value
from django.db.models.functions import Coalesce
from .models import Product, ProductReview

# Optimized queries with select_related and prefetch_related
def get_product_details(product_id):
    return Product.objects.select_related('owner').prefetch_related(
        'reviews__author'
    ).get(id=product_id)

# Aggregation queries
def get_top_products():
    return Product.objects.annotate(
        review_count=Count('reviews'),
        avg_rating=Avg('reviews__rating'),
        total_reviews=Count('reviews', distinct=True)
    ).filter(review_count__gt=0).order_by('-avg_rating')[:10]

# Complex filtering
def search_products(query, category=None, min_price=None, max_price=None):
    queryset = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )

    if category:
        queryset = queryset.filter(category=category)
    if min_price:
        queryset = queryset.filter(price__gte=min_price)
    if max_price:
        queryset = queryset.filter(price__lte=max_price)

    return queryset.select_related('owner')

# Bulk operations
def bulk_update_stock(updates):
    products_to_update = []
    for product_id, new_stock in updates.items():
        product = Product.objects.get(id=product_id)
        product.stock = new_stock
        products_to_update.append(product)

    Product.objects.bulk_update(products_to_update, ['stock'])
```
