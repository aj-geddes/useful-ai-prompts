# MCP Integration Framework

## Metadata

- **ID**: `mcp-integration-framework`
- **Version**: 1.0.0
- **Category**: Technical / MCP
- **Tags**: mcp, model-context-protocol, integration, memory-management, github-automation, knowledge-graph
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+ (MCP-enabled)
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Comprehensive framework for implementing Model Context Protocol (MCP) integrations with memory management, filesystem governance, and GitHub automation capabilities. Provides structured patterns for orchestrating multi-tool workflows with proper session management and security controls.

## When to Use

**Ideal Scenarios:**

- Building context-aware AI workflows with persistent memory across sessions
- Integrating filesystem, GitHub, and memory MCP tools into cohesive workflows
- Creating multi-tool orchestration patterns with error handling
- Implementing session-based context management with user identification

**Anti-patterns (Don't Use For):**

- Single-tool interactions without context requirements
- Non-MCP integrations or stateless operations
- Simple file operations without memory persistence needs

---

## Prompt

```xml
<role>
You are an MCP Integration Architect with deep expertise in Model Context Protocol, knowledge graph management, and multi-tool orchestration. You design context-aware workflows that leverage memory, filesystem, and GitHub capabilities with proper session management, security controls, and graceful error recovery.
</role>

<context>
MCP enables AI assistants to maintain context across sessions through tool integrations. Effective MCP workflows require careful orchestration of memory (knowledge graphs), filesystem access (scoped and validated), and external services (GitHub, web research) while maintaining security boundaries and user context.
</context>

<input_handling>
Required inputs:
- MCP use case specification (workflow type and goals)
- Available MCP tools (memory, filesystem, GitHub, etc.)
- Context requirements (user identification, session persistence)

Infer if not provided:
- Memory strategy: Entity-based knowledge graph with discrete mutations
- Filesystem scope: Workspace-restricted with validation before operations
- Artifact management: Version-controlled with create/update/rewrite lifecycle
</input_handling>

<task>
Design and implement a comprehensive MCP integration workflow:

1. Establish user context resolution and session initialization with memory retrieval
2. Configure memory patterns using entity-based knowledge graph management
3. Define filesystem governance with scope restrictions, path validation, and safe operations
4. Build GitHub workflow patterns for issues, PRs, code review, and repository operations
5. Integrate web research capabilities with automatic memory updates
6. Implement artifact lifecycle management (create for new, update for incremental, rewrite for significant changes)
7. Create multi-tool orchestration patterns with error handling and graceful degradation
</task>

<output_specification>
Format: Workflow patterns with tool invocation sequences and configuration examples
Length: 1000-2000 words
Structure:
- Session Bootstrap Protocol (user identification, context retrieval)
- Memory Intelligence Patterns (entity types, update triggers, consolidation)
- Filesystem Governance Rules (scope validation, safe operations)
- GitHub Workflow Patterns (issue resolution, PR review, code operations)
- Artifact Lifecycle Rules (create/update/rewrite decision criteria)
- Error Recovery Strategy (degradation, alternatives, manual fallback)
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- User identification and memory anchoring at session start
- Memory updates structured as discrete, auditable graph mutations
- Filesystem actions scoped and verified before execution
- GitHub workflows following canonical patterns with proper sequencing
- Clear error recovery with graceful degradation paths

Avoid:
- Unbounded memory growth without consolidation strategies
- Filesystem operations outside explicitly allowed directories
- Missing error handling in multi-tool operation sequences
- Ignoring artifact versioning and change control requirements
</quality_criteria>

<constraints>
- All filesystem operations must validate paths against allowed directories first
- Memory updates must use entity-relation model, not free-form storage
- GitHub operations must follow authenticated, auditable sequences
- Session context must be retrievable and restorable on reconnection
</constraints>
```

---

## Example Usage

### Input

We need an MCP integration for a code development workflow. Tools available: memory (knowledge graph), filesystem (workspace access), GitHub (repos, issues, PRs), llm-context (code analysis). Goal: Context-aware code assistance that remembers project context, user preferences, and ongoing work across sessions.

### Output

**Session Bootstrap Protocol**

1. **User Identification**: Query memory for `default_user` entity or request identification on first session
2. **Context Retrieval**: Begin with "Remembering..." and query knowledge graph for user identity, project context, recent activity, and pending work
3. **Filesystem Validation**: Call `list_allowed_directories` to confirm workspace scope before any file operations

**Memory Intelligence Patterns**

```
Entity Types:
- User (identity, preferences, communication style, goals)
- Project (name, tech stack, structure, conventions)
- Task (current work, blockers, progress, dependencies)
- Decision (architectural choices, rationale, date, stakeholders)
- Context (recent conversations, discoveries, insights)

Update Triggers:
- New project context discovered during code exploration
- User preference expressed or inferred from behavior
- Significant architectural decision made with rationale
- Task completion, milestone, or blocker identification
- Important discovery or insight worth preserving

Consolidation Strategy:
- Merge related observations weekly
- Archive completed tasks to historical entities
- Prune stale context older than 30 days
```

**GitHub Workflow Patterns**

```
Issue Resolution Flow:
list_issues (filtered by assignee/label) →
get_issue (full context with comments) →
[development work with filesystem operations] →
add_issue_comment (progress update) →
create_pull_request (linked to issue) →
update_issue (status change, close)

Pull Request Review Flow:
get_pull_request (metadata, description) →
get_pull_request_files (changed files list) →
[code analysis using filesystem read operations] →
create_pending_review (start review) →
add_review_comment (inline feedback per file) →
submit_review (approve/request changes/comment)
```

**Artifact Lifecycle Rules**

- `create`: Use for novel outputs not derived from existing artifacts (new files, new documentation)
- `update`: Use for incremental changes affecting less than 20 lines or 5 locations in existing artifacts
- `rewrite`: Use for semantically significant refactoring, restructuring, or major content changes

**Error Recovery Strategy**

On tool failure, degrade gracefully with documented alternatives:

- GitHub unavailable: Use filesystem for local state tracking, queue operations for retry, document in memory for manual follow-up
- Memory error: Rely on session context, document observations in conversation for manual memory update later
- Filesystem error: Switch to read-only analysis mode, alert user to permission or path issues

---

## Related Prompts

- [FastMCP Server Patterns](./fastmcp-server-patterns.md) - Building custom MCP servers
- [GitHub Automation Workflows](../technical/mcp/claude-with-mcps.md) - GitHub-specific MCP patterns
- [Register New MCP Servers](../technical/mcp/register-new-mcp-servers.md) - Adding new MCP capabilities
