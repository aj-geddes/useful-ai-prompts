---
name: user-research-analysis
description: Analyze user research data to uncover insights, identify patterns, and inform design decisions. Synthesize qualitative and quantitative research into actionable recommendations.
---

# User Research Analysis

## Overview

Effective research analysis transforms raw data into actionable insights that guide product development and design.

## When to Use

- Synthesis of user interviews and surveys
- Identifying patterns and themes
- Validating design assumptions
- Prioritizing user needs
- Communicating insights to stakeholders
- Informing design decisions

## Instructions

### 1. **Research Synthesis Methods**

```python
# Analyze qualitative and quantitative data

class ResearchAnalysis:
    def synthesize_interviews(self, interviews):
        """Extract themes and insights from interviews"""
        return {
            'interviews_analyzed': len(interviews),
            'methodology': 'Thematic coding and affinity mapping',
            'themes': self.identify_themes(interviews),
            'quotes': self.extract_key_quotes(interviews),
            'pain_points': self.identify_pain_points(interviews),
            'opportunities': self.identify_opportunities(interviews)
        }

    def identify_themes(self, interviews):
        """Find recurring patterns across interviews"""
        themes = {}
        theme_frequency = {}

        for interview in interviews:
            for statement in interview['statements']:
                theme = self.categorize_statement(statement)
                theme_frequency[theme] = theme_frequency.get(theme, 0) + 1

        # Sort by frequency
        return sorted(theme_frequency.items(), key=lambda x: x[1], reverse=True)

    def analyze_survey_data(self, survey_responses):
        """Quantify and analyze survey results"""
        return {
            'response_rate': self.calculate_response_rate(survey_responses),
            'sentiment': self.analyze_sentiment(survey_responses),
            'key_findings': self.find_key_findings(survey_responses),
            'segment_analysis': self.segment_responses(survey_responses),
            'statistical_significance': self.calculate_significance(survey_responses)
        }

    def triangulate_findings(self, interviews, surveys, analytics):
        """Cross-check findings across sources"""
        return {
            'confirmed_insights': self.compare_sources([interviews, surveys, analytics]),
            'conflicting_data': self.identify_conflicts([interviews, surveys, analytics]),
            'confidence_level': self.assess_confidence(),
            'recommendations': self.generate_recommendations()
        }
```

### 2. **Affinity Mapping**

```yaml
Affinity Mapping Process:

Step 1: Data Preparation
  - Print or write user quotes on cards (one per card)
  - Include source (interview name, survey #)
  - Include relevant demographic info

Step 2: Grouping
  - Place cards on wall or digital board
  - Group related insights together
  - Allow overlapping if relevant
  - Move cards as relationships become clear

Step 3: Theme Identification
  - Name each grouping with theme
  - Move up one level of abstraction
  - Create meta-themes grouping clusters

Step 4: Synthesis
  - Describe each theme in 1-2 sentences
  - Capture key insight
  - Note supporting evidence

Example Output:

Theme: Discovery & Onboarding
  Sub-themes:
    - Learning curve too steep
    - Documentation unclear
    - Need guided onboarding
  Quote: "I didn't know where to start, wish there was a tutorial"
  Frequency: 8 of 12 users mentioned

Theme: Performance Issues
  Sub-themes:
    - App is slow
    - Loading times unacceptable
    - Mobile particularly bad
  Quote: "I just switched to competitor, too slow"
  Frequency: 6 of 12 users mentioned
```

### 3. **Insight Documentation**

```javascript
// Document and communicate insights

class InsightDocumentation {
  createInsightStatement(insight) {
    return {
      title: insight.name,
      description: insight.detailed_description,
      evidence: {
        quotes: insight.supporting_quotes,
        frequency: `${insight.frequency_count} of ${insight.total_participants} participants`,
        data_sources: ['Interviews', 'Surveys', 'Analytics']
      },
      implications: {
        for_design: insight.design_implications,
        for_product: insight.product_implications,
        for_strategy: insight.strategy_implications
      },
      recommended_actions: [
        {
          action: 'Redesign onboarding flow',
          priority: 'High',
          owner: 'Design team',
          timeline: '2 sprints'
        }
      ],
      confidence: 'High (8/12 users mentioned, consistent pattern)'
    };
  }

  createResearchReport(research_data) {
    return {
      title: 'User Research Synthesis Report',
      executive_summary: 'Key findings in 2-3 sentences',
      methodology: 'How research was conducted',
      key_insights: [
        'Insight 1 with supporting evidence',
        'Insight 2 with supporting evidence',
        'Insight 3 with supporting evidence'
      ],
      personas_informed: ['Persona 1', 'Persona 2'],
      recommendations: ['Design recommendation 1', 'Product recommendation 2'],
      appendix: ['Raw data', 'Quotes', 'Demographic breakdown']
    };
  }

  presentInsights(insights) {
    return {
      format: 'Presentation + Report',
      audience: 'Product team, stakeholders',
      duration: '30 minutes',
      structure: [
        'Research overview (5 min)',
        'Key findings (15 min)',
        'Supporting evidence (5 min)',
        'Recommendations (5 min)'
      ],
      handout: 'One-page insight summary'
    };
  }
}
```

### 4. **Research Validation Matrix**

```yaml
Validation Matrix:

Research Finding: "Onboarding is too complex"

Supporting Evidence:
  Source 1: Interviews
    - 8 of 12 users mentioned difficulty
    - Average time to first value: 45 min vs target 10 min
    - 3 users abandoned before completing setup

  Source 2: Analytics
    - Drop-off at step 3 of onboarding: 35%
    - Bounce rate on onboarding page: 28% vs site avg 12%

  Source 3: Support Tickets
    - 15% of support tickets about onboarding
    - Most common: "How do I get started?"

Confidence Level: HIGH (consistent across 3 sources)

Action: Prioritize onboarding redesign in next quarter
```

## Best Practices

### ✅ DO
- Use multiple research methods
- Triangulate findings across sources
- Document quotes and evidence
- Look for patterns and frequency
- Separate findings from interpretation
- Validate findings with users
- Share insights across team
- Connect to design decisions
- Document methodology
- Iterate research approach based on learnings

### ❌ DON'T
- Over-interpret small samples
- Ignore conflicting data
- Base decisions on single data point
- Skip documentation
- Cherry-pick quotes that support assumptions
- Present without supporting evidence
- Forget to note limitations
- Analyze without involving participants
- Create insights without actionable recommendations
- Let research sit unused

## Research Analysis Tips

- Use affinity mapping for qualitative synthesis
- Quantify qualitative findings (frequency counts)
- Create insight posters for sharing
- Use direct quotes to support findings
- Cross-check insights across data sources
