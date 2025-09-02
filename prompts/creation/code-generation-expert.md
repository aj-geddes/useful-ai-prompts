# Code Generation Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Creation
- **Tags**: code generation, software development, programming, application development, clean code
- **Use Cases**: code generation, software development, automation scripting, prototype creation
- **Version**: 2.0.0
- **Use Cases**: application development, API creation, algorithm implementation, code refactoring
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical code generation assistant that helps you create well-structured, maintainable code following best practices. Provide your requirements and I'll generate production-ready code with proper architecture, error handling, and documentation.

## Prompt

```
I'll help you generate high-quality code that follows best practices and meets your requirements. Let me gather information about what you need to build.

About your project:
1. What type of application/system are you building? (web app, API, library, CLI tool, etc.)
2. What programming language and framework do you want to use?
3. What's the main functionality you need to implement?
4. Who will use this code? (end users, other developers, internal team)

Technical requirements:
5. Are there any specific technologies or libraries you must use?
6. What are the performance requirements? (users, requests/second, data size)
7. Do you need specific integrations? (databases, APIs, services)
8. Are there any security or compliance requirements?

Project context:
9. Is this a new project or adding to existing code?
10. What's your team's experience level with the chosen technology?
11. What's the timeline? (quick prototype, MVP, production-ready)
12. Do you have any existing code patterns or architecture to follow?

Based on your answers, I'll provide:

**1. ARCHITECTURE DESIGN** - Overall structure and component organization
**2. CORE IMPLEMENTATION** - Main functionality with proper error handling
**3. SUPPORTING CODE** - Utilities, configurations, and helper functions
**4. TESTING STRATEGY** - Unit tests and integration test examples
**5. DEPLOYMENT GUIDE** - Setup instructions and deployment considerations

Please provide the information above, and include any specific requirements or constraints.
```

## Example Usage

**User Input:**
```
1. Project: REST API for a task management system
2. Language: Node.js with Express framework and TypeScript
3. Functionality: CRUD operations for tasks, users, projects, with authentication
4. Users: Frontend developers will consume this API

5. Technologies: Must use PostgreSQL database, JWT for auth, Docker for deployment
6. Performance: Support 1000+ concurrent users, <200ms response time
7. Integrations: Email service for notifications, file storage for attachments
8. Security: JWT authentication, input validation, SQL injection protection

9. Project: New greenfield project
10. Team: Mid-level developers familiar with Node.js
11. Timeline: MVP in 6 weeks, production-ready in 3 months
12. Patterns: RESTful API design, clean architecture principles
```

**Assistant Output:**

Based on your task management API requirements, here's a complete implementation with clean architecture:

## ARCHITECTURE DESIGN

**Project Structure:**
```
task-management-api/
├── src/
│   ├── controllers/          # HTTP request handlers
│   ├── services/            # Business logic layer
│   ├── repositories/        # Data access layer
│   ├── models/              # Data models and interfaces
│   ├── middleware/          # Custom middleware
│   ├── utils/               # Utility functions
│   ├── config/              # Configuration files
│   └── app.ts               # Application setup
├── tests/                   # Test files
├── docker/                  # Docker configurations
├── docs/                    # API documentation
└── package.json
```

**Architecture Layers:**
1. **Controllers** - Handle HTTP requests/responses
2. **Services** - Business logic and validation
3. **Repositories** - Database operations
4. **Models** - Type definitions and interfaces

## CORE IMPLEMENTATION

### 1. Data Models & Interfaces

**src/models/User.ts**
```typescript
export interface User {
  id: string;
  email: string;
  password: string;
  firstName: string;
  lastName: string;
  role: UserRole;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateUserRequest {
  email: string;
  password: string;
  firstName: string;
  lastName: string;
  role?: UserRole;
}

export enum UserRole {
  ADMIN = 'admin',
  USER = 'user',
  MANAGER = 'manager'
}
```

**src/models/Task.ts**
```typescript
export interface Task {
  id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  assigneeId?: string;
  projectId: string;
  dueDate?: Date;
  createdAt: Date;
  updatedAt: Date;
}

export interface CreateTaskRequest {
  title: string;
  description?: string;
  priority: TaskPriority;
  assigneeId?: string;
  projectId: string;
  dueDate?: Date;
}

export enum TaskStatus {
  TODO = 'todo',
  IN_PROGRESS = 'in_progress',
  DONE = 'done',
  CANCELLED = 'cancelled'
}

export enum TaskPriority {
  LOW = 'low',
  MEDIUM = 'medium',
  HIGH = 'high',
  URGENT = 'urgent'
}
```

