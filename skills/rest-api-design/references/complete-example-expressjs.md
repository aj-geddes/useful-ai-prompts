# Complete Example: Express.js

```javascript
const express = require("express");
const app = express();

app.use(express.json());

// List users with pagination
app.get("/api/v1/users", async (req, res) => {
  try {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 20;
    const offset = (page - 1) * limit;

    const users = await User.findAndCountAll({
      limit,
      offset,
      attributes: ["id", "email", "firstName", "lastName"],
    });

    res.json({
      data: users.rows,
      pagination: {
        page,
        limit,
        total: users.count,
        totalPages: Math.ceil(users.count / limit),
      },
    });
  } catch (error) {
    res.status(500).json({
      error: {
        code: "INTERNAL_ERROR",
        message: "An error occurred while fetching users",
      },
    });
  }
});

// Get single user
app.get("/api/v1/users/:id", async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);

    if (!user) {
      return res.status(404).json({
        error: {
          code: "NOT_FOUND",
          message: "User not found",
        },
      });
    }

    res.json({ data: user });
  } catch (error) {
    res.status(500).json({
      error: {
        code: "INTERNAL_ERROR",
        message: "An error occurred",
      },
    });
  }
});

// Create user
app.post("/api/v1/users", async (req, res) => {
  try {
    const { email, firstName, lastName } = req.body;

    // Validation
    if (!email || !firstName || !lastName) {
      return res.status(400).json({
        error: {
          code: "VALIDATION_ERROR",
          message: "Missing required fields",
          details: [
            !email && { field: "email", message: "Email is required" },
            !firstName && {
              field: "firstName",
              message: "First name is required",
            },
            !lastName && {
              field: "lastName",
              message: "Last name is required",
            },
          ].filter(Boolean),
        },
      });
    }

    const user = await User.create({ email, firstName, lastName });

    res.status(201).location(`/api/v1/users/${user.id}`).json({ data: user });
  } catch (error) {
    if (error.name === "SequelizeUniqueConstraintError") {
      return res.status(409).json({
        error: {
          code: "CONFLICT",
          message: "Email already exists",
        },
      });
    }
    res.status(500).json({
      error: {
        code: "INTERNAL_ERROR",
        message: "An error occurred",
      },
    });
  }
});

app.listen(3000);
```
