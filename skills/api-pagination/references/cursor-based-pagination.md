# Cursor-Based Pagination

## Cursor-Based Pagination

```javascript
// Cursor-based pagination for better performance
class CursorPagination {
  static encode(value) {
    return Buffer.from(String(value)).toString("base64");
  }

  static decode(cursor) {
    return Buffer.from(cursor, "base64").toString("utf-8");
  }

  static generateCursor(resource) {
    return this.encode(`${resource.id}:${resource.createdAt.getTime()}`);
  }

  static parseCursor(cursor) {
    if (!cursor) return null;
    const decoded = this.decode(cursor);
    const [id, timestamp] = decoded.split(":");
    return { id, timestamp: parseInt(timestamp) };
  }
}

app.get("/api/users/cursor", async (req, res) => {
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const after = req.query.after
    ? CursorPagination.parseCursor(req.query.after)
    : null;

  try {
    const query = {};
    if (after) {
      query.createdAt = { $lt: new Date(after.timestamp) };
    }

    const users = await User.find(query)
      .sort({ createdAt: -1, _id: -1 })
      .limit(limit + 1)
      .select("id email firstName lastName createdAt");

    const hasMore = users.length > limit;
    const data = hasMore ? users.slice(0, limit) : users;
    const nextCursor = hasMore
      ? CursorPagination.generateCursor(data[data.length - 1])
      : null;

    res.json({
      data,
      pageInfo: {
        hasNextPage: hasMore,
        endCursor: nextCursor,
        totalCount: await User.countDocuments(),
      },
      links: {
        self: `/api/users/cursor?limit=${limit}`,
        next: nextCursor
          ? `/api/users/cursor?limit=${limit}&after=${nextCursor}`
          : null,
      },
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```
