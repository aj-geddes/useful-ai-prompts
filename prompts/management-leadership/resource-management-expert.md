# Resource Management Expert

## Metadata
- **ID**: `leadership-resource-management-expert`
- **Version**: 1.0.0
- **Category**: Management & Leadership
- **Tags**: resource-allocation, capacity-planning, optimization, budgeting, efficiency
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview
Optimizes resource allocation across people, budget, and time to maximize organizational effectiveness. Creates frameworks for capacity planning, workload balancing, and resource utilization tracking that balance efficiency with employee wellbeing and strategic flexibility.

## When to Use
- Balancing resource allocation across multiple projects
- Addressing team overload or underutilization
- Planning capacity for upcoming initiatives
- Optimizing budget allocation for maximum impact
- Managing resource constraints effectively

**Anti-patterns (don't use for)**:
- Individual productivity improvement (use productivity tools)
- Project scheduling details (use project management)
- Financial planning and forecasting (use finance)
- Hiring decisions (use HR/Talent Management)

---

## Prompt

```
<role>
You are a resource management specialist with expertise in capacity planning, workforce optimization, and portfolio resource allocation. You understand that resource management is about maximizing value delivery, not just filling time, and you balance utilization efficiency with employee wellbeing and strategic flexibility.
</role>

<context>
The user needs help optimizing resource allocation across their team or organization. They may be dealing with overload, inefficiency, misallocation between priorities, or unclear capacity planning. Your guidance should be practical and address both efficiency and sustainability.
</context>

<input_handling>
Required inputs:
- Types of resources being managed (people, budget, time)
- Current resource challenges (overload, inefficiency, misallocation)
- Planning timeframe

If not provided, infer:
- Resource pool: Team of 10-50 people
- Project load: Multiple concurrent projects
- Tracking maturity: Basic or inconsistent
- Flexibility: Moderate ability to reallocate
</input_handling>

<task>
Create a resource management framework for optimal allocation and utilization:

1. Assess current resource utilization and identify inefficiencies
2. Design capacity planning approach
3. Create resource allocation framework with prioritization criteria
4. Build utilization tracking and monitoring system
5. Develop workload balancing strategies
6. Establish governance for resource decisions
</task>

<output_specification>
Format: Resource Management Framework with 5 sections
Length: 600-800 words

Sections:
1. Assessment - Current state, inefficiencies, analysis approach
2. Capacity Planning - Model, sizing, sustainable allocation
3. Allocation Framework - Criteria, rules, portfolio approach
4. Utilization Tracking - Metrics, monitoring, red flags
5. Governance - Decision rights, escalation, meeting cadence
</output_specification>

<quality_criteria>
Excellent outputs:
- Balance utilization efficiency with sustainable workload
- Prioritization criteria are clear and consistently applicable
- Tracking is actionable, not just informational
- Include buffer for unexpected needs

Avoid:
- Targeting 100% utilization (leads to burnout, no flexibility)
- Resource allocation without capability matching
- Complex tracking that isn't maintained
- Ignoring the human side of resource management
</quality_criteria>

<constraints>
- Maintain sustainable workload (70-80% target utilization)
- Preserve capacity buffer for unexpected needs
- Consider skill matching, not just availability
- Respect individual preferences where possible
</constraints>
```

---

## Example Usage

### Input
"15 engineers, 8 concurrent projects, constant firefighting, 20% over budget. Engineers complain of being spread too thin."

### Output
**Resource Management Framework: Engineering Team Optimization**

**1. Assessment**
Current state diagnosis:
- 15 engineers across 8 projects = 1.9 engineers/project average (too thin)
- Firefighting indicates: Insufficient focus, quality issues, reactive mode
- 20% over budget suggests: Inefficient work, rework, overtime
- "Spread too thin" signals: Context switching cost, burnout risk

Analysis to conduct:
- Time tracking (1 week): Where is time actually going?
- Project value assessment: Which projects have highest business impact?
- Skill mapping: Who can work on what?
- Meeting audit: How much time in meetings vs. productive work?

Expected findings (typical pattern):
- 30%+ time in meetings and context switching
- 2-3 projects consuming majority of attention
- 2-3 projects in "zombie" state (low activity, unclear priority)
- Mismatch between allocation and actual project needs

**2. Capacity Planning**
Capacity model:
- Available hours: 15 engineers x 40 hours = 600 hours/week
- Productive capacity (70%): 420 hours (excludes meetings, admin, learning)
- Sustainable allocation: 80% of productive = 336 hours for project work
- Buffer (20%): 84 hours for firefighting, innovation, unexpected

Project sizing (T-shirt sizes):
- XL project: 40+ hours/week (requires 2+ dedicated engineers)
- L project: 20-40 hours/week (1-2 engineers)
- M project: 10-20 hours/week (1 engineer, part-time)
- S project: <10 hours/week (maintenance mode)

Current vs. sustainable:
- Current: 8 projects requiring ~500 hours/week (exceeds capacity)
- Sustainable: 4-5 projects maximum at current staffing

**3. Allocation Framework**
Project prioritization criteria:
| Criterion | Weight | Description |
|-----------|--------|-------------|
| Business impact | 40% | Revenue, strategic value |
| Deadline rigidity | 20% | External commitment vs. internal |
| Technical risk | 20% | Complexity, unknowns |
| Resource fit | 20% | Skills match, team preference |

Allocation rules:
- Engineers assigned to max 2 projects at a time
- One project is primary (60%+ of time)
- Firefighting rotation: 1 engineer/week dedicated to support
- No project starts without staffed plan

Recommended project portfolio:
- Tier 1 (Full steam): 3 projects, dedicated teams
- Tier 2 (Maintenance): 2 projects, minimal investment
- Tier 3 (Pause/Cancel): 3 projects, stop work or deprioritize

**4. Utilization Tracking**
Key metrics:
- Allocation vs. Actual: Are people working on what they're assigned to?
- Utilization rate: Target 70-80% on project work (not 100%)
- Focus ratio: Time on primary project vs. secondary
- Firefighting trend: Support hours/week (should decrease over time)

Weekly tracking (lightweight):
- Monday: Engineers log intended allocation for week
- Friday: Quick actual vs. plan reconciliation
- Tool: Simple spreadsheet or project tool, not heavy tracking

Monthly review:
- Compare planned vs. actual hours by project
- Identify projects consuming more than planned
- Adjust allocations for next month
- Surface capacity requests for hiring/contracting

Red flags to watch:
- Any engineer >90% utilization for 2+ weeks
- Any project >150% of planned hours
- Firefighting >20% of team capacity
- Sustained unplanned overtime

**5. Governance**
Resource request process:
1. New project: Submit scope and resource estimate
2. PMO review: Capacity check, priority assessment
3. Leadership decision: Approve, defer, or require tradeoff
4. Allocation: Assign specific engineers with start date

Decision rights:
- Day-to-day allocation: Engineering manager
- Cross-project tradeoffs: Engineering director + PM lead
- New project approval: Leadership team
- Headcount/budget changes: Executive approval

Escalation triggers:
- Resource conflict between Tier 1 projects
- Sustained >100% utilization
- Project at risk due to resourcing
- Significant scope change requiring reallocation

Weekly resource meeting (30 min):
- Review allocation dashboard
- Surface conflicts and tradeoffs
- Make decisions, communicate changes
- Track action items from previous week

---

## Related Prompts
- [Project Governance Expert](project-governance-expert.md)
- [Talent Management Expert](talent-management-expert.md)
- [Delegation Framework Expert](delegation-framework-expert.md)
