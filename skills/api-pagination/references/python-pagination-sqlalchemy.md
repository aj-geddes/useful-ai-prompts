# Python Pagination (SQLAlchemy)

## Python Pagination (SQLAlchemy)

```python
from flask import request, jsonify
from flask_sqlalchemy import Pagination

@app.route('/api/users', methods=['GET'])
def list_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 100)

    pagination: Pagination = User.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        'data': [user.to_dict() for user in pagination.items],
        'pagination': {
            'page': pagination.page,
            'per_page': pagination.per_page,
            'total': pagination.total,
            'pages': pagination.pages,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev
        }
    }), 200

# Cursor pagination with graphene
class UserNode(relay.Node):
    class Meta:
        model = User

    @classmethod
    def get_node(cls, info, id):
        return User.query.get(id)

class Query(graphene.ObjectType):
    users = relay.ConnectionField(UserNode)

    def resolve_users(self, info, **kwargs):
        return User.query.all()
```
