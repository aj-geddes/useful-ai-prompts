# Java JDBC with Prepared Statements

## Java JDBC with Prepared Statements

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
