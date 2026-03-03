# Event-Based Invalidation

## Event-Based Invalidation

**PostgreSQL with Triggers:**

```sql
-- Create function to invalidate cache on write
CREATE OR REPLACE FUNCTION invalidate_user_cache()
RETURNS TRIGGER AS $$
BEGIN
  -- In production, this would publish to Redis/Memcached
  -- PERFORM redis_publish('cache_invalidation', json_build_object(
  --   'event', 'user_updated',
  --   'user_id', NEW.id
  -- ));
  RAISE LOG 'Invalidating cache for user %', NEW.id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach to users table
CREATE TRIGGER invalidate_cache_on_user_update
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION invalidate_user_cache();

-- When users are updated, trigger fires and invalidates cache
UPDATE users SET email = 'newemail@example.com' WHERE id = 123;
```

**Application-Level Invalidation:**

```javascript
// Invalidate cache on data modification
async function updateUser(userId, userData) {
  // Update database
  const updatedUser = await db.query(
    "UPDATE users SET name = $1, email = $2 WHERE id = $3 RETURNING *",
    [userData.name, userData.email, userId],
  );

  // Invalidate related caches
  const cacheKeys = [
    `user:${userId}`,
    `user:${userId}:profile`,
    `user:${userId}:orders`,
    "active_users_list",
  ];

  for (const key of cacheKeys) {
    await client.del(key);
  }

  return updatedUser;
}
```
