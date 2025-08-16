---
category: business
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for business optimization and expert consultation
slug: meeting-minutes-summarization-expert
tags:
- business
title: Meeting Minutes & Summarization Expert
use_cases:
- business optimization
- professional workflow enhancement
version: 3.0.0
---

# Meeting Minutes & Summarization Expert

## Metadata

- **Category**: Business/Administrative
- **Tags**: meeting minutes, summarization, action items, administrative, documentation
- **Created**: 2025-07-20
- **Version**: 3.0.0
- **Use Cases**: post-meeting documentation, action item tracking, stakeholder communication, decision records
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt transforms raw meeting recordings, notes, or transcripts into professional meeting minutes with clear action items, decisions, and follow-up plans.

## Prompt

```
I'll help you create professional meeting minutes that capture key decisions and drive action. Let me understand your meeting:

**About the meeting:**
1. What type of meeting was this? (team, board, project, client, etc.)
2. Who attended and what are their roles?
3. What was the main purpose or agenda?
4. How long was the meeting?

**Content format:**
5. What do you have? (recording, transcript, notes, or live meeting)
6. Are there any sensitive topics that need careful handling?
7. Who will receive these minutes?
8. Any specific format or template requirements?

**Follow-up needs:**
9. Do you need action items tracked separately?
10. Are there deadlines or milestones to highlight?
11. Should this connect to previous meeting minutes?
12. Any decisions that need formal documentation?

Based on your input, I'll provide:

**EXECUTIVE SUMMARY** - Key outcomes and decisions at a glance
**DETAILED MINUTES** - Professional meeting record with structure
**ACTION ITEMS** - Clear tasks with owners and deadlines
**DECISION TRACKER** - Important decisions made and rationale
**FOLLOW-UP PLAN** - Next steps and future meeting needs

Please share your meeting content (recording transcript, notes, or description).
```

## Example Usage

**User Input:**
```
1. Weekly product team standup meeting
2. Attendees: Sarah (Product Manager), Mike (Tech Lead), Lisa (Designer), 
   Tom (QA), Alex (Marketing), Jennifer (CEO - joined for 15 min)
3. Review sprint progress, discuss Q4 feature roadmap, address user feedback
4. 60 minutes

5. I have a transcript from Zoom recording
6. Nothing too sensitive, but some competitive mentions
7. Team members, plus David (CTO who missed meeting)
8. Need action items in table format for Monday follow-up

9. Yes, separate action items list needed
10. Q4 launch deadline is critical (Dec 15)
11. This builds on last week's roadmap discussion
12. Decision on whether to delay Feature X needs formal documentation

[Transcript provided...]
SARAH: "Let's start with sprint updates. Mike, how are we tracking?"
MIKE: "We completed 8 of 10 story points. The payment integration is taking longer than expected..."
[Full transcript continues...]
```

**Assistant Output:**

Based on your product team standup, here are the professional meeting minutes:

## MEETING MINUTES - Product Team Weekly Standup

**Date:** January 21, 2025  
**Time:** 2:00 PM - 3:00 PM EST  
**Meeting Type:** Weekly Team Standup  
**Chair:** Sarah Martinez (Product Manager)

### ATTENDEES
- Sarah Martinez, Product Manager ✓
- Mike Chen, Tech Lead ✓  
- Lisa Rodriguez, UX Designer ✓
- Tom Johnson, QA Engineer ✓
- Alex Kim, Marketing Manager ✓
- Jennifer Walsh, CEO ✓ (2:45-3:00 PM)

**Absent:** David Thompson, CTO (traveling)

### EXECUTIVE SUMMARY

**Key Outcomes:**
- Sprint 23 achieved 80% completion (8/10 story points)
- **DECISION:** Feature X delayed to Q1 2026 due to resource constraints
- Q4 launch timeline remains Dec 15 with adjusted scope
- User feedback integration prioritized for next sprint
- 5 action items assigned with clear deadlines

**Critical Issues Resolved:**
- Payment integration complexity addressed with vendor consultation
- Mobile performance concerns escalated to infrastructure team
- Marketing timeline realigned with development delays

### DETAILED MINUTES

#### 1. SPRINT 23 PROGRESS REVIEW
**Completed (8/10 story points):**
- User authentication system ✅
- Search functionality improvements ✅  
- Mobile responsive updates ✅
- API rate limiting implementation ✅

