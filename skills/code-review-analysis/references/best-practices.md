# Best Practices

## Best Practices

### Error Handling

```typescript
// ❌ Silent failures
try {
  await saveData(data);
} catch (e) {
  // empty catch
}

// ✅ Proper error handling
try {
  await saveData(data);
} catch (error) {
  logger.error("Failed to save data", { error, data });
  throw new DataSaveError("Could not save data", { cause: error });
}
```

### Resource Management

```python
# ❌ Resources not closed
file = open('data.txt')
data = file.read()
process(data)

# ✅ Proper cleanup
with open('data.txt') as file:
    data = file.read()
    process(data)
```
