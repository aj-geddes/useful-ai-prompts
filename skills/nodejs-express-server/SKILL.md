---
name: nodejs-express-server
description: Build production-ready Express.js servers with middleware, authentication, routing, and database integration. Use when creating REST APIs, managing requests/responses, implementing middleware chains, and handling server logic.
---

# Node.js Express Server

## Overview

Create robust Express.js applications with proper routing, middleware chains, authentication mechanisms, and database integration following industry best practices.

## When to Use

- Building REST APIs with Node.js
- Implementing server-side request handling
- Creating middleware chains for cross-cutting concerns
- Managing authentication and authorization
- Connecting to databases from Node.js
- Implementing error handling and logging

## Instructions

### 1. **Basic Express Setup**

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message,
    requestId: req.id
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### 2. **Middleware Chain Implementation**

```javascript
// Logging middleware
const logger = (req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path} ${res.statusCode} ${duration}ms`);
  });
  next();
};

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
};

// Error catching middleware wrapper
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.use(logger);
app.use(express.json());
app.get('/protected', authenticateToken, (req, res) => {
  res.json({ user: req.user });
});
```

### 3. **Database Integration (PostgreSQL with Sequelize)**

```javascript
const { Sequelize, DataTypes } = require('sequelize');

const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASS,
  {
    host: process.env.DB_HOST,
    dialect: 'postgres',
    logging: false
  }
);

const User = sequelize.define('User', {
  id: {
    type: DataTypes.UUID,
    defaultValue: DataTypes.UUIDV4,
    primaryKey: true
  },
  email: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false
  },
  password: DataTypes.STRING,
  role: {
    type: DataTypes.ENUM('user', 'admin'),
    defaultValue: 'user'
  }
}, {
  timestamps: true
});

// Sync database
sequelize.sync({ alter: true });
```

### 4. **Authentication with JWT**

```javascript
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const generateToken = (userId) => {
  return jwt.sign(
    { userId, iat: Math.floor(Date.now() / 1000) },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );
};

app.post('/login', asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ where: { email } });

  if (!user) return res.status(404).json({ error: 'User not found' });

  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) return res.status(401).json({ error: 'Invalid password' });

  const token = generateToken(user.id);
  res.json({ token, user: { id: user.id, email: user.email } });
}));
```

### 5. **RESTful Routes with CRUD Operations**

```javascript
const userRouter = express.Router();

// GET all users (with pagination)
userRouter.get('/', authenticateToken, asyncHandler(async (req, res) => {
  const { page = 1, limit = 20 } = req.query;
  const users = await User.findAndCountAll({
    offset: (page - 1) * limit,
    limit: parseInt(limit)
  });

  res.json({
    data: users.rows,
    pagination: { page, limit, total: users.count }
  });
}));

// GET single user
userRouter.get('/:id', authenticateToken, asyncHandler(async (req, res) => {
  const user = await User.findByPk(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json({ data: user });
}));

// POST create user
userRouter.post('/', asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);

  const user = await User.create({
    email,
    password: hashedPassword
  });

  res.status(201).json({ data: user });
}));

// PATCH update user
userRouter.patch('/:id', authenticateToken, asyncHandler(async (req, res) => {
  const user = await User.findByPk(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });

  await user.update(req.body, {
    fields: ['email', 'role']
  });

  res.json({ data: user });
}));

// DELETE user
userRouter.delete('/:id', authenticateToken, asyncHandler(async (req, res) => {
  const user = await User.findByPk(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });

  await user.destroy();
  res.status(204).send();
}));

app.use('/api/users', userRouter);
```

### 6. **Error Handling Middleware**

```javascript
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    Error.captureStackTrace(this, this.constructor);
  }
}

app.use((err, req, res, next) => {
  err.statusCode = err.statusCode || 500;

  if (err.name === 'SequelizeValidationError') {
    return res.status(400).json({
      error: 'Validation failed',
      details: err.errors.map(e => ({ field: e.path, message: e.message }))
    });
  }

  if (process.env.NODE_ENV === 'production') {
    return res.status(err.statusCode).json({
      error: err.message,
      requestId: req.id
    });
  }

  res.status(err.statusCode).json({
    error: err.message,
    stack: err.stack
  });
});

app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});
```

### 7. **Environment Configuration**

```javascript
require('dotenv').config();

const config = {
  port: process.env.PORT || 3000,
  env: process.env.NODE_ENV || 'development',
  database: {
    url: process.env.DATABASE_URL,
    dialect: 'postgres'
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: '24h'
  },
  cors: {
    origin: process.env.CORS_ORIGIN || 'http://localhost:3000'
  }
};

module.exports = config;
```

## Best Practices

### ✅ DO
- Use middleware for cross-cutting concerns
- Implement proper error handling
- Validate input data before processing
- Use async/await for async operations
- Implement authentication on protected routes
- Use environment variables for configuration
- Add logging and monitoring
- Use HTTPS in production
- Implement rate limiting
- Keep route handlers focused and small

### ❌ DON'T
- Handle errors silently
- Store sensitive data in code
- Use synchronous operations in routes
- Forget to validate user input
- Implement authentication in route handlers
- Use callback hell (use promises/async-await)
- Expose stack traces in production
- Trust client-side validation only

## Complete Example

```javascript
const express = require('express');
const jwt = require('jsonwebtoken');
const { Sequelize, DataTypes } = require('sequelize');

const app = express();
app.use(express.json());

const sequelize = new Sequelize('postgres://user:pass@localhost/db');

const User = sequelize.define('User', {
  email: DataTypes.STRING,
  password: DataTypes.STRING
});

const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  jwt.verify(token, 'secret', (err, user) => {
    if (err) return res.status(403).json({ error: 'Forbidden' });
    req.user = user;
    next();
  });
};

app.get('/users', authenticateToken, async (req, res, next) => {
  try {
    const users = await User.findAll();
    res.json({ data: users });
  } catch (err) {
    next(err);
  }
});

app.post('/users', async (req, res, next) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json({ data: user });
  } catch (err) {
    next(err);
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));
```
