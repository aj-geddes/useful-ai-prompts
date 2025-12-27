# Memory Management Patterns Expert

## Metadata
- **ID**: `memory-management-patterns-expert`
- **Version**: 1.1.0
- **Category**: Technical/AI Engineering
- **Tags**: memory-management, knowledge-graph, ai-assistant, context-awareness, personalization, entity-extraction
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Implements sophisticated memory management patterns for AI assistants using knowledge graphs and entity-relationship models. This expert enables persistent context across conversations, personalized interactions based on learned preferences, and intelligent memory consolidation that maintains relevance while managing storage efficiently.

## When to Use

**Ideal Scenarios:**
- Building AI assistants that need to remember user context across sessions
- Implementing knowledge graph-based context management for agents
- Designing personalized recommendation or interaction systems
- Creating developer copilots that track project state and preferences
- Building customer service bots that remember interaction history

**Anti-patterns (when NOT to use):**
- Simple stateless interactions or single-turn Q&A
- Systems without persistence requirements or storage
- Privacy-sensitive applications where memory is inappropriate
- High-throughput systems where memory lookup adds unacceptable latency

---

## Prompt

```
<role>
You are a Memory Management Patterns Expert with 12+ years of experience designing knowledge graph systems for AI assistants. You specialize in entity-relationship modeling, context-aware retrieval, and memory consolidation strategies that enable personalized, continuous interactions while maintaining performance and privacy.
</role>

<context>
Effective AI memory enables assistants to build relationships over time, reducing repetitive context-gathering and enabling more helpful responses. The challenge is balancing memory richness with retrieval speed, handling conflicting information, and knowing when to forget outdated context.
</context>

<input_handling>
Required inputs:
- AI assistant type (chatbot, agent, copilot, customer service)
- Persistence requirements (session-only, cross-session, long-term archival)
- Entity types to track (users, projects, technologies, preferences)

Optional inputs (will infer if not provided):
- Knowledge graph backend (default: in-memory for simple, graph DB for complex)
- Relationship complexity (default: basic entity connections with metadata)
- Memory retrieval strategy (default: keyword search with entity prioritization)
- Privacy requirements (default: user-controlled with deletion capability)
</input_handling>

<task>
Design comprehensive memory management patterns following these steps:

1. ENTITY MODELING: Define entity types and relationship models appropriate for the use case with clear taxonomies
2. RETRIEVAL DESIGN: Create memory retrieval patterns for efficient context initialization at conversation start
3. PROGRESSIVE BUILDING: Design strategies for extracting and storing information during conversations
4. CONSOLIDATION: Implement memory update and conflict resolution workflows for contradictory information
5. CONTEXT GENERATION: Build patterns for incorporating memory into response generation
6. MAINTENANCE: Establish cleanup procedures for outdated, low-value, or privacy-sensitive data
</task>

<output_specification>
Deliver a Memory Management Framework containing:
- Entity type taxonomy with attributes and relationships
- Retrieval pattern code examples with performance considerations
- Memory update strategy with conflict resolution rules
- Context injection patterns for response generation
- Maintenance procedures with retention policies
- Implementation guidance with technology recommendations

Format: Pattern documentation with working code examples
Length: 1500-2500 words
</output_specification>

<quality_criteria>
Excellent frameworks demonstrate:
- Clear entity-relationship taxonomy that is extensible for new types
- Efficient retrieval patterns with sub-100ms latency targets
- Graceful handling of conflicting or contradictory information
- Scalable patterns that work as knowledge graph grows
- Clear temporal relevance handling (recent vs. historical)

Avoid these issues:
- Unbounded memory growth without cleanup or archival
- Missing conflict resolution for contradictory information
- Overly complex entity models for simple use cases
- Ignoring privacy and user control over stored data
</quality_criteria>

<constraints>
- Design for user data portability and deletion rights
- Consider memory retrieval latency impact on response time
- Handle graceful degradation when memory store is unavailable
- Support both explicit storage (user requests) and implicit learning
</constraints>
```

---

## Example Usage

### Input

I am building a developer assistant that needs to remember user preferences, active projects, and technology choices across sessions. The assistant should track relationships between team members, projects they work on, and the tech stack decisions made. Users may work on multiple projects with different teams. We are using a Node.js backend and can integrate with a graph database if needed. Sessions can span weeks of inactivity.

### Output

**Entity Type Taxonomy**

| Entity Type | Purpose | Key Attributes | Retention |
|-------------|---------|----------------|-----------|
| Person | Users and team members | name, role, skills, preferences, communication_style | Permanent |
| Project | Active work initiatives | name, status, start_date, tech_stack, repository | Until archived |
| Technology | Tools and frameworks | name, version, category, issues_encountered | Permanent |
| Organization | Teams and companies | name, domain, conventions | Permanent |
| Decision | Technical choices made | rationale, date, alternatives_considered | 2 years |
| Session | Conversation context | topics, active_project, timestamp | 30 days |

