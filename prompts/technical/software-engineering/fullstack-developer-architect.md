# Full Stack Development Expert

## Metadata
- **Created**: 2025-07-31

- **Category**: Technical/Software Engineering
- **Tags**: full stack, web development, system architecture, frontend, backend, DevOps
- **Version**: 3.0.0
- **Use Cases**: application development, system design, API architecture, performance optimization
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you design and build full-stack applications with proper architecture, best practices, and scalable code that delivers great user experiences.

## Prompt

```
I'll help you build a full-stack application from concept to deployment. Let me understand your project requirements:

**About your application:**
1. What type of application are you building? (web app, mobile app, API, etc.)
2. What's the main purpose and core functionality?
3. Who are your target users and how many do you expect?
4. Do you have any existing systems to integrate with?

**Technical preferences:**
5. What's your experience level with different technologies?
6. Any specific frontend framework preferences? (React, Vue, Angular, etc.)
7. Backend language/framework preferences? (Node.js, Python, Java, etc.)
8. Database needs? (relational, NoSQL, or hybrid)

**Project constraints:**
9. What's your timeline and budget?
10. Any hosting or deployment preferences? (AWS, Azure, Vercel, etc.)
11. Security or compliance requirements?
12. Performance requirements? (users, response times, uptime)

Based on your answers, I'll provide:

**SYSTEM ARCHITECTURE** - High-level design with technology recommendations
**FRONTEND IMPLEMENTATION** - UI/UX components with responsive design
**BACKEND SERVICES** - API design with database schema and business logic
**DEPLOYMENT STRATEGY** - Production setup with CI/CD and monitoring
**DEVELOPMENT ROADMAP** - Phased implementation plan with milestones

Tell me about your application idea and requirements.
```

## Example Usage

**User Input:**
```
1. Task management web application for small teams
2. Teams can create projects, assign tasks, track progress, collaborate
3. 5-50 person teams, expect 100 teams initially, grow to 1000 teams
4. Need to integrate with Slack, email notifications, maybe calendar apps

5. Intermediate - comfortable with React, some Node.js experience
6. React (familiar), maybe Next.js for better performance
7. Node.js with Express, or maybe try TypeScript
8. Need user auth, real-time updates, file attachments

9. 4 months to MVP, bootstrap budget (~$5K/month)
10. Prefer cloud hosting, heard good things about Vercel/Railway
11. Standard business data protection, GDPR compliance eventually
12. Real-time updates, handles 50 concurrent users per team

Current pain points we're solving:
- Teams using mix of Slack, email, spreadsheets
- No central place to track project progress  
- Hard to see who's working on what
- File sharing is chaotic
```

**Assistant Output:**

Based on your team task management app with real-time collaboration needs, here's your full-stack architecture:

## SYSTEM ARCHITECTURE

### TECHNOLOGY STACK RECOMMENDATION

**Frontend: React + Next.js**
```
├── Next.js 14 (App Router)
├── TypeScript for type safety
├── Tailwind CSS for styling
├── React Query for data fetching
├── Socket.io client for real-time
└── Framer Motion for animations
```

**Backend: Node.js + TypeScript**
```
├── Express.js with TypeScript
├── Socket.io for real-time updates
├── Prisma ORM for database
├── JWT + bcrypt for authentication
├── Multer for file uploads
└── Bull for background jobs
```

**Database: PostgreSQL + Redis**
```
├── PostgreSQL (main database)
│   ├── Users, Teams, Projects, Tasks
│   ├── Comments, Files, Notifications
│   └── Audit logs, Settings
└── Redis (caching + sessions)
    ├── Session storage
    ├── Real-time pub/sub
    └── Rate limiting
```

**Infrastructure: Vercel + Railway**
```
├── Vercel (Frontend hosting)
├── Railway (Backend + Database)
├── Cloudinary (File storage)
└── GitHub Actions (CI/CD)
```

### SYSTEM DESIGN

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Next.js App  │────│   Express API    │────│   PostgreSQL    │
│   (Frontend)    │    │   (Backend)      │    │   (Database)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌──────────────────┐             │
         └──────────────│   Socket.io      │─────────────┘
                        │   (Real-time)    │
                        └──────────────────┘
                                 │
                        ┌──────────────────┐
                        │     Redis        │
                        │   (Cache/Queue)  │
                        └──────────────────┘
