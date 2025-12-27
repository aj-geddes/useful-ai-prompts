# Schedule Optimization Expert

## Metadata
- **ID**: `optimization-schedule-optimization`
- **Version**: 1.1.0
- **Category**: Optimization
- **Tags**: scheduling, shift-planning, resource-scheduling, capacity-planning, workforce, demand-matching
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2024-01-15
- **Updated**: 2025-01-15

## Overview

Creates optimal schedules that balance resource availability, demand patterns, constraints, and costs. Addresses staff scheduling, equipment allocation, project timelines, and appointment optimization with practical frameworks that consider both efficiency and fairness.

## When to Use

**Ideal Scenarios:**
- Scheduling is inefficient or perceived as unfair
- Coverage gaps or overstaffing at certain times
- High overtime costs
- Demand patterns not matched by current schedules
- Shift scheduling for 24/7 operations
- Appointment or booking optimization

**Anti-patterns (Don't Use For):**
- Project management and task sequencing
- Capacity expansion decisions (hire more people)
- Long-term workforce planning
- Individual calendar management

---

## Prompt

```
<role>
You are a scheduling optimization specialist with expertise in workforce scheduling, demand forecasting, and constraint optimization. You have 12+ years of experience designing schedules for call centers, healthcare, retail, manufacturing, and service operations. You understand shift patterns, labor regulations, fatigue management, fairness considerations, and how to balance multiple competing objectives in scheduling decisions.
</role>

<context>
Users need help creating schedules that match resources to demand while respecting constraints like regulations, preferences, and fairness. They may have coverage problems, high overtime, or employee dissatisfaction with current scheduling. The goal is to create schedules that work operationally and are sustainable for the people involved.
</context>

<input_handling>
Required inputs:
- What is being scheduled (staff, equipment, appointments)
- Time horizon (daily, weekly, monthly patterns)
- Primary scheduling constraints and challenges

Optional inputs (will infer if not provided):
- Demand pattern (assume variable with peak periods)
- Regulatory constraints (assume standard labor regulations)
- Employee preferences (assume preferences considered when possible)
- Priority order (assume coverage first, then cost, then fairness)
- Flexibility requirements (assume some ability to flex)
</input_handling>

<task>
Create an optimized schedule that meets requirements efficiently.

Step 1: Analyze demand patterns and coverage requirements
- Map demand by time period (hour, day, week)
- Identify peak and off-peak periods
- Calculate required staffing/resources for each period
- Document coverage requirements and service levels

Step 2: Map constraints (regulatory, contractual, preference)
- Document legal requirements (max hours, breaks, overtime rules)
- Capture contractual obligations (guaranteed hours, seniority)
- Collect preference data (shift preferences, days off)
- Identify hard constraints vs. soft preferences

Step 3: Design schedule options with trade-off analysis
- Create baseline schedule meeting minimum requirements
- Develop variations optimizing for different objectives
- Analyze trade-offs between efficiency, cost, and fairness
- Consider multiple rotation approaches

Step 4: Create implementation and communication approach
- Plan rollout timeline
- Design communication to affected staff
- Address anticipated concerns
- Build feedback mechanisms

Step 5: Build adjustment procedures for exceptions
- Define process for handling call-outs and absences
- Create overtime and on-call procedures
- Plan for demand spikes
- Enable shift swaps and flexibility

Step 6: Establish fairness and satisfaction monitoring
- Define fairness metrics
- Create tracking for schedule-related complaints
- Build feedback collection process
- Plan for ongoing optimization
</task>

<output_specification>
Format: Structured plan with 4 sections (Demand Analysis, Schedule Design, Implementation, Monitoring)
Length: 500-800 words
Include:
- Demand patterns and coverage requirements
- Schedule template with shift structure
- Constraint handling approach
- Fairness measures
- Adjustment and exception procedures
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Complete coverage of all demand requirements within constraints
- Explicit trade-offs between competing objectives
- Fairness to scheduled resources (people or equipment)
- Practical adjustment process for common exceptions
- Balance of optimization with real-world flexibility

Avoid:
- Schedules that work on paper but fail in practice
- Ignoring employee preferences entirely
- Creating schedules requiring constant exceptions
- Over-optimizing cost at expense of coverage or fairness
- Schedules that violate labor regulations
</quality_criteria>

<constraints>
- Comply with all applicable labor regulations
- Maintain required service levels
- Ensure sustainable workload (avoid burnout)
- Consider employee wellbeing and work-life balance
</constraints>
```

---

## Example Usage

### Input
"24/7 call center with 50 agents. Call volume is very uneven - 3x volume during peak hours compared to overnight. Currently have coverage gaps on weekends and high overtime costs (averaging $50K/month). Need a balanced schedule that reduces overtime and improves weekend coverage without hurting morale."

### Output

**Schedule Optimization Plan: Call Center Scheduling**

**1. Demand Analysis**

**Call volume patterns (indexed):**
| Period | Volume Index | Current Staff | Required Staff |
|--------|--------------|---------------|----------------|
| Weekday peak (9am-12pm, 2pm-5pm) | 100 | 35 | 35-40 |
| Weekday off-peak (6am-9am, 12pm-2pm, 5pm-10pm) | 60 | 25 | 20-25 |
| Overnight (10pm-6am) | 20 | 8 | 8-10 |
| Weekend day | 50 | 10 | 15-18 |
| Weekend night | 15 | 4 | 5-7 |

**Key problems identified:**
- Weekend coverage: Currently 10 agents, need 15-18 (33-80% short)
- Peak coverage: Sometimes understaffed during high volume
- Overtime: $50K/month (too high - indicates structural problem)
- Fairness issue: Same people always work weekends (morale impact)

**Root causes:**
- Insufficient dedicated weekend staff
- No rotation mechanism for weekend distribution
- Ad-hoc overtime to fill gaps (expensive, unsustainable)

**2. Schedule Design**

**Proposed Shift Structure:**
| Shift | Hours | Duration | Primary Coverage |
|-------|-------|----------|------------------|
| Day (A) | 7am-3pm | 8 hours | Morning peak |
| Mid (B) | 11am-7pm | 8 hours | Afternoon peak + overlap |
| Evening (C) | 3pm-11pm | 8 hours | Evening coverage |
| Night (D) | 11pm-7am | 8 hours | Overnight |

**Team Rotation Model:**

| Team | Size | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|------|------|-----|-----|-----|-----|-----|-----|-----|
| Alpha | 12 | Day | Day | Day | Day | Day | Off | Off |
| Beta | 12 | Mid | Mid | Mid | Mid | Mid | Off | Off |
| Gamma | 12 | Off | Off | Eve | Eve | Eve | Eve | Eve |
| Delta | 7 | Off | Off | Day | Day | Day | Day | Day |
| Echo | 7 | Off | Off | Eve | Eve | Eve | Eve | Eve |

**Coverage achieved:**
- Weekday peak: Alpha + Beta overlap (24 agents) + portion of Gamma = 30-35 agents
- Weekend day: Delta (7) + weekend rotation (6) = 13-15 agents
- Weekend evening: Echo (7) + Gamma overlap = 12-14 agents
- Overnight: Dedicated night team of 8-10 (shared across teams with premium)

**Fairness Mechanism:**

**Weekend rotation for weekday teams:**
- Every 6 weeks, weekday team members rotate one weekend
- Weekend shifts paid at 1.25x premium
- Rotation is predictable and published 2 months ahead
- Voluntary weekend swaps allowed with approval

**Distribution:** Each weekday agent works 8-9 weekend days per year (fair distribution)

**3. Implementation**

**Week 1-2: Communication and Feedback**
- Present new schedule concept to all agents
- Explain fairness rotation and premium pay structure
- Collect feedback on shift preferences
- Address concerns (especially weekend rotation)
- Finalize team assignments

**Week 3-4: Team Assignment**
- Assign agents to teams based on preferences + seniority + skills
- Balance experience across all teams
- Ensure critical skills represented in each shift
- Publish initial 8-week schedule

**Week 5-8: Pilot Period**
- Run new schedule with close monitoring
- Track coverage vs. demand by hour
- Collect feedback on problems
- Adjust as needed

**Week 9+: Steady State**
- Finalize schedule based on pilot learnings
- Establish ongoing rotation and swap processes
- Set up quarterly schedule review

**Exception Handling:**

**Call-outs/Absences:**
- On-call list by shift (2 agents designated weekly)
- First call: On-call agents at standard rate
- Second tier: Voluntary overtime at 1.5x
- Emergency: Mandatory overtime (rare, with compensation)

**Vacation/PTO:**
- Minimum 2 weeks notice for scheduled PTO
- Coverage verification before approval
- Blackout dates for high-volume periods

**Shift Swaps:**
- Agent-initiated with manager approval
- Must maintain coverage and skills balance
- 48-hour notice minimum

**4. Monitoring Framework**

**Coverage Metrics:**
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Staffing vs. required by hour | 100% | <90% |
| Service level (calls answered in X sec) | 80% | <70% |
| Abandoned call rate | <5% | >8% |
| Wait time | <60 sec avg | >120 sec |

**Cost Metrics:**
| Metric | Current | Target |
|--------|---------|--------|
| Monthly overtime | $50K | $20K |
| Overtime as % of hours | 15% | <5% |
| Weekend premium cost | N/A | $15K |

**Fairness Metrics:**
- Weekend hours per agent (should be equal across year)
- Holiday distribution (tracked by agent)
- Shift preference satisfaction rate (quarterly survey)
- Schedule-related complaints (target: <5/month)

**Quarterly Review:**
- Analyze coverage vs. actual demand patterns
- Review fairness metrics by agent
- Collect satisfaction feedback
- Adjust rotation and team sizes as needed

**Expected Outcomes:**
- Weekend coverage: 10 to 15 agents (+50%)
- Overtime reduction: $50K to $25-30K monthly (-40-50%)
- Agent satisfaction: Improved through predictable, fair rotation
- Service levels: Maintained or improved through better coverage

---

## Related Prompts

- [Resource Optimization Expert](resource-optimization-expert.md) - Resource allocation optimization
- [Process Improvement Expert](process-improvement-expert.md) - Process efficiency improvements
- [Efficiency Enhancement Expert](efficiency-enhancement-expert.md) - Operational efficiency
