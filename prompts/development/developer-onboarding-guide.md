# Developer Onboarding Guide

## Metadata
- **ID**: `development-developer-onboarding-guide`
- **Version**: 1.0.0
- **Category**: Development
- **Tags**: onboarding, developer-experience, documentation, team-culture, setup-guide, new-hire
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-27
- **Updated**: 2026-02-27

## Overview

Creates comprehensive developer onboarding documentation and plans that get new engineers productive within days, not weeks. Covers environment setup, codebase orientation, team processes, and first-contribution paths — tailored to the team's specific stack, culture, and complexity level.

## When to Use

**Ideal Scenarios:**
- Onboarding a new engineer joining the team
- Rebuilding outdated onboarding documentation that nobody maintains
- Standardizing onboarding after rapid team growth
- Creating a 30-60-90 day plan for a new developer

**Anti-patterns (Don't Use For):**
- Non-technical staff onboarding (different scope)
- Security clearance or HR compliance onboarding
- Role-specific training (data science, ML — specialized track needed)

---

## Prompt

```
<role>
You are a developer experience (DX) specialist with 10+ years of experience designing onboarding programs for engineering teams. You understand that the first 2 weeks determine whether a new hire becomes productive quickly or spends months frustrated. You create documentation that is scannable, complete, and actually maintained.
</role>

<context>
Poor onboarding costs months of reduced productivity, increases early attrition, and forces senior engineers to repeatedly answer the same questions. Great onboarding transforms new hires into contributors within their first sprint.
</context>

<input_handling>
Required inputs:
- Technology stack (languages, frameworks, key tools)
- Team size and structure
- Key processes (Git workflow, deployment, code review practices)

Optional inputs (will infer if not provided):
- Experience level of new hire: assume mid-level engineer
- Onboarding timeline: aim for productive first PR within week 1
- Remote vs. on-site: assume hybrid/remote
</input_handling>

<task>
Produce a complete onboarding guide and 30-day plan.

Step 1: Design the setup experience
- Local environment setup (prerequisites, installation, configuration)
- Verification steps to confirm setup works
- Common setup problems and fixes

Step 2: Map codebase orientation
- Repository structure with purpose of each major directory
- Architecture overview (just enough to navigate, not everything)
- Key files and entry points
- Where to find what (logging, config, tests, docs)

Step 3: Document team processes
- Git workflow (branching, PR, review, merge)
- How to deploy (staging and production)
- Communication channels and when to use them
- Meeting cadence and expected participation

Step 4: Create the first-week plan
- Day 1: Setup + orient
- Day 2-3: Explore codebase with guided tasks
- Day 4-5: First contribution (low-risk issue or documentation PR)

Step 5: Define 30-60-90 day milestones
- 30 days: Independently completing assigned tasks
- 60 days: Driving small features end-to-end
- 90 days: Contributing to architectural decisions
</task>

<output_specification>
Format: Structured onboarding guide in markdown
Length: 600-1000 words
Include:
- Environment setup checklist (numbered steps)
- Codebase map (directory structure with descriptions)
- Day-by-day first week plan
- 30-60-90 day milestones
- "Who to ask" directory
</output_specification>

<quality_criteria>
Excellent onboarding guides:
- New hire can complete setup without asking for help
- First PR opened by end of week 1
- Every "where is X?" question is answered
- Maintained by the team (not a one-time artifact)

Avoid:
- Assuming knowledge of internal tooling
- Out-of-date setup steps (add "last verified: date" to each section)
- Missing error recovery (what to do when step fails)
- Overwhelming with everything at once
</quality_criteria>

<constraints>
- Every setup step must include a verification command
- Include "who to ask" for each major knowledge area
- Note which sections need updating when the stack changes
</constraints>
```

---

## Example Usage

### Input
"We need an onboarding guide for our Node.js/React/PostgreSQL SaaS team. 8 engineers total. We use GitHub Flow, deploy to AWS ECS, review PRs within 24 hours. New hires often spend 3 days just trying to get the app running locally."

### Output

**Developer Onboarding Guide — SaaS Engineering Team**
*Last verified: 2026-02-27 | Update owner: @team-lead*

---

**Welcome**

You'll be committing code by end of week 1. This guide covers everything from getting your machine set up to shipping your first PR.

**Who to Ask**
| Topic | Person | Channel |
|-------|--------|---------|
| Local setup problems | Any team member | #dev-help |
| Architecture questions | Tech Lead | DM or #architecture |
| Product/business context | Engineering Manager | 1:1 |
| AWS/deployment | DevOps Lead | #infrastructure |

---

**Environment Setup** *(~2 hours)*

**Prerequisites**
```bash
# Verify Node.js 20+
node --version  # Should show v20.x

# Install if missing:
curl -fsSL https://fnm.vercel.app/install | bash
fnm install 20 && fnm use 20
```

**Clone and Install**
```bash
git clone https://github.com/yourorg/saas-app.git
cd saas-app
cp .env.example .env.local  # Get values from 1Password → "Dev Environment" vault
npm install
```

**Database Setup**
```bash
# Install PostgreSQL 15 via Homebrew (Mac) or apt (Linux)
brew install postgresql@15

# Create local database
createdb saas_development
npm run db:migrate
npm run db:seed

# Verify:
npm run db:test-connection  # Should print: "✓ Connected to saas_development"
```

**Start the App**
```bash
npm run dev  # Starts API on :3001 and React on :3000
# Open http://localhost:3000 — you should see the login screen
# Login: dev@test.com / password123 (seed data)
```

**Common Setup Issues**
- *Port 5432 already in use*: `brew services stop postgresql` then restart
- *Module not found errors*: `rm -rf node_modules && npm install`
- *Database connection refused*: Ensure `PGPORT=5432` in `.env.local`

---

**Codebase Map**
```
saas-app/
├── packages/
│   ├── api/          # Express.js REST API
│   │   ├── routes/   # Route handlers (entry: server.js)
│   │   ├── services/ # Business logic (no DB calls here)
│   │   └── models/   # Database models (Knex.js)
│   └── web/          # React frontend (Vite)
│       ├── src/
│       │   ├── pages/      # One file per route
│       │   ├── components/ # Shared UI components
│       │   └── api/        # API client hooks
├── migrations/       # Database migrations (run with npm run db:migrate)
└── scripts/          # Dev utilities
```

---

**Week 1 Plan**

**Day 1: Setup + Orient**
- [ ] Complete environment setup (above)
- [ ] Read this guide fully
- [ ] Meet with Engineering Manager (1:1 scheduled for you)
- [ ] Join Slack channels: #dev-general, #dev-help, #deployments, #incidents

**Day 2: Explore the Codebase**
- [ ] Follow a request from frontend to database: pick any API call in the browser DevTools network tab and trace it through `web/src/api/` → `api/routes/` → `api/services/` → `api/models/`
- [ ] Run the full test suite: `npm test` (should be green)
- [ ] Read the last 5 merged PRs to understand code style and review culture

**Day 3-4: First Issue**
- Pick a "good first issue" label from GitHub Issues
- Create a feature branch: `git checkout -b feature/TICKET-XX-description`
- Make the change, write a test

**Day 5: First PR**
- Open a PR with your changes
- The team reviews within 24 hours
- Goal: have it merged by end of week 1

---

**30-60-90 Day Milestones**

| Period | Target |
|--------|--------|
| 30 days | Completing assigned tasks independently, familiar with full stack |
| 60 days | Driving small features end-to-end with minimal guidance |
| 90 days | Contributing to sprint planning, proposing architectural improvements |

---

## Variations

- **Remote-first version**: Add async communication expectations, documentation culture, timezone overlap guidance
- **Senior hire version**: Shortened setup + deeper architecture discussion, stakeholder map, first 90 days leadership expectations
- **Internship version**: More structured daily tasks, clear mentorship pairing, explicit learning goals

## Related Prompts

- [Technical Documentation Writer](documentation-writer.md) - Creating the underlying codebase docs
- [Git Workflow Advisor](git-workflow-advisor.md) - The branching strategy referenced in this guide
