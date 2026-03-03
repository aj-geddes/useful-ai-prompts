# Performance Review

## Performance Review

```javascript
// ❌ N+1 query problem
const users = await User.findAll();
for (const user of users) {
  user.orders = await Order.findAll({ where: { userId: user.id } });
}

// ✅ Eager loading
const users = await User.findAll({
  include: [{ model: Order }],
});
```

```python
# ❌ Inefficient list operations
result = []
for item in large_list:
    if item % 2 == 0:
        result.append(item * 2)

# ✅ List comprehension
result = [item * 2 for item in large_list if item % 2 == 0]
```
