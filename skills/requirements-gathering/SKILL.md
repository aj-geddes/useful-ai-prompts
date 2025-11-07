---
name: requirements-gathering
description: Systematically collect, document, and validate requirements from stakeholders. Ensure clarity, completeness, and agreement before development begins to reduce scope creep and rework.
---

# Requirements Gathering

## Overview

Effective requirements gathering establishes a shared understanding of what will be built, preventing misalignment and expensive changes later in the project.

## When to Use

- Project kickoff and planning
- Feature development initiation
- Product roadmap planning
- System modernization projects
- Customer discovery
- Stakeholder alignment sessions
- Writing user stories and acceptance criteria

## Instructions

### 1. **Stakeholder Discovery**

```python
# Identify and analyze stakeholders

class StakeholderDiscovery:
    STAKEHOLDER_CATEGORIES = [
        'End Users',
        'Business Owners',
        'Technical Leads',
        'Operations/Support',
        'Customers',
        'Regulatory Bodies',
        'Integration Partners'
    ]

    def identify_stakeholders(self, project):
        """Map all stakeholder groups"""
        return {
            'primary': self.get_primary_stakeholders(project),
            'secondary': self.get_secondary_stakeholders(project),
            'tertiary': self.get_tertiary_stakeholders(project),
            'total_to_engage': self.calculate_engagement_strategy(project)
        }

    def analyze_stakeholder_needs(self, stakeholder):
        """Understand what each stakeholder needs"""
        return {
            'stakeholder': stakeholder.name,
            'role': stakeholder.role,
            'goals': self.extract_goals(stakeholder),
            'pain_points': self.extract_pain_points(stakeholder),
            'constraints': self.extract_constraints(stakeholder),
            'success_criteria': self.define_success(stakeholder),
            'engagement_frequency': self.plan_engagement(stakeholder)
        }

    def extract_goals(self, stakeholder):
        """What does this stakeholder want to achieve?"""
        return {
            'business_goals': [],  # Revenue, efficiency, market share
            'technical_goals': [],  # Performance, scalability, reliability
            'user_goals': [],       # Ease of use, effectiveness
            'operational_goals': []  # Support efficiency, uptime
        }

    def extract_pain_points(self, stakeholder):
        """What are current problems?"""
        return [
            'Current solution limitations',
            'Integration challenges',
            'Performance issues',
            'User adoption barriers',
            'Operational costs'
        ]
```

### 2. **Requirements Elicitation Techniques**

```yaml
Elicitation Techniques:

1. Interviews (One-on-One)
   Best For: Senior stakeholders, sensitive topics
   Duration: 30-60 minutes
   Output: Detailed requirements, context
   Preparation: Create question guide, schedule in advance

   Sample Questions:
     - What are you trying to accomplish?
     - What's currently preventing you?
     - What would success look like?
     - What metrics matter most?
     - What are your biggest risks?

---

2. Workshops (Group Sessions)
   Best For: Cross-functional alignment, brainstorming
   Duration: 2-4 hours
   Output: Consensus, prioritization
   Preparation: Agenda, facilitation guide, materials

   Format:
     - Opening (10 min): Goals and agenda
     - Brainstorm (45 min): Generate ideas
     - Clarify (30 min): Understand each idea
     - Prioritize (45 min): Rank by importance
     - Decide (30 min): Commit to priorities

---

3. User Observation (Contextual Inquiry)
   Best For: Understanding actual workflows
   Duration: 2-4 hours
   Output: Realistic workflows, hidden requirements
   Preparation: Gain access, create observation guide

   Focus On:
     - Current workflow steps
     - Pain points and workarounds
     - Frequency of tasks
     - Error handling
     - Collaboration patterns

---

4. Surveys
   Best For: Broad input from many people
   Duration: 10-15 minutes per respondent
   Output: Quantified preferences, trends
   Preparation: Write clear questions, select sample

   Types:
     - Multiple choice (easy analysis)
     - Rating scales (prioritization)
     - Open-ended (discovery)
     - Ranking (prioritization)

---

5. Document Analysis
   Best For: Understanding existing processes
   Duration: Variable
   Output: Current state understanding
   Preparation: Request documents in advance

   Review:
     - Process documentation
     - System specifications
     - User manuals
     - Incident reports
     - Competitor products
```

### 3. **Requirements Documentation**

