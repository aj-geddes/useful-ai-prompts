---
name: sql-injection-prevention
description: Prevent SQL injection attacks using prepared statements, parameterized queries, and input validation. Use when building database-driven applications securely.
---

# SQL Injection Prevention

## Overview

Implement comprehensive SQL injection prevention using prepared statements, parameterized queries, ORM best practices, and input validation.

## When to Use

- Database query development
- Legacy code security review
- Security audit remediation
- API endpoint development
- User input handling
- Dynamic query generation

## Implementation Examples

### 1. **Node.js with PostgreSQL**

```javascript
// secure-db.js
const { Pool } = require('pg');

class SecureDatabase {
  constructor() {
    this.pool = new Pool({
      host: process.env.DB_HOST,
      database: process.env.DB_NAME,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000
    });
  }

  /**
   * ✅ SECURE: Parameterized query
   */
  async getUserById(userId) {
    const query = 'SELECT * FROM users WHERE id = $1';
    const values = [userId];

    try {
      const result = await this.pool.query(query, values);
      return result.rows[0];
    } catch (error) {
      console.error('Query error:', error);
      throw error;
    }
  }

  /**
   * ✅ SECURE: Multiple parameters
   */
  async searchUsers(email, status) {
    const query = `
      SELECT id, email, name, created_at
      FROM users
      WHERE email LIKE $1 AND status = $2
      LIMIT 100
    `;
    const values = [`%${email}%`, status];

    const result = await this.pool.query(query, values);
    return result.rows;
  }

  /**
   * ✅ SECURE: Dynamic column ordering with whitelist
   */
  async getUsers(sortBy = 'created_at', order = 'DESC') {
    // Whitelist allowed columns
    const allowedColumns = ['id', 'email', 'name', 'created_at'];
    const allowedOrders = ['ASC', 'DESC'];

    if (!allowedColumns.includes(sortBy)) {
      sortBy = 'created_at';
    }

    if (!allowedOrders.includes(order.toUpperCase())) {
      order = 'DESC';
    }

    // Safe to use in query since values are whitelisted
    const query = `
      SELECT id, email, name, created_at
      FROM users
      ORDER BY ${sortBy} ${order}
      LIMIT 100
    `;

    const result = await this.pool.query(query);
    return result.rows;
  }

  /**
   * ✅ SECURE: Batch insert with prepared statement
   */
  async insertUsers(users) {
    const query = `
      INSERT INTO users (email, name, password_hash)
      VALUES ($1, $2, $3)
      RETURNING id
    `;

    const results = [];

    for (const user of users) {
      const values = [user.email, user.name, user.passwordHash];
      const result = await this.pool.query(query, values);
      results.push(result.rows[0].id);
    }

    return results;
  }

  /**
   * ✅ SECURE: Transaction with prepared statements
   */
  async transferFunds(fromAccount, toAccount, amount) {
    const client = await this.pool.connect();

    try {
      await client.query('BEGIN');

      // Debit from account
      await client.query(
        'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
        [amount, fromAccount]
      );

      // Credit to account
      await client.query(
        'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
        [amount, toAccount]
      );

      // Record transaction
      await client.query(
        'INSERT INTO transactions (from_account, to_account, amount) VALUES ($1, $2, $3)',
        [fromAccount, toAccount, amount]
      );

      await client.query('COMMIT');
      return true;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }

  /**
   * ❌ VULNERABLE: String concatenation (DON'T USE)
   */
  async vulnerableQuery(userId) {
    // VULNERABLE TO SQL INJECTION!
    const query = `SELECT * FROM users WHERE id = '${userId}'`;
    // Attack: userId = "1' OR '1'='1"
    // Result: SELECT * FROM users WHERE id = '1' OR '1'='1'

    const result = await this.pool.query(query);
    return result.rows;
  }
}

module.exports = SecureDatabase;
```

### 2. **Python with SQLAlchemy ORM**

```python
# secure_queries.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import re

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(100))
    password_hash = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

class SecureDatabase:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string, pool_pre_ping=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_user_by_id(self, user_id: int):
        """✅ SECURE: ORM query"""
        return self.session.query(User).filter(User.id == user_id).first()

    def search_users(self, email: str):
        """✅ SECURE: Parameterized LIKE query"""
        return self.session.query(User).filter(
            User.email.like(f'%{email}%')
        ).limit(100).all()

    def get_users_sorted(self, sort_by: str = 'created_at', order: str = 'desc'):
        """✅ SECURE: Whitelisted column sorting"""
        allowed_columns = {
            'id': User.id,
            'email': User.email,
            'name': User.name,
            'created_at': User.created_at
        }

        if sort_by not in allowed_columns:
            sort_by = 'created_at'

        column = allowed_columns[sort_by]

        if order.lower() == 'asc':
            column = column.asc()
        else:
            column = column.desc()

        return self.session.query(User).order_by(column).limit(100).all()

    def raw_query_secure(self, user_id: int):
        """✅ SECURE: Raw SQL with parameters"""
        from sqlalchemy import text

        query = text("SELECT * FROM users WHERE id = :id")
        result = self.session.execute(query, {'id': user_id})

        return result.fetchall()

    def validate_and_sanitize(self, input_str: str) -> str:
        """Validate and sanitize user input"""
        # Remove potentially dangerous characters
        # Only allow alphanumeric, spaces, and common punctuation
        sanitized = re.sub(r'[^\w\s@.,\-]', '', input_str)

        # Limit length
        sanitized = sanitized[:255]

        return sanitized

    def vulnerable_query(self, user_input: str):
        """❌ VULNERABLE: String formatting (DON'T USE)"""
        from sqlalchemy import text

        # VULNERABLE TO SQL INJECTION!
        query = text(f"SELECT * FROM users WHERE email = '{user_input}'")
        # Attack: user_input = "' OR '1'='1"

        result = self.session.execute(query)
        return result.fetchall()

# Usage
if __name__ == '__main__':
    db = SecureDatabase('postgresql://user:pass@localhost/mydb')

    # Secure queries
    user = db.get_user_by_id(123)
    users = db.search_users('example.com')
    sorted_users = db.get_users_sorted('email', 'asc')
```

