---
name: user-story-writing
description: >
  Write effective user stories that capture requirements from the user's
  perspective. Create clear stories with detailed acceptance criteria to guide
  development and define done.
---

# User Story Writing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Well-written user stories communicate requirements in a user-focused way, facilitate discussion, and provide clear acceptance criteria for developers and testers.

## When to Use

- Breaking down requirements into development tasks
- Product backlog creation and refinement
- Agile sprint planning
- Communicating features to development team
- Defining acceptance criteria
- Creating test cases

## Quick Start

Minimal working example:

```markdown
# User Story Template

**Title:** [Feature name]

**As a** [user role/persona]
**I want to** [action/capability]
**So that** [business value/benefit]

---

## User Context

- User Role: [Who is performing this action?]
- User Goals: [What are they trying to accomplish?]
- Use Case: [When do they perform this action?]

---

## Acceptance Criteria

Given [precondition]
When [action]
Then [expected result]

Example:
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Story Refinement Process](references/story-refinement-process.md) | Story Refinement Process |
| [Acceptance Criteria Examples](references/acceptance-criteria-examples.md) | Acceptance Criteria Examples |
| [Story Splitting](references/story-splitting.md) | Story Splitting |
| [Story Estimation](references/story-estimation.md) | Story Estimation |

## Best Practices

### ✅ DO

- Write from the user's perspective
- Focus on value, not implementation
- Create stories small enough for one sprint
- Define clear acceptance criteria
- Use consistent format and terminology
- Have product owner approve stories
- Include edge cases and error scenarios
- Link to requirements/business goals
- Update stories based on learning
- Create testable stories

### ❌ DON'T

- Write technical task-focused stories
- Create overly detailed specifications
- Write stories that require multiple sprints
- Forget about non-functional requirements
- Skip acceptance criteria
- Create dependent stories unnecessarily
- Write ambiguous acceptance criteria
- Ignore edge cases
- Create too large stories
- Change stories mid-sprint without discussion