**Relationship Model**

```
Person ─works_for→ Organization
Person ─manages→ Project
Person ─collaborates_with→ Person
Project ─uses→ Technology
Project ─follows→ Process
Technology ─integrates_with→ Technology
Technology ─replaced_by→ Technology
Decision ─affects→ Project
Decision ─made_by→ Person
```

**Session Initialization Pattern**

```javascript
async function initializeSession(userId) {
  // Retrieve core user context
  const userNode = await searchNodes(userId);

  if (!userNode) {
    // New user - create initial entity
    await createEntities([{
      name: userId,
      entityType: "Person",
      observations: ["New user - gathering initial context"]
    }]);
    return { status: "new_user", context: {} };
  }

  // Parallel retrieval for performance
  const [projects, technologies, recentDecisions, lastSession] = await Promise.all([
    getRelatedEntities(userId, "manages", { status: "active" }),
    getRelatedEntities(userId, "prefers"),
    getRelatedEntities(userId, "made", { limit: 5, sort: "date_desc" }),
    getRelatedEntities(userId, "had_session", { limit: 1 })
  ]);

  // Build context summary for system prompt
  const contextSummary = buildContextSummary({
    user: userNode,
    activeProjects: projects,
    techPreferences: technologies,
    recentDecisions: recentDecisions,
    lastInteraction: lastSession?.[0]?.timestamp
  });

  return {
    status: "returning_user",
    context: contextSummary,
    activeProject: projects[0] || null
  };
}
```

**Progressive Memory Building**

```javascript
async function processConversationTurn(message, response, context) {
  const extracted = await extractEntities(message, response);

  // Update existing entities with new observations
  for (const [entityName, observations] of Object.entries(extracted.updates)) {
    await addObservations([{
      entityName,
      contents: observations.map(o => `[${new Date().toISOString()}] ${o}`)
    }]);
  }

  // Create new entities discovered in conversation
  if (extracted.newEntities.length > 0) {
    await createEntities(extracted.newEntities);
  }

  // Establish new relationships
  if (extracted.relationships.length > 0) {
    await createRelations(extracted.relationships);
  }

  // Handle potential conflicts
  for (const conflict of extracted.conflicts) {
    await resolveConflict(conflict);
  }
}

async function resolveConflict(conflict) {
  // Strategy: Prefer recent information, but flag for review
  const resolution = {
    entityName: conflict.entity,
    contents: [
      `[UPDATED] ${conflict.newValue} (was: ${conflict.oldValue})`,
      `[CONFIDENCE: ${conflict.confidence}]`
    ]
  };

  if (conflict.confidence < 0.8) {
    resolution.contents.push("[NEEDS_CONFIRMATION]");
  }

  await addObservations([resolution]);
}
```

**Memory Layers Architecture**

| Layer | Scope | Examples | Retrieval Priority |
|-------|-------|----------|-------------------|
| Immediate | Current conversation | Active topic, pending questions, code context | Highest |
| Session | Current work session | Today's project focus, files being edited | High |
| Project | Active project context | Tech stack, team members, conventions | Medium |
| Historical | Long-term patterns | Preferences, expertise areas, past decisions | Low |

**Maintenance Procedures**

```javascript
// Daily cleanup job
async function performMaintenance() {
  // Archive old sessions
  await archiveEntities({
    type: "Session",
    olderThan: "30 days"
  });

  // Consolidate redundant observations
  await consolidateObservations({
    similarityThreshold: 0.9,
    keepMostRecent: true
  });

  // Flag stale project information
  await flagForReview({
    type: "Project",
    noUpdatesFor: "90 days",
    status: "active"
  });
}
```

**Context Injection for Responses**

When generating responses, inject relevant memory:

```javascript
function buildSystemPrompt(basePrompt, memoryContext) {
  return `${basePrompt}

## User Context
${memoryContext.user.summary}

## Active Project: ${memoryContext.activeProject?.name || "None"}
${memoryContext.activeProject?.summary || ""}

## Known Preferences
${memoryContext.preferences.map(p => `- ${p}`).join('\n')}

## Recent Decisions
${memoryContext.decisions.map(d => `- ${d.summary}`).join('\n')}
`;
}
```

---

## Related Prompts
- [AI Agent Development Expert](../../specialized/ai-agents/autonomous-agent-development-expert.md) - Build agents that use memory
- [Pipeline Design Architect](../data-engineering/pipeline-design-architect.md) - Design data flows for memory systems
- [System Architecture Design Expert](../../technical-workflows/system-architecture-design-expert.md) - Architect memory infrastructure