**In Progress:**
- Payment integration (60% complete, blocking issue with Stripe API)
- Performance optimization (waiting for infrastructure team input)

**Challenges Identified:**
- Payment integration more complex than estimated (3 days → 8 days)
- Mobile performance issues discovered during testing
- Resource allocation stretched across too many features

#### 2. Q4 FEATURE ROADMAP DISCUSSION
**Features Confirmed for Q4 Release:**
- Enhanced search with filters
- Mobile performance improvements
- User dashboard redesign
- Basic payment functionality

**Feature X Status - DECISION MADE:**
- **Decision:** Delay Feature X to Q1 2026
- **Rationale:** Current timeline too aggressive, quality concerns raised
- **Impact:** Allows focus on core Q4 features and proper testing
- **CEO Approval:** Jennifer confirmed this decision aligns with business priorities

#### 3. USER FEEDBACK INTEGRATION
**Key Themes from Last Sprint:**
- Mobile app loading speed (addressed in current sprint)
- Search accuracy improvements (83% user satisfaction target)
- Payment flow confusion (will inform Q1 Feature X design)

**Actions Taken:**
- UX research scheduled for next week
- A/B testing framework setup for search improvements
- Customer feedback tagged and categorized in product backlog

### DECISIONS MADE

| Decision | Rationale | Impact | Approved By |
|----------|-----------|--------|-------------|
| Delay Feature X to Q1 2026 | Resource constraints, quality concerns | Frees 2 developers for Q4 focus | Jennifer (CEO) |
| Extend payment integration timeline | Stripe API complexity underestimated | Sprint 24 buffer needed | Sarah (PM) |
| Prioritize mobile performance | User feedback critical mass reached | Infrastructure team engagement | Mike (Tech Lead) |

### ACTION ITEMS

| Task | Owner | Deadline | Priority | Status |
|------|-------|----------|----------|--------|
| Schedule Stripe vendor consultation | Mike | Jan 23 | High | Pending |
| Complete mobile performance audit | Tom | Jan 25 | High | Pending |
| Update Q4 timeline in project tracker | Sarah | Jan 22 | Medium | Pending |
| Send feature delay communication to stakeholders | Alex | Jan 24 | Medium | Pending |
| Schedule UX research sessions for Feature X | Lisa | Jan 30 | Low | Pending |

### FOLLOW-UP ITEMS
- **Next Meeting:** January 28, 2025 (Weekly Standup)
- **Special Sessions Needed:**
  - Feature X planning workshop (Early February)
  - Q4 launch preparation meeting (November)
- **Stakeholder Communications:**
  - David (CTO) - catch up on Feature X decision
  - Customer Success team - updated timeline communication
  - Finance team - Q4 budget impact review

### MEETING EFFECTIVENESS NOTES
- **Duration:** On time (60 minutes)
- **Participation:** High engagement, all voices heard
- **Decision Quality:** Clear rationale provided, CEO input valuable
- **Action Clarity:** All items have clear owners and deadlines

**Process Improvements for Next Meeting:**
- Pre-meeting tech check for Jennifer's audio issues
- Distribute user feedback summary 24 hours in advance
- Include David via video link when traveling

---

**Minutes Prepared By:** AI Assistant  
**Distribution:** All attendees + David Thompson (CTO)  
**Next Review:** January 28, 2025 Weekly Standup

## ACTION ITEMS SUMMARY FOR MONDAY FOLLOW-UP

**This Week (High Priority):**
1. ⚠️ Mike: Stripe consultation scheduled (due Jan 23)
2. ⚠️ Tom: Mobile performance audit complete (due Jan 25)  
3. 📋 Sarah: Update project tracker with new timeline (due Jan 22)

**Early Next Week:**
4. 📧 Alex: Stakeholder communication sent (due Jan 24)
5. 📅 Lisa: UX research sessions scheduled (due Jan 30)

**Overdue Items from Previous Meetings:** None

Would you like me to format this differently or add any additional sections?
```

## Related Prompts

- [Calendar Optimization Expert](./calendar-optimization.md)
- [Task Delegation Expert](./task-delegation-tracking.md)
- [Email Management Expert](./email-prioritization-response.md)