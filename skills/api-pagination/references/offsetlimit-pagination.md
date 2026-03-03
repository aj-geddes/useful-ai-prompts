# Offset/Limit Pagination

## Offset/Limit Pagination

```javascript
// Node.js offset/limit implementation
app.get('/api/users', async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = Math.min(parseInt(req.query.limit) || 20, 100); // Max 100
  const offset = (page - 1) * limit;

  try {
    const [users, total] = await Promise.all([
      User.find()
        .skip(offset)
        .limit(limit)
        .select('id email firstName lastName createdAt'),
      User.countDocuments()
    ]);

    const totalPages = Math.ceil(total / limit);

    res.json({
      data: users,
      pagination: {
        page,
        limit,
        total,
        totalPages,
        hasNext: page < totalPages,
        hasPrev: page > 1
      },
      links: {
        self: `/api/users?page=${page}&limit=${limit}`,
        first: `/api/users?page=1&limit=${limit}`,
        last: `/api/users?page=${totalPages}&limit=${limit}`,
        ...(page > 1 && { prev: `/api/users?page=${page - 1}&limit=${limit}` }),
        ...(page < totalPages && { next: `/api/users?page=${page + 1}&limit=${limit}` })
      }
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Python offset/limit
from flask import request
from sqlalchemy import func

@app.route('/api/users', methods=['GET'])
def list_users():
    page = request.args.get('page', 1, type=int)
    limit = min(request.args.get('limit', 20, type=int), 100)
    offset = (page - 1) * limit

    total = db.session.query(func.count(User.id)).scalar()
    users = db.session.query(User).offset(offset).limit(limit).all()

    total_pages = (total + limit - 1) // limit

    return jsonify({
        'data': [u.to_dict() for u in users],
        'pagination': {
            'page': page,
            'limit': limit,
            'total': total,
            'totalPages': total_pages,
            'hasNext': page < total_pages,
            'hasPrev': page > 1
        }
    }), 200
```
