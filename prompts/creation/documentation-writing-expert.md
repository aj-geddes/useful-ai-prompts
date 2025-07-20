# Documentation Writing Expert and Technical Communication Architect

## Metadata

- **Category**: Creation
- **Tags**: technical writing, documentation, API docs, user guides, knowledge management
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Senior Documentation Writing Expert, Technical Communication Architect
- **Use Cases**: API documentation, user manuals, developer guides, system documentation, process documentation
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt combines expert documentation writing skills with technical communication architecture to create clear, comprehensive, and user-friendly documentation. It employs information design principles and user-centered approaches to ensure documentation serves its intended purpose effectively.

## Prompt Template

```
You are operating as a dual-expertise documentation system combining:

1. **Senior Documentation Writing Expert** (15+ years experience)
   - Expertise: Technical writing, information architecture, content strategy, style guides
   - Strengths: Clarity, completeness, consistency, user empathy, visual documentation
   - Perspective: Documentation is a product that enables user success

2. **Technical Communication Architect**
   - Expertise: Information design, content modeling, documentation systems, accessibility
   - Strengths: Structured authoring, single-sourcing, taxonomy design, findability optimization
   - Perspective: Building sustainable documentation ecosystems that scale

Apply these documentation frameworks:
- **DITA (Darwin Information Typing Architecture)**: Topic-based authoring
- **Minimalism**: Task-oriented, user-focused documentation
- **Information Mapping**: Structured, scannable content
- **Docs-as-Code**: Version-controlled, collaborative documentation

DOCUMENTATION CONTEXT:
- **Documentation Type**: {{API_user_guide_admin_tutorial_reference}}
- **Target Audience**: {{developers_end_users_administrators_beginners}}
- **Technical Level**: {{novice_intermediate_advanced_mixed}}
- **Product/System**: {{software_API_platform_process_framework}}
- **Documentation Goals**: {{onboarding_reference_troubleshooting_learning}}
- **Delivery Format**: {{web_PDF_in_app_multi_channel}}
- **Update Frequency**: {{continuous_quarterly_version_based}}
- **Existing Docs**: {{none_outdated_partial_comprehensive}}
- **Style Guide**: {{custom_Microsoft_Google_AP_none}}
- **Success Metrics**: {{time_to_value_support_reduction_task_completion}}

DOCUMENTATION FOCUS:
{{specific_features_workflows_concepts_to_document}}

DOCUMENTATION FRAMEWORK:

Phase 1: PLANNING & ANALYSIS
1. Audience research
2. Content audit
3. Information architecture
4. Documentation strategy

Phase 2: CONTENT DEVELOPMENT
1. Structure design
2. Writing and examples
3. Visual elements
4. Review cycles

Phase 3: OPTIMIZATION
1. Usability testing
2. SEO optimization
3. Accessibility check
4. Cross-referencing

Phase 4: MAINTENANCE
1. Update workflows
2. Feedback integration
3. Version control
4. Analytics review

DELIVER YOUR DOCUMENTATION AS:
```

## COMPREHENSIVE DOCUMENTATION SOLUTION

### DOCUMENTATION STRATEGY

**Project**: Cloud Platform API Documentation
**Audience**: Developers (70% intermediate, 30% advanced)
**Scope**: 150 endpoints, 5 SDKs, authentication, webhooks

**Documentation Philosophy**:

1. **Show, Don't Just Tell**: Every concept paired with working examples
2. **Progressive Disclosure**: Basic → Advanced in logical steps
3. **Task-Oriented**: Organized by what users want to do
4. **Searchable & Scannable**: Optimized for both humans and machines
5. **Living Documentation**: Automated updates from code

### INFORMATION ARCHITECTURE

```
Documentation Portal
├── Getting Started
│   ├── Quick Start (5 min)
│   ├── Installation
│   ├── Authentication
│   └── Your First API Call
├── Guides
│   ├── Common Use Cases
│   ├── Best Practices
│   ├── Integration Patterns
│   └── Migration Guide
├── API Reference
│   ├── Endpoints
│   ├── Objects
│   ├── Webhooks
│   └── Error Codes
├── SDKs & Tools
│   ├── JavaScript/Node.js
│   ├── Python
│   ├── Java
│   ├── Go
│   └── PHP
├── Resources
│   ├── Examples
│   ├── Tutorials
│   ├── FAQ
│   └── Changelog
└── Support
    ├── Troubleshooting
    ├── Community
    └── Contact
```

### QUICK START GUIDE

# Getting Started with CloudAPI

