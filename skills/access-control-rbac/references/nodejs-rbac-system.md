# Node.js RBAC System

## Node.js RBAC System

```javascript
// rbac-system.js
class Permission {
  constructor(resource, action) {
    this.resource = resource;
    this.action = action;
  }

  toString() {
    return `${this.resource}:${this.action}`;
  }
}

class Role {
  constructor(name, description) {
    this.name = name;
    this.description = description;
    this.permissions = new Set();
    this.inherits = new Set();
  }

  addPermission(permission) {
    this.permissions.add(permission.toString());
  }

  removePermission(permission) {
    this.permissions.delete(permission.toString());
  }

  inheritFrom(role) {
    this.inherits.add(role.name);
  }

  hasPermission(permission, rbac) {
    // Check direct permissions
    if (this.permissions.has(permission.toString())) {
      return true;
    }

    // Check inherited permissions
    for (const parentRoleName of this.inherits) {
      const parentRole = rbac.getRole(parentRoleName);
      if (parentRole && parentRole.hasPermission(permission, rbac)) {
        return true;
      }
    }

    return false;
  }
}

class RBACSystem {
  constructor() {
    this.roles = new Map();
    this.userRoles = new Map();
    this.initializeDefaultRoles();
  }

  initializeDefaultRoles() {
    // Admin role - full access
    const admin = new Role("admin", "Administrator with full access");
    admin.addPermission(new Permission("*", "*"));
    this.createRole(admin);

    // Editor role
    const editor = new Role("editor", "Can create and edit content");
    editor.addPermission(new Permission("posts", "create"));
    editor.addPermission(new Permission("posts", "read"));
    editor.addPermission(new Permission("posts", "update"));
    editor.addPermission(new Permission("comments", "read"));
    editor.addPermission(new Permission("comments", "moderate"));
    this.createRole(editor);

    // Viewer role
    const viewer = new Role("viewer", "Read-only access");
    viewer.addPermission(new Permission("posts", "read"));
    viewer.addPermission(new Permission("comments", "read"));
    this.createRole(viewer);

    // User role (inherits from viewer)
    const user = new Role("user", "Authenticated user");
    user.inheritFrom(viewer);
    user.addPermission(new Permission("posts", "create"));
    user.addPermission(new Permission("comments", "create"));
    user.addPermission(new Permission("profile", "update"));
    this.createRole(user);
  }

  createRole(role) {
    this.roles.set(role.name, role);
  }

  getRole(roleName) {
    return this.roles.get(roleName);
  }

  assignRole(userId, roleName) {
    if (!this.roles.has(roleName)) {
      throw new Error(`Role ${roleName} does not exist`);
    }

    if (!this.userRoles.has(userId)) {
      this.userRoles.set(userId, new Set());
    }

    this.userRoles.get(userId).add(roleName);
  }

  revokeRole(userId, roleName) {
    const roles = this.userRoles.get(userId);
    if (roles) {
      roles.delete(roleName);
    }
  }

  getUserRoles(userId) {
    return Array.from(this.userRoles.get(userId) || []);
  }

  can(userId, resource, action) {
    const permission = new Permission(resource, action);
    const userRoles = this.userRoles.get(userId);

    if (!userRoles) {
      return false;
    }

    // Check if user has admin role (wildcard permissions)
    if (userRoles.has("admin")) {
      return true;
    }

    // Check all user roles
    for (const roleName of userRoles) {
      const role = this.roles.get(roleName);
      if (role && role.hasPermission(permission, this)) {
        return true;
      }
    }

    return false;
  }

  // Express middleware
  authorize(resource, action) {
    return (req, res, next) => {
      const userId = req.user?.id;

      if (!userId) {
        return res.status(401).json({
          error: "unauthorized",
          message: "Authentication required",
        });
      }

      if (!this.can(userId, resource, action)) {
        return res.status(403).json({
          error: "forbidden",
          message: `Permission denied: ${resource}:${action}`,
        });
      }

      next();
    };
  }
}

// Usage
const rbac = new RBACSystem();

// Assign roles to users
rbac.assignRole("user-123", "editor");
rbac.assignRole("user-456", "viewer");
rbac.assignRole("user-789", "admin");

// Check permissions
console.log(rbac.can("user-123", "posts", "update")); // true
console.log(rbac.can("user-456", "posts", "update")); // false
console.log(rbac.can("user-789", "anything", "anything")); // true

// Express route protection
const express = require("express");
const app = express();

app.post("/api/posts", rbac.authorize("posts", "create"), (req, res) => {
  res.json({ message: "Post created" });
});

module.exports = RBACSystem;
```
