# Modernize Patterns

## Modernize Patterns

Replace outdated patterns with modern equivalents:

### Promises over Callbacks

```javascript
// BEFORE: Callback hell
function fetchUserData(userId, callback) {
  db.query("SELECT * FROM users WHERE id = ?", [userId], (err, user) => {
    if (err) return callback(err);
    db.query(
      "SELECT * FROM orders WHERE user_id = ?",
      [userId],
      (err, orders) => {
        if (err) return callback(err);
        callback(null, { user, orders });
      },
    );
  });
}

// AFTER: Async/await
async function fetchUserData(userId) {
  const user = await db.query("SELECT * FROM users WHERE id = ?", [userId]);
  const orders = await db.query("SELECT * FROM orders WHERE user_id = ?", [
    userId,
  ]);
  return { user, orders };
}
```

### Modern Language Features

```javascript
// BEFORE: var and string concatenation
var userName = user.firstName + " " + user.lastName;
var isActive = user.status === "active" ? true : false;

// AFTER: const/let and template literals
const userName = `${user.firstName} ${user.lastName}`;
const isActive = user.status === "active";
```