```javascript
// Structure and document requirements

class RequirementsDocument {
  createRequirementStatement(requirement) {
    return {
      id: `REQ-${Date.now()}`,
      title: requirement.title,
      description: requirement.description,
      rationale: 'Why is this important?',
      source: requirement.stakeholder,
      category: requirement.category, // Functional, non-functional, constraint
      priority: requirement.priority, // Must, Should, Could, Won't
      acceptance_criteria: [
        {
          criterion: 'Specific, measurable behavior',
          test: 'How to verify'
        }
      ],
      dependencies: [],
      assumptions: [],
      constraints: [],
      estimated_effort: 'TBD',
      status: 'Draft',
      last_reviewed: new Date(),
      review_comments: []
    };
  }

  categorizeRequirements(requirements) {
    return {
      functional: requirements.filter(r => r.category === 'Functional'),
      non_functional: requirements.filter(r => r.category === 'Non-Functional'),
      constraints: requirements.filter(r => r.category === 'Constraint'),
      prioritized: this.prioritizeRequirements(requirements)
    };
  }

  prioritizeRequirements(requirements) {
    // MoSCoW method: Must, Should, Could, Won't
    return {
      must: requirements.filter(r => r.priority === 'Must'),
      should: requirements.filter(r => r.priority === 'Should'),
      could: requirements.filter(r => r.priority === 'Could'),
      wont: requirements.filter(r => r.priority === 'Won\'t')
    };
  }

  validateRequirements(requirements) {
    const issues = [];

    requirements.forEach(req => {
      // Check completeness
      if (!req.acceptance_criteria || req.acceptance_criteria.length === 0) {
        issues.push({
          requirement: req.id,
          issue: 'Missing acceptance criteria',
          severity: 'High'
        });
      }

      // Check clarity
      if (req.description.length < 20) {
        issues.push({
          requirement: req.id,
          issue: 'Description too vague',
          severity: 'High'
        });
      }

      // Check for ambiguous words
      const ambiguousWords = ['quickly', 'easily', 'user-friendly', 'efficient'];
      if (ambiguousWords.some(word => req.description.includes(word))) {
        issues.push({
          requirement: req.id,
          issue: 'Contains ambiguous language',
          severity: 'Medium'
        });
      }
    });

    return {
      valid: issues.length === 0,
      issues: issues,
      recommendations: this.getRecommendations(issues)
    };
  }
}
```

### 4. **Requirement Validation & Sign-Off**

```yaml
Requirements Review Checklist:

Completeness:
  [ ] All stakeholder needs documented
  [ ] Functional requirements defined
  [ ] Non-functional requirements specified
  [ ] Constraints identified
  [ ] Assumptions documented
  [ ] Exclusions clearly stated

Clarity:
  [ ] Requirements are specific and measurable
  [ ] No ambiguous language
  [ ] Acceptance criteria clear
  [ ] Technical team understands
  [ ] Business team agrees

Feasibility:
  [ ] Requirements technically feasible
  [ ] Timeline realistic
  [ ] Resource requirements identified
  [ ] Risk assessment completed
  [ ] Dependencies identified

Traceability:
  [ ] Each requirement traced to stakeholder need
  [ ] Each requirement linked to user story
  [ ] Each requirement connected to tests

Validation:
  [ ] Stakeholder review completed
  [ ] Business approval obtained
  [ ] Technical feasibility confirmed
  [ ] Sign-off received

---

Sign-Off:

Business Lead: ____________________  Date: ________
Technical Lead: ____________________  Date: ________
Project Manager: ____________________  Date: ________

Requirements Baseline Established: February 1, 2025
Approved For: Development Planning
Change Control Process: Activated
```

### 5. **Requirements Traceability Matrix**

```yaml
Traceability Matrix:

Stakeholder Need → Requirement → User Story → Test Case

---

Stakeholder: CFO (Cost Reduction)
Need: Reduce operational costs by 30%

Requirements:
  REQ-101: System must auto-scale infrastructure
  REQ-102: Must support multi-region deployment
  REQ-103: Database queries must complete in <500ms

User Stories:
  US-201: As an ops engineer, I can scale resources automatically
  US-202: As a user, I can access service from any region

Test Cases:
  TC-301: Verify auto-scaling triggers at 80% capacity
  TC-302: Verify <100ms latency between regions

---

Stakeholder: VP Product
Need: Improve user engagement by 25%

Requirements:
  REQ-104: Mobile-first responsive design
  REQ-105: Push notifications support
  REQ-106: Offline-first capability

Related Metrics:
  - Daily active users +25%
  - Session duration +40%
  - User retention +15%
```

## Best Practices

### ✅ DO
- Engage all key stakeholders early
- Document requirements in writing
- Use specific, measurable language
- Define acceptance criteria
- Prioritize using MoSCoW method
- Get stakeholder sign-off
- Create traceability matrix
- Review requirements regularly
- Distinguish must-haves from nice-to-haves
- Document assumptions and constraints

### ❌ DON'T
- Rely on memory or verbal agreements
- Create requirements without stakeholder input
- Use ambiguous language (quickly, easily, etc.)
- Skip non-functional requirements
- Ignore constraints and dependencies
- Over-document trivial details
- Rush through requirements phase
- Build without stakeholder agreement
- Make scope changes without process
- Forget about edge cases and error conditions

## Requirements Gathering Tips

- Use prototypes to clarify requirements
- Review requirements in writing before meetings
- Get one stakeholder representative
- Use visual diagrams for complex workflows
- Test requirements understanding through mock demos
