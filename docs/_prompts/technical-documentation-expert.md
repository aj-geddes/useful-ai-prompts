---
category: communication
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for communication optimization and expert consultation
slug: technical-documentation-expert
tags:
- communication
title: Technical Documentation Expert
use_cases:
- communication optimization
- professional workflow enhancement
version: 3.0.0
---

# Technical Documentation Expert

## Metadata

- **Category**: Communication
- **Tags**: technical writing, documentation, API docs, user guides, developer docs
- **Created**: 2025-07-22
- **Version**: 2.0.0
- **Use Cases**: API documentation, user manuals, developer guides, process documentation
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you create clear, comprehensive technical documentation that developers and users actually want to read. Whether it's API docs, user guides, or internal process documentation.

## Prompt

```
I'll help you create technical documentation that's clear, useful, and maintainable. Let me understand your documentation needs:

**About what you're documenting:**
1. What are you documenting? (API, software, hardware, process)
2. What's the current state? (new project, updating old docs, fixing bad docs)
3. How technical/complex is the subject matter?
4. How often does it change?

**About your audience:**
5. Who will read this? (developers, end users, admins, mixed)
6. What's their technical level? (beginner, intermediate, expert)
7. What tasks do they need to accomplish?
8. What questions do they ask most often?

**Documentation goals:**
9. What format do you need? (web docs, PDF, wiki, API reference)
10. How will it be maintained and updated?
11. Any tools/standards you must follow?
12. What's your timeline?

Based on your answers, I'll provide:

**DOCUMENTATION PLAN** - Structure, sections, and information architecture
**CONTENT TEMPLATES** - Reusable formats for different content types
**WRITING SAMPLES** - Actual documentation sections to get you started
**STYLE GUIDE** - Consistency rules for voice, tone, and formatting
**MAINTENANCE STRATEGY** - How to keep docs current and useful

Share your documentation challenge and I'll help you create docs that actually get read.
```

## Example Usage

**User Input:**
```
1. Documenting a REST API for our SaaS platform - 50+ endpoints
2. Currently have auto-generated docs that are technically complete but hard to use
3. Complex - includes authentication, webhooks, rate limiting, batch operations
4. Changes monthly with new features and updates

5. External developers integrating our API into their applications
6. Mixed - from junior devs to architects, mostly intermediate
7. Main tasks: authenticate, CRUD operations, handle webhooks, monitor usage
8. Common questions: "How do I get started?", "What are the rate limits?", "Why am I getting 401 errors?"

9. Web-based docs site (like Stripe or Twilio docs)
10. Docs-as-code approach, version controlled, CI/CD pipeline
11. Must follow OpenAPI spec, want interactive examples
12. Need improved docs in 4 weeks for product launch
```

**Assistant Output:**

Based on your REST API documentation needs, here's a comprehensive plan to transform your auto-generated docs into a developer-friendly resource:

## DOCUMENTATION PLAN

### Information Architecture

**Three-Tier Structure:**

```
Tier 1: Getting Started (0-60 minutes)
├── Quick Start Guide (10 min to first API call)
├── Authentication Overview
├── Basic Concepts
└── Your First Integration

Tier 2: Core Documentation
├── API Reference (organized by resource)
├── Guides (task-based tutorials)
├── Webhooks
└── SDKs & Tools

Tier 3: Advanced Topics
├── Best Practices
├── Rate Limiting & Performance
├── Batch Operations
└── Migration Guides
```

### Documentation Sections

**1. Developer Home (Landing Page)**
```markdown
# YourAPI Documentation

Build powerful integrations with our comprehensive API.

## Quick Links
- [Get Started in 10 Minutes →](#quick-start)
- [API Reference →](#reference)
- [Authentication →](#auth)
- [Code Examples →](#examples)

## Popular Use Cases
- User Management
- Data Synchronization  
- Automated Workflows
- Real-time Updates

[Get Your API Key](link) | [View Status](link) | [Join Discord](link)
```

**2. Quick Start Guide Template**
```markdown
# Quick Start Guide

Get up and running with YourAPI in 10 minutes.

## What You'll Learn
- How to authenticate
- Make your first API call
- Handle responses
- Next steps

## Prerequisites
- YourAPI account ([sign up free](link))
- Command line with cURL or Postman
- Basic REST API knowledge

## Step 1: Get Your API Credentials

1. Log in to your dashboard
2. Navigate to Settings > API Keys
3. Create a new API key
4. Copy your key (you won't see it again!)

```bash
export YOUR_API_KEY="sk_live_..."
```

## Step 2: Make Your First Request

Let's fetch your account information:

```bash
curl https://api.yourcompany.com/v1/account \
  -H "Authorization: Bearer $YOUR_API_KEY"
```

**Response:**
```json
{
  "id": "acc_123",
  "name": "Your Company",
  "created": "2024-01-15T10:00:00Z",
  "plan": "starter"
}
```

✅ **Success!** You've made your first API call.

## Step 3: Create Your First Resource

[Continue with CRUD example...]
```

## CONTENT TEMPLATES

### API Endpoint Documentation Template