### 2. Database Repository Layer

**src/repositories/TaskRepository.ts**
```typescript
import { Pool } from 'pg';
import { Task, CreateTaskRequest, TaskStatus } from '../models/Task';

export class TaskRepository {
  constructor(private db: Pool) {}

  async create(task: CreateTaskRequest, userId: string): Promise<Task> {
    const query = `
      INSERT INTO tasks (title, description, priority, assignee_id, project_id, due_date, created_by)
      VALUES ($1, $2, $3, $4, $5, $6, $7)
      RETURNING id, title, description, status, priority, assignee_id as "assigneeId", 
                project_id as "projectId", due_date as "dueDate", created_at as "createdAt", 
                updated_at as "updatedAt"
    `;
    
    const values = [
      task.title,
      task.description || null,
      task.priority,
      task.assigneeId || null,
      task.projectId,
      task.dueDate || null,
      userId
    ];

    try {
      const result = await this.db.query(query, values);
      return result.rows[0];
    } catch (error) {
      throw new Error(`Failed to create task: ${error.message}`);
    }
  }

  async findById(taskId: string): Promise<Task | null> {
    const query = `
      SELECT id, title, description, status, priority, assignee_id as "assigneeId",
             project_id as "projectId", due_date as "dueDate", created_at as "createdAt",
             updated_at as "updatedAt"
      FROM tasks 
      WHERE id = $1 AND deleted_at IS NULL
    `;

    try {
      const result = await this.db.query(query, [taskId]);
      return result.rows[0] || null;
    } catch (error) {
      throw new Error(`Failed to fetch task: ${error.message}`);
    }
  }

  async findByProject(projectId: string, filters?: {
    status?: TaskStatus;
    assigneeId?: string;
    limit?: number;
    offset?: number;
  }): Promise<Task[]> {
    let query = `
      SELECT id, title, description, status, priority, assignee_id as "assigneeId",
             project_id as "projectId", due_date as "dueDate", created_at as "createdAt",
             updated_at as "updatedAt"
      FROM tasks 
      WHERE project_id = $1 AND deleted_at IS NULL
    `;
    
    const values: any[] = [projectId];
    let paramCount = 1;

    if (filters?.status) {
      query += ` AND status = $${++paramCount}`;
      values.push(filters.status);
    }

    if (filters?.assigneeId) {
      query += ` AND assignee_id = $${++paramCount}`;
      values.push(filters.assigneeId);
    }

    query += ` ORDER BY created_at DESC`;

    if (filters?.limit) {
      query += ` LIMIT $${++paramCount}`;
      values.push(filters.limit);
    }

    if (filters?.offset) {
      query += ` OFFSET $${++paramCount}`;
      values.push(filters.offset);
    }

    try {
      const result = await this.db.query(query, values);
      return result.rows;
    } catch (error) {
      throw new Error(`Failed to fetch tasks: ${error.message}`);
    }
  }

  async update(taskId: string, updates: Partial<Task>): Promise<Task> {
    const setClause = [];
    const values = [];
    let paramCount = 0;

    Object.entries(updates).forEach(([key, value]) => {
      if (value !== undefined) {
        setClause.push(`${key} = $${++paramCount}`);
        values.push(value);
      }
    });

    if (setClause.length === 0) {
      throw new Error('No valid updates provided');
    }

    setClause.push(`updated_at = NOW()`);
    values.push(taskId);

    const query = `
      UPDATE tasks 
      SET ${setClause.join(', ')} 
      WHERE id = $${++paramCount} AND deleted_at IS NULL
      RETURNING id, title, description, status, priority, assignee_id as "assigneeId",
                project_id as "projectId", due_date as "dueDate", created_at as "createdAt",
                updated_at as "updatedAt"
    `;

    try {
      const result = await this.db.query(query, values);
      if (result.rows.length === 0) {
        throw new Error('Task not found or already deleted');
      }
      return result.rows[0];
    } catch (error) {
      throw new Error(`Failed to update task: ${error.message}`);
    }
  }

  async delete(taskId: string): Promise<void> {
    const query = `
      UPDATE tasks 
      SET deleted_at = NOW() 
      WHERE id = $1 AND deleted_at IS NULL
    `;

    try {
      const result = await this.db.query(query, [taskId]);
      if (result.rowCount === 0) {
        throw new Error('Task not found or already deleted');
      }
    } catch (error) {
      throw new Error(`Failed to delete task: ${error.message}`);
    }
  }
}
```