### 3. **Java JDBC with Prepared Statements**

```java
// SecureDatabase.java
package com.example.security;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class SecureDatabase {
    private Connection connection;

    public SecureDatabase(String url, String username, String password)
            throws SQLException {
        this.connection = DriverManager.getConnection(url, username, password);
    }

    /**
     * ✅ SECURE: Prepared statement
     */
    public User getUserById(int userId) throws SQLException {
        String sql = "SELECT * FROM users WHERE id = ?";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, userId);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return new User(
                        rs.getInt("id"),
                        rs.getString("email"),
                        rs.getString("name")
                    );
                }
            }
        }

        return null;
    }

    /**
     * ✅ SECURE: Multiple parameters
     */
    public List<User> searchUsers(String email, String status)
            throws SQLException {
        String sql = "SELECT * FROM users WHERE email LIKE ? AND status = ? LIMIT 100";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, "%" + email + "%");
            stmt.setString(2, status);

            try (ResultSet rs = stmt.executeQuery()) {
                List<User> users = new ArrayList<>();

                while (rs.next()) {
                    users.add(new User(
                        rs.getInt("id"),
                        rs.getString("email"),
                        rs.getString("name")
                    ));
                }

                return users;
            }
        }
    }

    /**
     * ✅ SECURE: Batch insert
     */
    public void insertUsers(List<User> users) throws SQLException {
        String sql = "INSERT INTO users (email, name, password_hash) VALUES (?, ?, ?)";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            for (User user : users) {
                stmt.setString(1, user.getEmail());
                stmt.setString(2, user.getName());
                stmt.setString(3, user.getPasswordHash());
                stmt.addBatch();
            }

            stmt.executeBatch();
        }
    }

    /**
     * ✅ SECURE: Dynamic sorting with whitelist
     */
    public List<User> getUsersSorted(String sortBy, String order)
            throws SQLException {
        // Whitelist allowed values
        List<String> allowedColumns = List.of("id", "email", "name", "created_at");
        List<String> allowedOrders = List.of("ASC", "DESC");

        if (!allowedColumns.contains(sortBy)) {
            sortBy = "created_at";
        }

        if (!allowedOrders.contains(order.toUpperCase())) {
            order = "DESC";
        }

        // Safe to use in query since values are whitelisted
        String sql = String.format(
            "SELECT * FROM users ORDER BY %s %s LIMIT 100",
            sortBy, order
        );

        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            List<User> users = new ArrayList<>();

            while (rs.next()) {
                users.add(new User(
                    rs.getInt("id"),
                    rs.getString("email"),
                    rs.getString("name")
                ));
            }

            return users;
        }
    }

    /**
     * ❌ VULNERABLE: String concatenation (DON'T USE)
     */
    public List<User> vulnerableQuery(String userInput) throws SQLException {
        // VULNERABLE TO SQL INJECTION!
        String sql = "SELECT * FROM users WHERE email = '" + userInput + "'";
        // Attack: userInput = "' OR '1'='1"

        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            List<User> users = new ArrayList<>();

            while (rs.next()) {
                users.add(new User(
                    rs.getInt("id"),
                    rs.getString("email"),
                    rs.getString("name")
                ));
            }

            return users;
        }
    }
}

class User {
    private int id;
    private String email;
    private String name;
    private String passwordHash;

    public User(int id, String email, String name) {
        this.id = id;
        this.email = email;
        this.name = name;
    }

    // Getters and setters
    public String getEmail() { return email; }
    public String getName() { return name; }
    public String getPasswordHash() { return passwordHash; }
}
```

### 4. **Input Validation & Sanitization**

```javascript
// input-validator.js
class InputValidator {
  static validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 255;
  }

  static validateInteger(value) {
    const num = parseInt(value, 10);
    return Number.isInteger(num) && num >= 0;
  }

  static sanitizeString(input, maxLength = 255) {
    // Remove control characters
    let sanitized = input.replace(/[\x00-\x1F\x7F]/g, '');

    // Trim and limit length
    sanitized = sanitized.trim().substring(0, maxLength);

    return sanitized;
  }

  static validateSQLIdentifier(identifier) {
    // Only allow alphanumeric and underscore
    return /^[a-zA-Z_][a-zA-Z0-9_]*$/.test(identifier);
  }

  static escapeForLike(input) {
    // Escape LIKE wildcards
    return input.replace(/[%_]/g, '\\$&');
  }
}

module.exports = InputValidator;
```

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

## Prevention Techniques

1. **Prepared Statements**: Parameterized queries
2. **ORM Frameworks**: Abstraction layer
3. **Input Validation**: Whitelist approach
4. **Least Privilege**: Minimal DB permissions
5. **WAF**: Web Application Firewall
6. **Code Review**: Manual inspection

## Testing for SQL Injection

- **Manual testing**: Input payloads
- **Automated scanners**: SQLMap, Burp Suite
- **Code review**: Static analysis
- **Penetration testing**: Professional assessment

## Resources

- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [SQLMap](https://sqlmap.org/)
- [PortSwigger SQL Injection](https://portswigger.net/web-security/sql-injection)