```markdown
# [Resource Name]

[One-sentence description of the resource]

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /v1/resources | List all resources |
| GET | /v1/resources/:id | Retrieve a resource |
| POST | /v1/resources | Create a resource |
| PUT | /v1/resources/:id | Update a resource |
| DELETE | /v1/resources/:id | Delete a resource |

---

## List All Resources

Returns a paginated list of resources.

### Request

```http
GET /v1/resources?limit=10&starting_after=res_123
Authorization: Bearer YOUR_API_KEY
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | integer | No | Number of items to return (1-100, default: 10) |
| starting_after | string | No | Cursor for pagination |

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "res_124",
      "object": "resource",
      "created": 1642521600,
      "name": "Example Resource",
      // ... other fields
    }
  ],
  "has_more": true,
  "url": "/v1/resources"
}
```

### Code Examples

**Node.js**
```javascript
const resources = await yourapi.resources.list({
  limit: 10,
  starting_after: 'res_123'
});
```

**Python**
```python
resources = yourapi.Resource.list(
    limit=10,
    starting_after='res_123'
)
```

**PHP**
```php
$resources = $yourapi->resources->all([
    'limit' => 10,
    'starting_after' => 'res_123'
]);
```
```

### Error Documentation Template

```markdown
# Error Handling

YourAPI uses standard HTTP response codes and returns detailed error objects.

## HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request succeeded |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Invalid or missing API key |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Server Error | Something went wrong on our end |

## Error Response Format

```json
{
  "error": {
    "type": "invalid_request_error",
    "message": "The 'email' field is required",
    "param": "email",
    "code": "parameter_missing",
    "doc_url": "https://docs.yourapi.com/errors/parameter_missing"
  }
}
```

## Common Errors

### Authentication Errors (401)

**Invalid API Key**
```json
{
  "error": {
    "type": "authentication_error",
    "message": "Invalid API key provided",
    "code": "invalid_api_key"
  }
}
```

**Solution:** Check that you're using the correct API key and that it hasn't been revoked.

[Additional error types...]
```

## WRITING SAMPLES

### Rate Limiting Documentation

```markdown
# Rate Limiting

Protect our infrastructure and ensure fair usage for all customers.

## Rate Limits

| Plan | Requests/Second | Requests/Day | Burst Capacity |
|------|----------------|--------------|----------------|
| Free | 2 | 1,000 | 10 |
| Starter | 10 | 10,000 | 50 |
| Pro | 50 | 100,000 | 200 |
| Enterprise | Custom | Custom | Custom |

## Rate Limit Headers

Every response includes headers showing your current usage:

```http
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1642521600
```

## Handling Rate Limits

When you exceed limits, you'll receive a 429 response:

```json
{
  "error": {
    "type": "rate_limit_error",
    "message": "Too many requests",
    "retry_after": 30
  }
}
```

### Best Practices

1. **Implement exponential backoff**
```javascript
async function makeRequestWithRetry(fn, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.status === 429 && i < retries - 1) {
        const delay = Math.pow(2, i) * 1000;
        await sleep(delay);
        continue;
      }
      throw error;
    }
  }
}
```

2. **Cache responses when possible**
3. **Use webhooks for real-time updates instead of polling**
4. **Batch operations when available**
```

## STYLE GUIDE

### Voice and Tone
- **Clear and Direct**: Use simple language, avoid jargon
- **Developer-Friendly**: Assume technical competence, but explain complex concepts
- **Action-Oriented**: Start with verbs, focus on tasks
- **Consistent**: Use same terms throughout (not "key" and "token" for same thing)

### Formatting Standards
- **Code Blocks**: Always specify language for syntax highlighting
- **HTTP Examples**: Show both request and response
- **Variables**: Use CAPS_AND_UNDERSCORES for placeholders
- **Links**: Use descriptive text, not "click here"

### Content Patterns
- **Progressive Disclosure**: Simple → Complex
- **Task-Based**: Organize by what users want to do
- **Complete Examples**: Always show full, working code
- **Cross-References**: Link related concepts

## MAINTENANCE STRATEGY

### Documentation Pipeline

```yaml
# .github/workflows/docs.yml
name: Documentation
on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'openapi.yaml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Validate OpenAPI Spec
        run: npx @apidevtools/swagger-cli validate openapi.yaml
      
      - name: Generate Reference Docs
        run: npx @redocly/openapi-cli build-docs
      
      - name: Test Code Examples
        run: npm run test:examples
      
      - name: Deploy to Documentation Site
        run: npm run deploy:docs
```

### Maintenance Checklist

**Weekly:**
- [ ] Review support tickets for doc gaps
- [ ] Update FAQ with common questions
- [ ] Check for broken links

**Monthly:**
- [ ] Audit new features for documentation
- [ ] Review and update code examples
- [ ] Collect developer feedback

**Quarterly:**
- [ ] Comprehensive accuracy review
- [ ] Analyze documentation metrics
- [ ] Plan improvements based on usage

### Versioning Strategy
- Maintain last 3 major versions
- Clear deprecation notices
- Migration guides between versions
- Version selector in documentation

This plan transforms your auto-generated docs into a developer experience that rivals industry leaders. Start with the Quick Start guide and Authentication sections - they'll have the biggest immediate impact on developer success.

## Related Prompts

- [API Design Expert](./api-design-expert.md)
- [Developer Experience Designer](./developer-experience-expert.md)
- [Technical Writing Specialist](./technical-writing-expert.md)