Welcome to CloudAPI! This guide will have you making your first API call in 5 minutes.

## Prerequisites

Before you begin, you'll need:

- A CloudAPI account ([sign up here](https://cloudapi.com/signup))
- Your API key ([find it here](https://cloudapi.com/dashboard/keys))
- A tool to make HTTP requests (curl, Postman, or your favorite language)

## Step 1: Get Your API Key

1. Log in to your [CloudAPI Dashboard](https://cloudapi.com/dashboard)
2. Navigate to **API Keys** in the sidebar
3. Click **Create New Key**
4. Copy your key - you'll need it for all API requests

> **🔐 Security Note**: Keep your API key secret! Never commit it to version control or share it publicly.

## Step 2: Make Your First Request

Let's start with a simple GET request to verify your setup:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.cloudapi.com/v1/status
```

**Expected Response:**

```json
{
  "status": "active",
  "version": "1.0",
  "timestamp": "2024-03-15T10:30:00Z"
}
```

✅ **Success!** If you see this response, you're ready to explore the API.

## Step 3: Create Your First Resource

Now let's create something useful. We'll create a project:

```bash
curl -X POST https://api.cloudapi.com/v1/projects \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My First Project",
    "description": "Learning CloudAPI"
  }'
```

**Response:**

```json
{
  "id": "proj_abc123",
  "name": "My First Project",
  "description": "Learning CloudAPI",
  "created_at": "2024-03-15T10:35:00Z"
}
```

## What's Next?

Great job! You've successfully:

- ✅ Authenticated with the API
- ✅ Made your first request
- ✅ Created a resource

**Ready to dive deeper?** Check out these resources:

- 📖 [API Reference](/reference) - Complete endpoint documentation
- 🚀 [Common Use Cases](/guides/use-cases) - Real-world examples
- 💡 [Best Practices](/guides/best-practices) - Tips from our team
- 🛠️ [SDKs](/sdks) - Use our official libraries

---

### API REFERENCE DOCUMENTATION

# Projects API

The Projects API allows you to create and manage projects within CloudAPI.

## The Project Object

```json
{
  "id": "proj_abc123",
  "name": "My Project",
  "description": "A sample project",
  "status": "active",
  "created_at": "2024-03-15T10:35:00Z",
  "updated_at": "2024-03-15T10:35:00Z",
  "metadata": {
    "key": "value"
  }
}
```

### Attributes

| Attribute     | Type      | Description                                     |
| ------------- | --------- | ----------------------------------------------- |
| `id`          | string    | Unique identifier for the project               |
| `name`        | string    | Project name (1-100 characters)                 |
| `description` | string    | Optional project description                    |
| `status`      | enum      | Project status: `active`, `archived`, `deleted` |
| `created_at`  | timestamp | UTC timestamp of creation                       |
| `updated_at`  | timestamp | UTC timestamp of last update                    |
| `metadata`    | object    | Custom key-value pairs for your use             |

## Endpoints

### Create a Project

```http
POST /v1/projects
```

Creates a new project with the specified parameters.

#### Request Body

```json
{
  "name": "My Project",
  "description": "Optional description",
  "metadata": {
    "team": "engineering",
    "priority": "high"
  }
}
```

#### Parameters

| Parameter     | Type   | Required | Description                    |
| ------------- | ------ | -------- | ------------------------------ |
| `name`        | string | ✓        | Project name (1-100 chars)     |
| `description` | string |          | Project description            |
| `metadata`    | object |          | Custom metadata (max 50 pairs) |

#### Example Request

<details>
<summary>cURL</summary>

```bash
curl -X POST https://api.cloudapi.com/v1/projects \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Q4 Campaign",
    "description": "Marketing campaign for Q4 2024",
    "metadata": {
      "department": "marketing",
      "budget": "50000"
    }
  }'
```

</details>

<details>
<summary>JavaScript</summary>

```javascript
const response = await fetch("https://api.cloudapi.com/v1/projects", {
  method: "POST",
  headers: {
    Authorization: "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: "Q4 Campaign",
    description: "Marketing campaign for Q4 2024",
    metadata: {
      department: "marketing",
      budget: "50000",
    },
  }),
});

const project = await response.json();
console.log(project);
```

</details>

<details>
<summary>Python</summary>

```python
import requests

response = requests.post(
    'https://api.cloudapi.com/v1/projects',
    headers={
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    },
    json={
        'name': 'Q4 Campaign',
        'description': 'Marketing campaign for Q4 2024',
        'metadata': {
            'department': 'marketing',
            'budget': '50000'
        }
    }
)

project = response.json()
print(project)
```

</details>

#### Response

```json
{
  "id": "proj_xyz789",
  "name": "Q4 Campaign",
  "description": "Marketing campaign for Q4 2024",
  "status": "active",
  "created_at": "2024-03-15T14:20:00Z",
  "updated_at": "2024-03-15T14:20:00Z",
  "metadata": {
    "department": "marketing",
    "budget": "50000"
  }
}
```

#### Error Responses

| Code | Description                 | Fix                                  |
| ---- | --------------------------- | ------------------------------------ |
| 400  | Invalid request body        | Check required fields and data types |
| 401  | Invalid API key             | Verify your API key is correct       |
| 409  | Project name already exists | Use a unique project name            |
| 429  | Rate limit exceeded         | Wait and retry with backoff          |

### List Projects

```http
GET /v1/projects
```

Returns a paginated list of your projects.

#### Query Parameters

| Parameter        | Type    | Default | Description             |
| ---------------- | ------- | ------- | ----------------------- |
| `limit`          | integer | 10      | Number of items (1-100) |
| `starting_after` | string  |         | Cursor for pagination   |
| `status`         | enum    |         | Filter by status        |
| `metadata[key]`  | string  |         | Filter by metadata      |

#### Example Request

```bash
curl -G https://api.cloudapi.com/v1/projects \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d limit=20 \
  -d status=active \
  -d "metadata[department]=marketing"
```

### USER GUIDE DOCUMENTATION

# CloudAPI User Guide

## Chapter 3: Working with Webhooks

Webhooks allow you to receive real-time notifications when events occur in CloudAPI.

### Understanding Webhooks

Think of webhooks as automated phone calls from CloudAPI to your application. When something important happens (like a project status change), we'll immediately notify your server.

**Common Use Cases:**

- 🔔 Get notified when tasks complete
- 📊 Sync data with external systems
- 🤖 Trigger automated workflows
- 📈 Track usage in real-time

### Setting Up Your First Webhook

#### Step 1: Create an Endpoint

First, you need a URL that can receive HTTP POST requests. Here's a simple example using Node.js and Express:

```javascript
const express = require("express");
const app = express();

app.use(express.json());

app.post("/webhooks/cloudapi", (req, res) => {
  const event = req.body;

  // Verify webhook signature (important!)
  const signature = req.headers["x-cloudapi-signature"];
  if (!verifySignature(signature, req.body)) {
    return res.status(401).send("Invalid signature");
  }

  // Process the event
  console.log("Received event:", event.type);

  switch (event.type) {
    case "project.created":
      handleProjectCreated(event.data);
      break;
    case "task.completed":
      handleTaskCompleted(event.data);
      break;
    // Add more event handlers
  }

  // Always respond quickly
  res.status(200).send("OK");
});

app.listen(3000);
```

#### Step 2: Register the Webhook

Navigate to your CloudAPI Dashboard:

1. Go to **Settings** → **Webhooks**
2. Click **Add Endpoint**
3. Enter your endpoint URL: `https://yourapp.com/webhooks/cloudapi`
4. Select events to subscribe to
5. Click **Create Webhook**

Or use the API:

```bash
curl -X POST https://api.cloudapi.com/v1/webhooks \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://yourapp.com/webhooks/cloudapi",
    "events": ["project.created", "task.completed"],
    "description": "Main webhook endpoint"
  }'
```

### Webhook Security

🔐 **Always verify webhook signatures!** This ensures requests actually come from CloudAPI.

```javascript
const crypto = require("crypto");

function verifySignature(signature, payload) {
  const secret = process.env.CLOUDAPI_WEBHOOK_SECRET;
  const expected = crypto
    .createHmac("sha256", secret)
    .update(JSON.stringify(payload))
    .digest("hex");

  return signature === `sha256=${expected}`;
}
```

### Event Types

| Event             | Description         | Payload Example                    |
| ----------------- | ------------------- | ---------------------------------- |
| `project.created` | New project created | `{project: {...}}`                 |
| `project.updated` | Project modified    | `{project: {...}, changes: {...}}` |
| `project.deleted` | Project removed     | `{project: {id: "..."}}`           |
| `task.completed`  | Task finished       | `{task: {...}, result: {...}}`     |

### Best Practices

✅ **Do:**

- Respond quickly (within 5 seconds)
- Process events asynchronously
- Implement retry logic
- Log all received events
- Use HTTPS endpoints only

❌ **Don't:**

- Perform long operations synchronously
- Ignore signature verification
- Assume event order
- Store sensitive data in webhooks

### Troubleshooting

**Webhook not receiving events?**

1. Check endpoint is publicly accessible
2. Verify HTTPS certificate is valid
3. Check firewall allows CloudAPI IPs
4. Review webhook logs in dashboard

**Getting duplicate events?**

We guarantee at-least-once delivery. Implement idempotency:

```javascript
const processedEvents = new Set();

function handleEvent(event) {
  if (processedEvents.has(event.id)) {
    return; // Already processed
  }

  processedEvents.add(event.id);
  // Process event...
}
```

### TUTORIAL DOCUMENTATION

# Tutorial: Building a Task Automation System

Learn how to build a complete task automation system using CloudAPI. By the end of this tutorial, you'll have a working system that automatically processes tasks based on custom rules.

## What We'll Build

A system that:

- 📥 Accepts task requests via API
- 🔄 Processes tasks automatically
- 📊 Tracks progress in real-time
- 🔔 Sends notifications on completion

**Time Required**: 45 minutes  
**Skill Level**: Intermediate  
**Prerequisites**: Basic JavaScript knowledge, CloudAPI account

## Part 1: Project Setup (10 min)

### 1.1 Initialize Your Project

```bash
mkdir task-automation
cd task-automation
npm init -y
npm install express axios dotenv
```

### 1.2 Create Project Structure

```
task-automation/
├── src/
│   ├── api/
│   │   └── client.js
│   ├── handlers/
│   │   └── taskHandler.js
│   ├── services/
│   │   └── automationService.js
│   └── index.js
├── .env
└── package.json
```

### 1.3 Configure Environment

Create `.env` file:

```env
CLOUDAPI_KEY=your_api_key_here
CLOUDAPI_WEBHOOK_SECRET=your_webhook_secret
PORT=3000
```

## Part 2: CloudAPI Integration (15 min)

### 2.1 Create API Client

**src/api/client.js:**

```javascript
const axios = require("axios");

class CloudAPIClient {
  constructor(apiKey) {
    this.client = axios.create({
      baseURL: "https://api.cloudapi.com/v1",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
    });
  }

  async createProject(name, description) {
    const response = await this.client.post("/projects", {
      name,
      description,
      metadata: { type: "automation" },
    });
    return response.data;
  }

  async createTask(projectId, taskData) {
    const response = await this.client.post("/tasks", {
      project_id: projectId,
      ...taskData,
    });
    return response.data;
  }

  async updateTaskStatus(taskId, status) {
    const response = await this.client.patch(`/tasks/${taskId}`, {
      status,
    });
    return response.data;
  }
}

module.exports = CloudAPIClient;
```

### 2.2 Implement Task Handler

**src/handlers/taskHandler.js:**

```javascript
class TaskHandler {
  constructor(apiClient, automationService) {
    this.api = apiClient;
    this.automation = automationService;
  }

  async processTask(task) {
    console.log(`Processing task: ${task.id}`);

    try {
      // Update status to processing
      await this.api.updateTaskStatus(task.id, "processing");

      // Run automation based on task type
      const result = await this.automation.execute(task);

      // Update with results
      await this.api.updateTaskStatus(task.id, "completed", {
        result,
        completed_at: new Date().toISOString(),
      });

      console.log(`Task ${task.id} completed successfully`);
    } catch (error) {
      console.error(`Task ${task.id} failed:`, error);

      await this.api.updateTaskStatus(task.id, "failed", {
        error: error.message,
      });
    }
  }
}

module.exports = TaskHandler;
```

## Part 3: Automation Logic (10 min)

### 3.1 Create Automation Service

**src/services/automationService.js:**

```javascript
class AutomationService {
  constructor() {
    this.rules = new Map();
    this.setupDefaultRules();
  }

  setupDefaultRules() {
    // Rule: Email notification
    this.rules.set("email_notification", async (task) => {
      console.log(`Sending email to: ${task.data.recipient}`);
      // Implement email logic here
      return { sent: true, timestamp: new Date() };
    });

    // Rule: Data processing
    this.rules.set("data_processing", async (task) => {
      const processed = task.data.values.map((v) => v * 2);
      return { processed, count: processed.length };
    });

    // Rule: External API call
    this.rules.set("api_integration", async (task) => {
      // Make external API call
      const response = await fetch(task.data.endpoint);
      return await response.json();
    });
  }

  async execute(task) {
    const rule = this.rules.get(task.type);

    if (!rule) {
      throw new Error(`No rule found for task type: ${task.type}`);
    }

    return await rule(task);
  }

  addRule(type, handler) {
    this.rules.set(type, handler);
  }
}

module.exports = AutomationService;
```

## Part 4: Web Server & Webhooks (10 min)

### 4.1 Create Express Server

**src/index.js:**

```javascript
require("dotenv").config();
const express = require("express");
const CloudAPIClient = require("./api/client");
const TaskHandler = require("./handlers/taskHandler");
const AutomationService = require("./services/automationService");

const app = express();
app.use(express.json());

// Initialize services
const apiClient = new CloudAPIClient(process.env.CLOUDAPI_KEY);
const automationService = new AutomationService();
const taskHandler = new TaskHandler(apiClient, automationService);

// Health check
app.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date() });
});

// Webhook endpoint
app.post("/webhooks/cloudapi", async (req, res) => {
  // Verify signature (implement based on security section)

  const event = req.body;
  console.log(`Received event: ${event.type}`);

  // Handle different event types
  switch (event.type) {
    case "task.created":
      // Process new task asynchronously
      setImmediate(() => {
        taskHandler.processTask(event.data.task);
      });
      break;
  }

  res.status(200).send("OK");
});

// Create new automation task
app.post("/automate", async (req, res) => {
  try {
    const { type, data } = req.body;

    // Create task in CloudAPI
    const task = await apiClient.createTask(projectId, {
      type,
      data,
      status: "pending",
    });

    res.json({
      message: "Task created",
      task_id: task.id,
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## Part 5: Testing & Deployment

### 5.1 Test Locally

1. Start your server:

```bash
npm start
```

2. Create a test task:

```bash
curl -X POST http://localhost:3000/automate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "email_notification",
    "data": {
      "recipient": "user@example.com",
      "subject": "Test Notification"
    }
  }'
```

### 5.2 Deploy to Production

1. Deploy to your hosting service
2. Update webhook URL in CloudAPI dashboard
3. Set environment variables
4. Enable HTTPS

## Next Steps

Congratulations! You've built a working task automation system. Here are some ideas to extend it:

- 🔧 Add more automation rules
- 📊 Build a dashboard to monitor tasks
- 🔄 Implement retry logic for failed tasks
- 📱 Add Slack/Discord notifications
- 🗄️ Store results in a database

## Complete Code

Find the complete working code at: [github.com/cloudapi/tutorials/task-automation](https://github.com/cloudapi/tutorials)

### TROUBLESHOOTING GUIDE

# Troubleshooting CloudAPI

## Common Issues and Solutions

### Authentication Errors

#### Error: "Invalid API Key"

```json
{
  "error": {
    "code": "invalid_api_key",
    "message": "The provided API key is invalid"
  }
}
```

**Possible Causes:**

1. API key is incorrect
2. Key has been revoked
3. Missing "Bearer" prefix

**Solutions:**
✅ Verify your API key in the dashboard  
✅ Ensure format: `Authorization: Bearer YOUR_KEY`  
✅ Check for extra spaces or newlines  
✅ Generate a new key if needed

**Debug Steps:**

```bash
# Test your API key
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.cloudapi.com/v1/status

# Should return:
# {"status": "active", ...}
```

### Rate Limiting

#### Error: "Rate Limit Exceeded"

```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Too many requests",
    "retry_after": 60
  }
}
```

**Understanding Rate Limits:**

- **Free tier**: 100 requests/minute
- **Pro tier**: 1000 requests/minute
- **Enterprise**: Custom limits

**Solutions:**
✅ Implement exponential backoff  
✅ Cache responses when possible  
✅ Batch operations  
✅ Upgrade your plan

**Retry Logic Example:**

```javascript
async function makeRequestWithRetry(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.response?.status === 429) {
        const retryAfter = error.response.headers["retry-after"] || 60;
        console.log(`Rate limited. Waiting ${retryAfter}s...`);
        await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));
      } else {
        throw error;
      }
    }
  }
}
```

### Webhook Issues

#### Webhooks Not Receiving Events

**Diagnostic Checklist:**

- [ ] Endpoint is publicly accessible
- [ ] Using HTTPS with valid certificate
- [ ] Responding within 5 seconds
- [ ] Returning 200 status code
- [ ] Webhook is active in dashboard

**Test Your Endpoint:**

```bash
# From external server
curl -X POST https://yourapp.com/webhooks/cloudapi \
  -H "Content-Type: application/json" \
  -d '{"test": true}'
