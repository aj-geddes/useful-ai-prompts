---
name: sql-injection-prevention
description: >
  Prevent SQL injection attacks using prepared statements, parameterized
  queries, and input validation. Use when building database-driven applications
  securely.
---

# SQL Injection Prevention

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive SQL injection prevention using prepared statements, parameterized queries, ORM best practices, and input validation.

## When to Use

- Database query development
- Legacy code security review
- Security audit remediation
- API endpoint development
- User input handling
- Dynamic query generation

## Quick Start

Minimal working example:

```javascript
// secure-db.js
const { Pool } = require("pg");

class SecureDatabase {
  constructor() {
    this.pool = new Pool({
      host: process.env.DB_HOST,
      database: process.env.DB_NAME,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,
    });
  }

  /**
   * ✅ SECURE: Parameterized query
   */
  async getUserById(userId) {
    const query = "SELECT * FROM users WHERE id = $1";
    const values = [userId];

    try {
      const result = await this.pool.query(query, values);
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js with PostgreSQL](references/nodejs-with-postgresql.md) | Node.js with PostgreSQL |
| [Python with SQLAlchemy ORM](references/python-with-sqlalchemy-orm.md) | Python with SQLAlchemy ORM |
| [Java JDBC with Prepared Statements](references/java-jdbc-with-prepared-statements.md) | Java JDBC with Prepared Statements |
| [Input Validation & Sanitization](references/input-validation-sanitization.md) | Input Validation & Sanitization |

## Best Practices

### ✅ DO

- Use prepared statements ALWAYS
- Use ORM frameworks properly
- Validate all user inputs
- Whitelist dynamic values
- Use least privilege DB accounts
- Enable query logging
- Regular security audits
- Use parameterized queries

### ❌ DON'T

- Concatenate user input
- Trust client-side validation
- Use string formatting for queries
- Allow dynamic table/column names
- Grant excessive DB permissions
- Skip input validation
