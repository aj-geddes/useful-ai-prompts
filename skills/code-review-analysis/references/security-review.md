# Security Review

## Security Review

### Common Vulnerabilities

**SQL Injection**

```python
# ❌ Vulnerable to SQL injection
query = f"SELECT * FROM users WHERE email = '{user_email}'"

# ✅ Parameterized query
query = "SELECT * FROM users WHERE email = ?"
cursor.execute(query, (user_email,))
```

**XSS Prevention**

```javascript
// ❌ XSS vulnerable
element.innerHTML = userInput;

// ✅ Safe rendering
element.textContent = userInput;
// or use framework escaping: {{ userInput }} in templates
```

**Authentication & Authorization**

```typescript
// ❌ Missing authorization check
app.delete("/api/users/:id", async (req, res) => {
  await deleteUser(req.params.id);
  res.json({ success: true });
});

// ✅ Proper authorization
app.delete("/api/users/:id", requireAuth, async (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: "Forbidden" });
  }
  await deleteUser(req.params.id);
  res.json({ success: true });
});
```
