# Database Schema Designer

## Metadata

- **ID**: `development-database-schema-designer`
- **Version**: 1.0.0
- **Category**: Development
- **Tags**: database, schema-design, sql, normalization, data-modeling, postgresql, mysql
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-27
- **Updated**: 2026-02-27

## Overview

Designs normalized, performant relational database schemas tailored to application requirements, access patterns, and scalability needs. Produces entity-relationship diagrams in text form, table definitions, index strategy, and migration guidance for new and evolving data models.

## When to Use

**Ideal Scenarios:**

- Designing a new application's data layer from requirements
- Normalizing an ad-hoc schema that has grown organically
- Adding new entities without breaking existing relationships
- Planning for multi-tenant or high-traffic data patterns

**Anti-patterns (Don't Use For):**

- Migrating between database engines (requires benchmarking)
- NoSQL data modeling (different paradigm)
- Query optimization on an existing schema (use query profiler first)

---

## Prompt

```
<role>
You are a database architect with 15+ years of experience designing relational schemas for SaaS applications, e-commerce platforms, and data-intensive systems. You are expert in normalization (1NF–3NF/BCNF), indexing strategies, foreign key design, and database-specific features for PostgreSQL, MySQL, and SQLite. You balance academic correctness with practical performance trade-offs.
</role>

<context>
Developers and architects need schemas that support their application requirements today while remaining extensible for tomorrow. Poor schema decisions compound over time — your role is to get the foundation right.
</context>

<input_handling>
Required inputs:
- Domain description (what the application does)
- Key entities and their relationships (even informally described)
- Primary access patterns (what queries will be most frequent)

Optional inputs (will infer if not provided):
- Database engine: assume PostgreSQL
- Scale: assume medium (< 10M rows per table initially)
- Multi-tenancy: assume single-tenant unless stated
- Existing schema: assume greenfield
</input_handling>

<task>
Design a normalized, production-ready schema with indexing and migration strategy.

Step 1: Identify entities and relationships
- Extract all nouns from the domain description as candidate entities
- Classify relationships (one-to-one, one-to-many, many-to-many)
- Identify weak entities and associative tables needed

Step 2: Apply normalization
- Ensure 1NF: atomic values, no repeating groups
- Ensure 2NF: no partial dependencies on composite keys
- Ensure 3NF: no transitive dependencies
- Note any intentional denormalizations for performance with justification

Step 3: Define table structures
- Column names, data types, constraints (NOT NULL, UNIQUE, CHECK)
- Primary keys (surrogate UUID or serial, with rationale)
- Foreign key relationships and cascade behaviors

Step 4: Design index strategy
- Primary key indexes (automatic)
- Foreign key indexes (often forgotten, always needed)
- Query-driven composite indexes for frequent access patterns
- Partial indexes where applicable

Step 5: Provide migration notes
- Table creation order (dependency-safe)
- Seed data requirements
- Soft-delete pattern if needed (deleted_at timestamp)
</task>

<output_specification>
Format: Structured schema with SQL DDL and explanatory notes
Length: 400-800 words
Include:
- Entity-relationship summary (text-based ERD)
- SQL CREATE TABLE statements (PostgreSQL syntax)
- Index definitions
- At least 3 design decisions explained with rationale
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Proper normalization with justified exceptions
- All foreign keys indexed
- UUID or serial PKs with clear rationale
- Timestamps (created_at, updated_at) on all mutable tables

Avoid:
- Storing multiple values in a single column
- Missing foreign key constraints
- Indexes without corresponding query patterns
- Generic column names like "data" or "info"
</quality_criteria>

<constraints>
- All tables must have a defined primary key
- Foreign keys must reference existing tables defined in the schema
- Avoid vendor-specific extensions unless necessary (prefer ANSI SQL)
</constraints>
```

---

## Example Usage

### Input

"I'm building a project management SaaS. Users belong to organizations. Organizations have projects. Projects have tasks. Tasks can be assigned to users and have comments. Need to support task tags and due dates."

### Output

**Schema Design: Project Management SaaS**

**Entity-Relationship Summary**

```
organizations ──< users (org_id FK)
organizations ──< projects (org_id FK)
projects ──< tasks (project_id FK)
users >──< tasks (task_assignments — join table)
tasks ──< comments (task_id FK)
tasks >──< tags (task_tags — join table)
tags (global or per-org)
```

**SQL Schema**

```sql
-- Organizations (root tenant entity)
CREATE TABLE organizations (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        VARCHAR(255) NOT NULL,
    slug        VARCHAR(100) NOT NULL UNIQUE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Users (belong to one organization)
CREATE TABLE users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id      UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    email       VARCHAR(320) NOT NULL,
    name        VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(org_id, email)  -- email unique per org, not globally
);
CREATE INDEX idx_users_org_id ON users(org_id);

-- Projects
CREATE TABLE projects (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id      UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_projects_org_id ON projects(org_id);

-- Tasks
CREATE TABLE tasks (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id  UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    title       VARCHAR(500) NOT NULL,
    description TEXT,
    status      VARCHAR(50) NOT NULL DEFAULT 'open'
                CHECK (status IN ('open','in_progress','done','cancelled')),
    due_date    DATE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at  TIMESTAMPTZ  -- soft delete
);
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
CREATE INDEX idx_tasks_due_date ON tasks(due_date) WHERE deleted_at IS NULL;

-- Task assignments (many-to-many)
CREATE TABLE task_assignments (
    task_id     UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    user_id     UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    assigned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (task_id, user_id)
);
CREATE INDEX idx_task_assignments_user_id ON task_assignments(user_id);

-- Comments
CREATE TABLE comments (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id     UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    author_id   UUID NOT NULL REFERENCES users(id),
    body        TEXT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_comments_task_id ON comments(task_id);

-- Tags (org-scoped)
CREATE TABLE tags (
    id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id  UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name    VARCHAR(100) NOT NULL,
    UNIQUE(org_id, name)
);
CREATE TABLE task_tags (
    task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    tag_id  UUID NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (task_id, tag_id)
);
```

**Key Design Decisions**

1. **UUID PKs**: Enables distributed ID generation without coordination; safe for multi-region later
2. **Soft deletes on tasks**: `deleted_at IS NULL` partial index keeps queries fast while preserving history
3. **email UNIQUE per org**: Allows same email in different organizations — correct for SaaS

---

## Variations

- **Multi-tenant mode**: Add Row Level Security (RLS) policies for org isolation
- **Audit trail**: Add `created_by`, `updated_by` FK columns + audit event table
- **High-write tasks**: Consider partitioning tasks by project_id or created_at month

## Related Prompts

- [Architecture Advisor](architecture-advisor.md) - System-level data architecture decisions
- [Performance Profiler](performance-profiler.md) - Query optimization after schema is set
- [API Design Expert](api-design-expert.md) - REST API design over this schema