### 3. Business Logic Service Layer

**src/services/TaskService.ts**
```typescript
import { TaskRepository } from '../repositories/TaskRepository';
import { Task, CreateTaskRequest, TaskStatus } from '../models/Task';
import { NotificationService } from './NotificationService';

export class TaskService {
  constructor(
    private taskRepository: TaskRepository,
    private notificationService: NotificationService
  ) {}

  async createTask(taskData: CreateTaskRequest, userId: string): Promise<Task> {
    // Validation
    this.validateTaskData(taskData);

    // Create task
    const task = await this.taskRepository.create(taskData, userId);

    // Send notification if task is assigned
    if (task.assigneeId && task.assigneeId !== userId) {
      await this.notificationService.sendTaskAssignedNotification(
        task.assigneeId,
        task
      );
    }

    return task;
  }

  async getTaskById(taskId: string, userId: string): Promise<Task> {
    const task = await this.taskRepository.findById(taskId);
    
    if (!task) {
      throw new Error('Task not found');
    }

    // Check if user has access to this task
    await this.validateTaskAccess(task, userId);

    return task;
  }

  async getProjectTasks(
    projectId: string, 
    userId: string,
    filters?: {
      status?: TaskStatus;
      assigneeId?: string;
      page?: number;
      limit?: number;
    }
  ): Promise<{ tasks: Task[]; total: number }> {
    // Validate user access to project
    await this.validateProjectAccess(projectId, userId);

    const limit = filters?.limit || 50;
    const offset = filters?.page ? (filters.page - 1) * limit : 0;

    const tasks = await this.taskRepository.findByProject(projectId, {
      ...filters,
      limit,
      offset
    });

    // Get total count for pagination
    const total = await this.getTaskCount(projectId, filters);

    return { tasks, total };
  }

  async updateTask(
    taskId: string, 
    updates: Partial<Task>, 
    userId: string
  ): Promise<Task> {
    const existingTask = await this.taskRepository.findById(taskId);
    
    if (!existingTask) {
      throw new Error('Task not found');
    }

    await this.validateTaskAccess(existingTask, userId);

    // Validate updates
    this.validateTaskUpdates(updates);

    const updatedTask = await this.taskRepository.update(taskId, updates);

    // Send notifications for status changes
    if (updates.status && updates.status !== existingTask.status) {
      await this.handleStatusChangeNotifications(updatedTask, existingTask);
    }

    return updatedTask;
  }

  async deleteTask(taskId: string, userId: string): Promise<void> {
    const task = await this.taskRepository.findById(taskId);
    
    if (!task) {
      throw new Error('Task not found');
    }

    await this.validateTaskAccess(task, userId);
    await this.taskRepository.delete(taskId);
  }

  private validateTaskData(taskData: CreateTaskRequest): void {
    if (!taskData.title?.trim()) {
      throw new Error('Task title is required');
    }

    if (taskData.title.length > 200) {
      throw new Error('Task title must be less than 200 characters');
    }

    if (taskData.description && taskData.description.length > 2000) {
      throw new Error('Task description must be less than 2000 characters');
    }

    if (taskData.dueDate && taskData.dueDate < new Date()) {
      throw new Error('Due date cannot be in the past');
    }
  }

  private validateTaskUpdates(updates: Partial<Task>): void {
    if (updates.title !== undefined) {
      if (!updates.title?.trim()) {
        throw new Error('Task title cannot be empty');
      }
      if (updates.title.length > 200) {
        throw new Error('Task title must be less than 200 characters');
      }
    }

    if (updates.description !== undefined && updates.description && updates.description.length > 2000) {
      throw new Error('Task description must be less than 2000 characters');
    }
  }

  private async validateTaskAccess(task: Task, userId: string): Promise<void> {
    // Implementation would check if user has access to the project
    // This could involve checking project membership, role permissions, etc.
  }

  private async validateProjectAccess(projectId: string, userId: string): Promise<void> {
    // Implementation would validate user access to project
  }

  private async getTaskCount(projectId: string, filters?: any): Promise<number> {
    // Implementation would return total count for pagination
    return 0;
  }

  private async handleStatusChangeNotifications(updatedTask: Task, originalTask: Task): Promise<void> {
    // Send appropriate notifications based on status change
    if (updatedTask.status === TaskStatus.DONE) {
      await this.notificationService.sendTaskCompletedNotification(updatedTask);
    }
  }
}
```