```

## FRONTEND IMPLEMENTATION

### COMPONENT ARCHITECTURE

**App Structure:**
```
src/
├── app/                     # Next.js app router
│   ├── (auth)/             # Authentication pages
│   ├── dashboard/          # Main app pages
│   ├── projects/[id]/      # Project details
│   └── teams/[id]/         # Team management
├── components/             # Reusable components
│   ├── ui/                 # Basic UI components
│   ├── forms/              # Form components
│   ├── modals/             # Modal dialogs
│   └── layout/             # Layout components
├── hooks/                  # Custom React hooks
├── lib/                    # Utilities and config
└── types/                  # TypeScript definitions
```

### KEY COMPONENTS

**1. Task Board Component**
```typescript
// components/TaskBoard.tsx
interface TaskBoardProps {
  projectId: string;
  tasks: Task[];
  onTaskUpdate: (task: Task) => void;
}

export function TaskBoard({ projectId, tasks, onTaskUpdate }: TaskBoardProps) {
  const [columns, setColumns] = useState(['todo', 'in-progress', 'done']);
  
  // Real-time task updates
  useSocket(`project:${projectId}`, (data) => {
    if (data.type === 'task_updated') {
      onTaskUpdate(data.task);
    }
  });

  return (
    <div className="grid grid-cols-3 gap-6">
      {columns.map(status => (
        <TaskColumn 
          key={status}
          status={status}
          tasks={tasks.filter(t => t.status === status)}
          onDrop={handleTaskMove}
        />
      ))}
    </div>
  );
}
```

**2. Real-time Hook**
```typescript
// hooks/useSocket.ts
export function useSocket(room: string, onMessage: (data: any) => void) {
  useEffect(() => {
    const socket = io();
    socket.emit('join_room', room);
    socket.on('message', onMessage);
    
    return () => {
      socket.emit('leave_room', room);
      socket.disconnect();
    };
  }, [room, onMessage]);
}
```

### RESPONSIVE DESIGN

**Mobile-First Approach:**
```css
/* Tailwind CSS classes for responsiveness */
<div className="
  grid grid-cols-1           /* Mobile: 1 column */
  md:grid-cols-2            /* Tablet: 2 columns */
  lg:grid-cols-3            /* Desktop: 3 columns */
  gap-4 md:gap-6            /* Responsive spacing */
  p-4 md:p-6 lg:p-8         /* Responsive padding */
">
```

## BACKEND SERVICES

### API DESIGN

**RESTful Endpoints:**
```
Authentication:
POST   /api/auth/register    # User registration
POST   /api/auth/login       # User login
POST   /api/auth/refresh     # Token refresh
DELETE /api/auth/logout      # User logout

Teams:
GET    /api/teams            # List user's teams
POST   /api/teams            # Create new team
GET    /api/teams/:id        # Get team details
PUT    /api/teams/:id        # Update team
DELETE /api/teams/:id        # Delete team

Projects:
GET    /api/teams/:id/projects     # List team projects
POST   /api/teams/:id/projects     # Create project
GET    /api/projects/:id           # Get project details
PUT    /api/projects/:id           # Update project
DELETE /api/projects/:id           # Delete project

Tasks:
GET    /api/projects/:id/tasks     # List project tasks
POST   /api/projects/:id/tasks     # Create task
PUT    /api/tasks/:id              # Update task
DELETE /api/tasks/:id              # Delete task
```

### DATABASE SCHEMA

**Core Tables:**
```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  avatar_url TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Teams table
CREATE TABLE teams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  owner_id UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Projects table
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  team_id UUID REFERENCES teams(id),
  status VARCHAR(50) DEFAULT 'active',
  due_date DATE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Tasks table
CREATE TABLE tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  project_id UUID REFERENCES projects(id),
  assignee_id UUID REFERENCES users(id),
  status VARCHAR(50) DEFAULT 'todo',
  priority VARCHAR(20) DEFAULT 'medium',
  due_date TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### REAL-TIME IMPLEMENTATION

