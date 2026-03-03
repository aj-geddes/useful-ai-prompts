# Insight Documentation

## Insight Documentation

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
        data_sources: ["Interviews", "Surveys", "Analytics"],
      },
      implications: {
        for_design: insight.design_implications,
        for_product: insight.product_implications,
        for_strategy: insight.strategy_implications,
      },
      recommended_actions: [
        {
          action: "Redesign onboarding flow",
          priority: "High",
          owner: "Design team",
          timeline: "2 sprints",
        },
      ],
      confidence: "High (8/12 users mentioned, consistent pattern)",
    };
  }

  createResearchReport(research_data) {
    return {
      title: "User Research Synthesis Report",
      executive_summary: "Key findings in 2-3 sentences",
      methodology: "How research was conducted",
      key_insights: [
        "Insight 1 with supporting evidence",
        "Insight 2 with supporting evidence",
        "Insight 3 with supporting evidence",
      ],
      personas_informed: ["Persona 1", "Persona 2"],
      recommendations: ["Design recommendation 1", "Product recommendation 2"],
      appendix: ["Raw data", "Quotes", "Demographic breakdown"],
    };
  }

  presentInsights(insights) {
    return {
      format: "Presentation + Report",
      audience: "Product team, stakeholders",
      duration: "30 minutes",
      structure: [
        "Research overview (5 min)",
        "Key findings (15 min)",
        "Supporting evidence (5 min)",
        "Recommendations (5 min)",
      ],
      handout: "One-page insight summary",
    };
  }
}
```
