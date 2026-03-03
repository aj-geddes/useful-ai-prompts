# Date Format

## Date Format

**v1:** ISO 8601 strings
**v2:** Unix timestamps

**Migration:**

```javascript
// Before
const created = new Date(user.created);

// After
const created = new Date(user.created * 1000);
```


## Error Format

**v1:**

```json
{ "error": "User not found" }
```

**v2:**

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User not found",
    "details": {}
  }
}
```
