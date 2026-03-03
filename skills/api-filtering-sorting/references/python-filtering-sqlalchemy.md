# Python Filtering (SQLAlchemy)

## Python Filtering (SQLAlchemy)

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