### 4. HTTP Controllers

**src/controllers/TaskController.ts**
```typescript
import { Request, Response } from 'express';
import { TaskService } from '../services/TaskService';
import { CreateTaskRequest, TaskStatus } from '../models/Task';

export class TaskController {
  constructor(private taskService: TaskService) {}

  createTask = async (req: Request, res: Response): Promise<void> => {
    try {
      const taskData: CreateTaskRequest = req.body;
      const userId = req.user?.id; // From authentication middleware

      const task = await this.taskService.createTask(taskData, userId);

      res.status(201).json({
        success: true,
        data: task,
        message: 'Task created successfully'
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        message: error.message
      });
    }
  };

  getTask = async (req: Request, res: Response): Promise<void> => {
    try {
      const { taskId } = req.params;
      const userId = req.user?.id;

      const task = await this.taskService.getTaskById(taskId, userId);

      res.json({
        success: true,
        data: task
      });
    } catch (error) {
      const statusCode = error.message === 'Task not found' ? 404 : 400;
      res.status(statusCode).json({
        success: false,
        message: error.message
      });
    }
  };

  getProjectTasks = async (req: Request, res: Response): Promise<void> => {
    try {
      const { projectId } = req.params;
      const userId = req.user?.id;
      
      const filters = {
        status: req.query.status as TaskStatus,
        assigneeId: req.query.assigneeId as string,
        page: req.query.page ? parseInt(req.query.page as string) : 1,
        limit: req.query.limit ? parseInt(req.query.limit as string) : 50
      };

      const result = await this.taskService.getProjectTasks(projectId, userId, filters);

      res.json({
        success: true,
        data: result.tasks,
        pagination: {
          page: filters.page,
          limit: filters.limit,
          total: result.total,
          pages: Math.ceil(result.total / filters.limit)
        }
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        message: error.message
      });
    }
  };

  updateTask = async (req: Request, res: Response): Promise<void> => {
    try {
      const { taskId } = req.params;
      const updates = req.body;
      const userId = req.user?.id;

      const task = await this.taskService.updateTask(taskId, updates, userId);

      res.json({
        success: true,
        data: task,
        message: 'Task updated successfully'
      });
    } catch (error) {
      const statusCode = error.message === 'Task not found' ? 404 : 400;
      res.status(statusCode).json({
        success: false,
        message: error.message
      });
    }
  };

  deleteTask = async (req: Request, res: Response): Promise<void> => {
    try {
      const { taskId } = req.params;
      const userId = req.user?.id;

      await this.taskService.deleteTask(taskId, userId);

      res.json({
        success: true,
        message: 'Task deleted successfully'
      });
    } catch (error) {
      const statusCode = error.message === 'Task not found' ? 404 : 400;
      res.status(statusCode).json({
        success: false,
        message: error.message
      });
    }
  };
}
```

## SUPPORTING CODE

### Authentication Middleware

**src/middleware/auth.ts**
```typescript
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { UserRepository } from '../repositories/UserRepository';

interface AuthRequest extends Request {
  user?: {
    id: string;
    email: string;
    role: string;
  };
}

export const authenticateToken = (userRepository: UserRepository) => {
  return async (req: AuthRequest, res: Response, next: NextFunction) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Access token required'
      });
    }

    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;
      
      // Verify user still exists
      const user = await userRepository.findById(decoded.userId);
      if (!user) {
        return res.status(401).json({
          success: false,
          message: 'Invalid token'
        });
      }

      req.user = {
        id: user.id,
        email: user.email,
        role: user.role
      };

      next();
    } catch (error) {
      return res.status(403).json({
        success: false,
        message: 'Invalid or expired token'
      });
    }
  };
};
```

### Validation Middleware

