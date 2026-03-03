# Multiple Personas

## Multiple Personas

```javascript
// Create persona set for comprehensive coverage

class PersonaFramework {
  createPersonaSet(research_data) {
    return {
      primary_personas: [
        {
          name: "Sarah (VP Product)",
          percentage: "35%",
          influence: "High",
          role: "Decision maker",
        },
        {
          name: "Mike (Team Lead)",
          percentage: "40%",
          influence: "High",
          role: "Daily user, key influencer",
        },
        {
          name: "Lisa (Admin)",
          percentage: "25%",
          influence: "Medium",
          role: "Setup and management",
        },
      ],
      secondary_personas: [
        {
          name: "John (Executive)",
          percentage: "10%",
          influence: "Medium",
          role: "Budget approval",
        },
      ],
      anti_personas: [
        {
          name: "Enterprise IT Director",
          reason: "Not target market, different needs",
          avoid: "Marketing to large enterprise buyers",
        },
      ],
    };
  }

  validatePersonas(personas) {
    return {
      coverage: personas.reduce((sum, p) => sum + p.percentage, 0),
      primary_count: personas.filter((p) => p.influence === "High").length,
      recommendations: [
        "Personas cover 100% of target market",
        "Focus on 2-3 primary personas",
        "Plan for secondary use cases",
        "Define clear anti-personas",
      ],
    };
  }

  createPersonaMap(personas) {
    return {
      influence_x_axis: "Low → High",
      adoption_y_axis: "Slow → Fast",
      sarah_vp: { influence: "High", adoption: "Fast" },
      mike_lead: { influence: "Very High", adoption: "Very Fast" },
      lisa_admin: { influence: "Medium", adoption: "Medium" },
      john_executive: { influence: "Very High", adoption: "Slow" },
      strategy:
        "Focus on Mike (influencer), design for Sarah (buyer), support Lisa (user)",
    };
  }
}
```