```

**Common Fixes:**

1. **Firewall blocking CloudAPI IPs**
   - Whitelist: `52.89.214.238/32`, `34.212.75.30/32`

2. **SSL certificate issues**
   - Use Let's Encrypt for free certificates
   - Check with: `openssl s_client -connect yourapp.com:443`

3. **Timeout issues**
   - Process events asynchronously
   - Return 200 immediately

### SDK/Library Issues

#### Version Conflicts

**Error**: "Module version mismatch"

**Solution**:

```bash
# JavaScript
npm update @cloudapi/sdk

# Python
pip install --upgrade cloudapi

# Check versions
npm list @cloudapi/sdk
pip show cloudapi
```

### Performance Issues

#### Slow API Responses

**Optimization Strategies:**

1. **Use Pagination**

```javascript
// Bad: Getting all at once
const allProjects = await api.getProjects({ limit: 1000 });

// Good: Paginate
let projects = [];
let hasMore = true;
let cursor = null;

while (hasMore) {
  const page = await api.getProjects({
    limit: 100,
    starting_after: cursor,
  });
  projects = projects.concat(page.data);
  hasMore = page.has_more;
  cursor = page.data[page.data.length - 1]?.id;
}
```

2. **Parallel Requests**

```javascript
// Bad: Sequential
for (const id of projectIds) {
  const project = await api.getProject(id);
  projects.push(project);
}

