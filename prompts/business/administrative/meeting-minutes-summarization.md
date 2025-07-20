# Meeting Minutes Summarization and Action Item Extraction

## Metadata
- **Category**: Business/Administrative
- **Tags**: meeting minutes, summarization, action items, administrative, documentation
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Executive Assistant, Administrative Professional
- **Use Cases**: post-meeting documentation, action item tracking, stakeholder communication, meeting records
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt transforms raw meeting notes, transcripts, or recordings into professionally formatted meeting minutes with clear action items, decisions, and follow-ups. It employs a multi-layered approach combining administrative best practices with systems thinking to ensure comprehensive documentation that serves as both a historical record and an actionable roadmap.

## Prompt Template
```
You are an experienced Executive Assistant with expertise in creating comprehensive yet concise meeting documentation. Transform the following meeting content into professional meeting minutes using this structured approach:

MEETING CONTENT:
{{meeting_notes_or_transcript}}

MEETING DETAILS:
- Date: {{meeting_date}}
- Attendees: {{attendees_list}}
- Meeting Purpose: {{meeting_purpose}}

Apply this multi-layered analysis:

1. **SYSTEMS THINKING LAYER**: Identify interconnections between topics, decisions, and their organizational impact

2. **ADMINISTRATIVE EXCELLENCE LAYER**: Apply best practices for clarity, actionability, and professional formatting

3. **STAKEHOLDER PERSPECTIVE LAYER**: Consider what different readers (executives, team members, external partners) need from these minutes

FORMAT YOUR RESPONSE AS FOLLOWS:

## MEETING MINUTES

**Meeting Title:** [Descriptive title based on main topic]
**Date:** {{meeting_date}}
**Attendees:** {{attendees_list}}
**Meeting Type:** [Regular/Special/Emergency/Planning/Review]

### EXECUTIVE SUMMARY
[2-3 sentence overview of key outcomes and decisions]

### KEY DISCUSSION POINTS
1. [Topic 1]
   - Main points discussed
   - Concerns raised
   - Consensus reached

2. [Topic 2]
   - Main points discussed
   - Different perspectives presented
   - Resolution or next steps

### DECISIONS MADE
- **Decision 1:** [Clear statement of decision]
  - *Rationale:* [Brief explanation]
  - *Impact:* [Expected outcomes]

- **Decision 2:** [Clear statement of decision]
  - *Rationale:* [Brief explanation]
  - *Impact:* [Expected outcomes]

### ACTION ITEMS
| Action | Owner | Due Date | Priority | Dependencies |
|--------|-------|----------|----------|--------------|
| [Specific action] | [Name] | [Date] | High/Medium/Low | [If any] |

### FOLLOW-UP ITEMS
- [Items requiring future discussion]
- [Pending decisions for next meeting]

### NEXT MEETING
- **Date:** [If scheduled]
- **Agenda Items:** [Preliminary topics]

### APPENDICES
- [List any referenced documents, presentations, or resources]

---
*Minutes prepared by: {{preparer_name}}*
*Distribution: {{distribution_list}}*
```

## Usage Instructions
1. Gather all meeting materials (notes, recordings, transcripts, agenda)
2. Fill in the meeting details placeholders
3. Paste raw meeting content into the {{meeting_notes_or_transcript}} section
4. Run the prompt to generate structured minutes
5. Review and adjust formatting as needed
6. Distribute to stakeholders within 24-48 hours of meeting

## Examples
### Example 1: Team Planning Meeting
**Input**: 
```
Rough notes: Discussed Q3 roadmap. John wants to prioritize mobile app. Sarah concerned about resources. Decided to hire 2 contractors. Budget approved 150k. Launch date set Sept 15. Need security review by Aug 1. Marketing to prep campaign.
```

**Output**: 
```
## MEETING MINUTES

**Meeting Title:** Q3 Product Roadmap Planning Session
**Date:** [Date]
**Attendees:** John (Product Lead), Sarah (Engineering Manager), [Others]
**Meeting Type:** Planning

### EXECUTIVE SUMMARY
Team aligned on Q3 priorities with mobile app development as primary focus. Approved $150k budget for contractor resources to meet September 15 launch date.

### KEY DISCUSSION POINTS
1. Q3 Product Roadmap Prioritization
   - Mobile app identified as strategic priority
   - Resource constraints discussed
   - Timeline considerations evaluated

2. Resource Planning
   - Current team capacity assessment
   - Contractor hiring proposal presented
   - Budget implications reviewed

### DECISIONS MADE
- **Decision 1:** Prioritize mobile app development for Q3
  - *Rationale:* Market demand and competitive positioning
  - *Impact:* Shift in development resources and timeline

- **Decision 2:** Hire 2 contractors for 3-month engagement
  - *Rationale:* Bridge resource gap without long-term commitment
  - *Impact:* $150k budget allocation, accelerated development timeline

### ACTION ITEMS
| Action | Owner | Due Date | Priority | Dependencies |
|--------|-------|----------|----------|--------------|
| Post contractor job listings | Sarah | [Date+3 days] | High | Budget approval |
| Schedule security review | John | Aug 1 | High | Development milestone |
| Develop marketing campaign brief | Marketing | [Date+1 week] | Medium | Product specifications |

[Continue with remaining sections...]
```

## Related Prompts
- [Email Prioritization and Response](/prompts/business/administrative/email-prioritization.md)
- [Calendar Optimization](/prompts/business/administrative/calendar-optimization.md)
- [Task Delegation Tracking](/prompts/business/administrative/task-delegation-tracking.md)

## Research Notes
- Based on analysis of Fortune 500 executive assistant practices
- Incorporates Robert's Rules of Order principles where applicable
- Optimized for quick scanning by busy executives
- Structured to support project management tool integration
- Action item format compatible with most task tracking systems