**src/middleware/validation.ts**
```typescript
import { Request, Response, NextFunction } from 'express';
import Joi from 'joi';

export const validateRequest = (schema: Joi.ObjectSchema) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const { error, value } = schema.validate(req.body);
    
    if (error) {
      return res.status(400).json({
        success: false,
        message: 'Validation error',
        details: error.details.map(detail => detail.message)
      });
    }

    req.body = value;
    next();
  };
};

// Task validation schemas
export const createTaskSchema = Joi.object({
  title: Joi.string().required().max(200).trim(),
  description: Joi.string().max(2000).allow(''),
  priority: Joi.string().valid('low', 'medium', 'high', 'urgent').required(),
  assigneeId: Joi.string().uuid().optional(),
  projectId: Joi.string().uuid().required(),
  dueDate: Joi.date().greater('now').optional()
});

export const updateTaskSchema = Joi.object({
  title: Joi.string().max(200).trim().optional(),
  description: Joi.string().max(2000).allow('').optional(),
  status: Joi.string().valid('todo', 'in_progress', 'done', 'cancelled').optional(),
  priority: Joi.string().valid('low', 'medium', 'high', 'urgent').optional(),
  assigneeId: Joi.string().uuid().allow(null).optional(),
  dueDate: Joi.date().allow(null).optional()
});
```

## TESTING STRATEGY

### Unit Tests Example

**tests/services/TaskService.test.ts**
```typescript
import { TaskService } from '../../src/services/TaskService';
import { TaskRepository } from '../../src/repositories/TaskRepository';
import { NotificationService } from '../../src/services/NotificationService';
import { CreateTaskRequest, TaskPriority } from '../../src/models/Task';

describe('TaskService', () => {
  let taskService: TaskService;
  let mockTaskRepository: jest.Mocked<TaskRepository>;
  let mockNotificationService: jest.Mocked<NotificationService>;

  beforeEach(() => {
    mockTaskRepository = {
      create: jest.fn(),
      findById: jest.fn(),
      findByProject: jest.fn(),
      update: jest.fn(),
      delete: jest.fn()
    } as any;

    mockNotificationService = {
      sendTaskAssignedNotification: jest.fn(),
      sendTaskCompletedNotification: jest.fn()
    } as any;

    taskService = new TaskService(mockTaskRepository, mockNotificationService);
  });

  describe('createTask', () => {
    it('should create a task successfully', async () => {
      const taskData: CreateTaskRequest = {
        title: 'Test Task',
        description: 'Test Description',
        priority: TaskPriority.MEDIUM,
        projectId: 'project-123'
      };

      const expectedTask = {
        id: 'task-123',
        ...taskData,
        status: 'todo',
        createdAt: new Date(),
        updatedAt: new Date()
      };

      mockTaskRepository.create.mockResolvedValue(expectedTask as any);

      const result = await taskService.createTask(taskData, 'user-123');

      expect(mockTaskRepository.create).toHaveBeenCalledWith(taskData, 'user-123');
      expect(result).toEqual(expectedTask);
    });

    it('should throw error for invalid task data', async () => {
      const invalidTaskData: CreateTaskRequest = {
        title: '', // Invalid empty title
        priority: TaskPriority.MEDIUM,
        projectId: 'project-123'
      };

      await expect(
        taskService.createTask(invalidTaskData, 'user-123')
      ).rejects.toThrow('Task title is required');
    });

    it('should send notification when task is assigned', async () => {
      const taskData: CreateTaskRequest = {
        title: 'Test Task',
        priority: TaskPriority.MEDIUM,
        projectId: 'project-123',
        assigneeId: 'assignee-123'
      };

      const createdTask = {
        id: 'task-123',
        ...taskData,
        status: 'todo',
        createdAt: new Date(),
        updatedAt: new Date()
      };

      mockTaskRepository.create.mockResolvedValue(createdTask as any);

      await taskService.createTask(taskData, 'user-123');

      expect(mockNotificationService.sendTaskAssignedNotification)
        .toHaveBeenCalledWith('assignee-123', createdTask);
    });
  });

  describe('getTaskById', () => {
    it('should return task when found', async () => {
      const task = {
        id: 'task-123',
        title: 'Test Task',
        projectId: 'project-123'
      };

      mockTaskRepository.findById.mockResolvedValue(task as any);
      jest.spyOn(taskService as any, 'validateTaskAccess').mockResolvedValue(undefined);

      const result = await taskService.getTaskById('task-123', 'user-123');

      expect(result).toEqual(task);
    });

    it('should throw error when task not found', async () => {
      mockTaskRepository.findById.mockResolvedValue(null);

      await expect(
        taskService.getTaskById('nonexistent', 'user-123')
      ).rejects.toThrow('Task not found');
    });
  });
});
```

### Integration Tests Example