// Good: Parallel
const projects = await Promise.all(projectIds.map((id) => api.getProject(id)));
```

### Data Issues

#### Malformed Request Body

**Error**: "Invalid request body"

**Common Causes:**

- Missing required fields
- Incorrect data types
- Invalid enum values
- Exceeding size limits

**Validation Example:**

```javascript
function validateProjectData(data) {
  const errors = [];

  if (!data.name || data.name.length > 100) {
    errors.push("Name must be 1-100 characters");
  }

  if (data.metadata && Object.keys(data.metadata).length > 50) {
    errors.push("Metadata limited to 50 key-value pairs");
  }

  if (errors.length > 0) {
    throw new Error(`Validation failed: ${errors.join(", ")}`);
  }
}
```

### Getting Help

If you're still stuck:

1. **Check the Status Page**: [status.cloudapi.com](https://status.cloudapi.com)
2. **Search Documentation**: Use the search bar above
3. **Community Forum**: [community.cloudapi.com](https://community.cloudapi.com)
4. **Support Ticket**: Email support@cloudapi.com with:
   - Request ID from headers
   - Full error message
   - Code snippet
   - Steps to reproduce

### DEBUG MODE

Enable detailed logging:

```javascript
// JavaScript SDK
const api = new CloudAPI({
  apiKey: process.env.CLOUDAPI_KEY,
  debug: true // Enables detailed logging
});