**Socket.io Server Setup:**
```typescript
// server/socket.ts
export function setupSocket(server: any) {
  const io = new Server(server, {
    cors: { origin: process.env.FRONTEND_URL }
  });

  io.on('connection', (socket) => {
    socket.on('join_room', (room) => {
      socket.join(room);
    });

    socket.on('task_update', async (data) => {
      // Update database
      const task = await updateTask(data.taskId, data.changes);
      
      // Broadcast to room
      io.to(`project:${task.projectId}`).emit('message', {
        type: 'task_updated',
        task: task
      });
    });
  });
}
```

## DEPLOYMENT STRATEGY

### DEVELOPMENT ENVIRONMENT

**Local Development Setup:**
```bash
# Backend setup
cd backend
npm install
cp .env.example .env
npm run dev              # Starts on port 3001

# Frontend setup  
cd frontend
npm install
cp .env.local.example .env.local
npm run dev              # Starts on port 3000

# Database setup
docker-compose up -d     # PostgreSQL + Redis
npm run db:migrate       # Run migrations
npm run db:seed          # Seed test data
```

### PRODUCTION DEPLOYMENT

**Railway (Backend + Database):**
```yaml
# railway.toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "npm start"

[env]
DATABASE_URL = "${{Railway.DATABASE_URL}}"
REDIS_URL = "${{Railway.REDIS_URL}}"
JWT_SECRET = "${{Railway.JWT_SECRET}}"
```

**Vercel (Frontend):**
```json
{
  "name": "task-manager-frontend",
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next"
    }
  ],
  "env": {
    "NEXT_PUBLIC_API_URL": "https://your-backend.railway.app"
  }
}
```

### CI/CD PIPELINE

**GitHub Actions:**
```yaml
# .github/workflows/deploy.yml
name: Deploy Application

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run test
      - run: npm run type-check

  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: railway deploy --service backend

  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: vercel deploy --prod
```

## DEVELOPMENT ROADMAP

### PHASE 1: MVP (Month 1-2)

**Week 1-2: Foundation**
- Set up development environment
- Basic authentication system
- User registration and login
- Simple dashboard layout

**Week 3-4: Core Features**  
- Team creation and management
- Project creation and listing
- Basic task CRUD operations
- Simple task board view

**Week 5-6: Essential Features**
- Task assignment and status updates
- Basic real-time updates
- File upload functionality
- User profile management

**Week 7-8: Polish & Deploy**
- Responsive design implementation
- Error handling and validation
- Basic testing coverage
- MVP deployment

### PHASE 2: ENHANCEMENT (Month 3)

**Week 9-10: Advanced Features**
- Advanced task filtering and search
- Task comments and collaboration
- Email notifications
- Improved real-time features

**Week 11-12: Integrations**
- Slack integration setup
- Calendar integration (Google/Outlook)
- Export functionality
- Performance optimization

### PHASE 3: SCALE (Month 4)

**Week 13-14: Performance & Scale**
- Database optimization
- Caching implementation
- Load testing and optimization
- Advanced monitoring setup

**Week 15-16: Business Features**
- Team analytics and reporting
- Advanced permissions system
- API rate limiting
- GDPR compliance features

## EXPECTED RESULTS

**Technical Achievements:**
- Sub-200ms API response times
- 99.9% uptime reliability
- Real-time updates under 100ms
- Mobile-responsive on all devices

**Business Metrics:**
- Support 1000+ teams (50 users each)
- 95%+ user satisfaction
- <2 second page load times
- 99%+ feature availability

**Development Efficiency:**
- 80%+ test coverage
- Automated deployment pipeline
- Comprehensive monitoring
- Easy feature addition process

**Estimated Costs:**
- Vercel Pro: $20/month
- Railway: $30/month for backend + DB
- Cloudinary: $10/month for file storage
- Total: ~$60/month for production

Would you like me to elaborate on any specific part of this architecture or provide more detailed implementation code for particular features?
```

## Related Prompts

- [API Design Expert](../api-design-expert.md)
- [Database Design Expert](../database-design-expert.md)
- [DevOps Expert](../../devops/deployment-expert.md)