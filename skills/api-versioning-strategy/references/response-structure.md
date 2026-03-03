# Response Structure

## Response Structure

**v1:**

```json
{
  "users": [...],
  "total": 10,
  "page": 1
}
```
````

**v2:**

```json
{
  "data": [...],
  "meta": {
    "total": 10,
    "page": 1,
    "perPage": 20
  }
}
```

**Migration:**

```javascript
// Before
const users = response.users;
const total = response.total;

// After
const users = response.data;
const total = response.meta.total;
```