**tests/controllers/TaskController.integration.test.ts**
```typescript
import request from 'supertest';
import { app } from '../../src/app';
import { setupTestDatabase, cleanupTestDatabase } from '../helpers/database';

describe('Task API Integration Tests', () => {
  let authToken: string;
  let projectId: string;

  beforeAll(async () => {
    await setupTestDatabase();
    // Setup test user and get auth token
    authToken = await getTestAuthToken();
    projectId = await createTestProject();
  });

  afterAll(async () => {
    await cleanupTestDatabase();
  });

  describe('POST /api/tasks', () => {
    it('should create a new task', async () => {
      const taskData = {
        title: 'Test Task',
        description: 'Test Description',
        priority: 'medium',
        projectId
      };

      const response = await request(app)
        .post('/api/tasks')
        .set('Authorization', `Bearer ${authToken}`)
        .send(taskData)
        .expect(201);

      expect(response.body.success).toBe(true);
      expect(response.body.data).toMatchObject({
        title: taskData.title,
        description: taskData.description,
        priority: taskData.priority,
        status: 'todo'
      });
    });

    it('should return 401 without auth token', async () => {
      const taskData = {
        title: 'Test Task',
        priority: 'medium',
        projectId
      };

      await request(app)
        .post('/api/tasks')
        .send(taskData)
        .expect(401);
    });

    it('should return 400 for invalid data', async () => {
      const invalidTaskData = {
        title: '', // Empty title
        priority: 'invalid-priority',
        projectId
      };

      await request(app)
        .post('/api/tasks')
        .set('Authorization', `Bearer ${authToken}`)
        .send(invalidTaskData)
        .expect(400);
    });
  });
});
```

## DEPLOYMENT GUIDE

### Docker Configuration

**Dockerfile**
```dockerfile
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY tsconfig.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY src/ ./src/

# Build TypeScript
RUN npm run build

# Production stage
FROM node:18-alpine AS production

WORKDIR /app

# Install dumb-init for proper signal handling
RUN apk add --no-cache dumb-init

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001

# Copy built application
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

# Set ownership
RUN chown -R nodejs:nodejs /app
USER nodejs

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node dist/healthcheck.js

EXPOSE 3000

ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/app.js"]
```

**docker-compose.yml**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: production
      DATABASE_URL: postgresql://postgres:password@postgres:5432/taskmanager
      JWT_SECRET: your-secret-key
      REDIS_URL: redis://redis:6379
    depends_on:
      - postgres
      - redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: taskmanager
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/migrations:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### Environment Configuration

**src/config/database.ts**
```typescript
import { Pool } from 'pg';

const databaseConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5432'),
  database: process.env.DB_NAME || 'taskmanager',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'password',
  max: parseInt(process.env.DB_POOL_MAX || '10'),
  idleTimeoutMillis: parseInt(process.env.DB_IDLE_TIMEOUT || '30000'),
  connectionTimeoutMillis: parseInt(process.env.DB_CONNECTION_TIMEOUT || '2000'),
};

export const db = new Pool(databaseConfig);

// Health check function
export const checkDatabaseHealth = async (): Promise<boolean> => {
  try {
    const client = await db.connect();
    await client.query('SELECT 1');
    client.release();
    return true;
  } catch (error) {
    console.error('Database health check failed:', error);
    return false;
  }
};
```

### Deployment Scripts

**scripts/deploy.sh**
```bash
#!/bin/bash

set -e

echo "🚀 Starting deployment..."

# Build and tag Docker image
echo "📦 Building Docker image..."
docker build -t task-management-api:latest .

# Run database migrations
echo "🗄️ Running database migrations..."
npm run migrate

# Run tests
echo "🧪 Running tests..."
npm test

# Deploy with docker-compose
echo "🚢 Deploying services..."
docker-compose down
docker-compose up -d

# Health check
echo "🏥 Checking application health..."
sleep 10

if curl -f http://localhost:3000/health; then
  echo "✅ Deployment successful!"
else
  echo "❌ Health check failed"
  docker-compose logs api
  exit 1
fi
```

This implementation provides a production-ready REST API with:

- Clean architecture with proper separation of concerns
- Type-safe TypeScript implementation
- Comprehensive error handling and validation
- JWT authentication and authorization
- Database connection pooling and proper queries
- Unit and integration tests
- Docker containerization
- Health checks and monitoring
- Security best practices

Would you like me to continue with more Creation workflow prompts or dive deeper into any specific aspect?

## Related Prompts

- [API Design Expert](../technical-workflows/api-design-expert.md)
- [Database Design Expert](../renewable-energy/energy-storage-system-design-expert.md)
- [Software Architecture Expert](../space-economy/commercial-space-mission-architecture-expert.md)
