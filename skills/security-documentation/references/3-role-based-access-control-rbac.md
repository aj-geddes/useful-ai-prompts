# 3 Role-Based Access Control (RBAC)

## 3 Role-Based Access Control (RBAC)

**Principle of Least Privilege:** Users receive minimum access needed for their role.

**Roles:**

| Role      | Permissions             | Access Level           |
| --------- | ----------------------- | ---------------------- |
| Admin     | Full system access      | Read/Write/Delete All  |
| Developer | Code, staging env       | Read/Write Dev/Staging |
| Support   | Customer data (limited) | Read customer data     |
| Auditor   | Logs, audit trails      | Read-only all          |
| User      | Own data only           | Read/Write own data    |

**Implementation:**

```javascript
// Permission middleware
const requirePermission = (permission) => {
  return async (req, res, next) => {
    const user = req.user;
    const userPermissions = await getUserPermissions(user.role);

    if (!userPermissions.includes(permission)) {
      await logSecurityEvent("unauthorized_access", user.id, {
        permission,
        endpoint: req.path,
      });

      return res.status(403).json({
        error: "Insufficient permissions",
        required: permission,
      });
    }

    next();
  };
};

// Usage
app.delete("/api/users/:id", requirePermission("users:delete"), deleteUser);
```

---