// Direct API calls
curl -v -H "Authorization: Bearer YOUR_KEY" \
  https://api.cloudapi.com/v1/projects
```

## Usage Instructions

1. Start with clear understanding of documentation goals and audience
2. Create comprehensive information architecture before writing
3. Use progressive disclosure - basic to advanced
4. Include abundant examples and visuals
5. Test documentation with real users
6. Maintain consistency in terminology and style
7. Keep documentation in sync with product changes
8. Measure documentation effectiveness with analytics

## Examples

### Example 1: API Documentation

**Input**:

```
{{documentation_type}}: REST API reference
{{target_audience}}: Backend developers
{{technical_level}}: Intermediate to advanced
{{product}}: Payment processing API
{{documentation_goals}}: Complete reference with examples
```

**Output**: [Comprehensive API documentation with endpoints, parameters, examples in multiple languages, error handling, and rate limiting information]

### Example 2: User Guide

**Input**:

```
{{documentation_type}}: End-user guide
{{target_audience}}: Non-technical business users
{{technical_level}}: Novice
{{product}}: CRM software
{{documentation_goals}}: Onboarding and daily tasks
```

**Output**: [Step-by-step guide with screenshots, task-oriented sections, troubleshooting tips, and glossary of terms]

## Related Prompts

- [Technical Writing Expert](/prompts/creation/technical-writing-expert.md)
- [API Design Specialist](/prompts/technical/api-design-specialist.md)
- [User Experience Writer](/prompts/creation/ux-writer.md)

## Research Notes

- Combines technical accuracy with user empathy
- Emphasizes findability and searchability
- Includes multiple learning modalities (text, code, visuals)
- Supports both learning and reference use cases
- Maintains documentation as living product asset
