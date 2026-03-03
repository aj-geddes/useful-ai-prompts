# Node.js with PostgreSQL

## Node.js with PostgreSQL

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
      return result.rows[0];
    } catch (error) {
      console.error("Query error:", error);
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
  async getUsers(sortBy = "created_at", order = "DESC") {
    // Whitelist allowed columns
    const allowedColumns = ["id", "email", "name", "created_at"];
    const allowedOrders = ["ASC", "DESC"];

    if (!allowedColumns.includes(sortBy)) {
      sortBy = "created_at";
    }

    if (!allowedOrders.includes(order.toUpperCase())) {
      order = "DESC";
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
      await client.query("BEGIN");

      // Debit from account
      await client.query(
        "UPDATE accounts SET balance = balance - $1 WHERE id = $2",
        [amount, fromAccount],
      );

      // Credit to account
      await client.query(
        "UPDATE accounts SET balance = balance + $1 WHERE id = $2",
        [amount, toAccount],
      );

      // Record transaction
      await client.query(
        "INSERT INTO transactions (from_account, to_account, amount) VALUES ($1, $2, $3)",
        [fromAccount, toAccount, amount],
      );

      await client.query("COMMIT");
      return true;
    } catch (error) {
      await client.query("ROLLBACK");
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
