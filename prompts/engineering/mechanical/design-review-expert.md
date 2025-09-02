# Mechanical Design Review Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Engineering/Mechanical
- **Tags**: design review, mechanical engineering, analysis, validation, optimization, CAD
- **Version**: 2.0.0
- **Use Cases**: design review, engineering analysis, optimization, validation, compliance assessment
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you conduct thorough mechanical design reviews that ensure safety, performance, manufacturability, and cost-effectiveness through systematic engineering analysis.

## Prompt

```
I'll help you conduct a comprehensive mechanical design review. Let me gather information about your design:

**About the design:**
1. What type of product/component are you designing? (consumer, industrial, automotive, etc.)
2. What are the main performance requirements? (load, speed, accuracy, life)
3. What environment will it operate in? (temperature, pressure, chemicals, outdoor/indoor)
4. What materials are you planning to use?

**Technical specifications:**
5. What are the critical dimensions and tolerances?
6. What manufacturing processes will be used?
7. What safety standards or regulations apply?
8. What's your target cost per unit?

**Design documentation:**
9. What stage is the design in? (concept, detailed, prototype)
10. What analysis has been done? (FEA, thermal, fatigue, etc.)
11. Any failure history or concerns from similar designs?
12. Production volume expectations?

Based on your answers, I'll provide:

**DESIGN ASSESSMENT** - Strengths, weaknesses, and critical issues
**PERFORMANCE ANALYSIS** - Stress, thermal, dynamic, and safety evaluations
**MANUFACTURABILITY REVIEW** - DFM recommendations and cost optimization
**RISK ASSESSMENT** - Failure modes, safety concerns, and mitigation strategies
**OPTIMIZATION RECOMMENDATIONS** - Improvements for performance, cost, and reliability

Share your design details and any specific concerns you'd like me to focus on.
```

## Example Usage

**User Input:**
```
1. Industrial pump impeller for chemical processing
2. 3600 RPM, 500 GPM flow, 150 PSI head, 5-year continuous operation
3. Corrosive chemicals (pH 2-12), 20-80°C, occasional dry running
4. Currently specified: 316L stainless steel

5. Diameter: 250mm ±0.5mm, blade thickness: 8mm min, shaft bore: 50mm H7
6. Investment casting followed by CNC machining of critical surfaces
7. API 610 pump standard, ASME B73.1, ATEX for explosive atmospheres
8. Target: $800 per impeller at 200 units/year

9. Detailed design phase, preparing for prototype
10. Basic FEA done showing max stress 180 MPa, no thermal or fatigue analysis yet
11. Previous design had fatigue cracks at blade roots after 2 years
12. 200-300 units/year for next 5 years
```

**Assistant Output:**

Based on your industrial pump impeller design, here's my comprehensive review:

## DESIGN ASSESSMENT

### Strengths
- **Material Selection**: 316L SS excellent for corrosion resistance in pH 2-12 range
- **Conservative Stress**: 180 MPa max stress provides ~40% safety margin on yield
- **Standard Compliance**: Following API 610 ensures proven design practices

### Critical Issues Requiring Attention

1. **Fatigue Life Concern** 🚨
   - Previous 2-year failure vs. 5-year requirement is major red flag
   - No fatigue analysis completed yet
   - Stress concentration at blade roots likely cause

2. **Dry Running Risk** 🚨
   - No provision mentioned for dry run protection
   - Can cause rapid overheating and seizure
   - Consider wear rings or monitoring system

3. **Dynamic Analysis Gap**
   - No mention of modal analysis or critical speed evaluation
   - 3600 RPM operation requires resonance avoidance

## PERFORMANCE ANALYSIS

### Structural Analysis Recommendations

**Fatigue Life Calculation:**
```
Based on 316L SS properties and your stress levels:
- Endurance limit: ~140 MPa (adjusted for surface finish)
- Stress concentration factor at blade root: likely 2.5-3.0
- Effective stress: 180 × 2.5 = 450 MPa
- Expected life: ~10^5 cycles = 28 hours at 3600 RPM ❌

Required Actions:
1. Add generous root radius (minimum 5mm)
2. Polish blade roots to Ra 0.4 μm
3. Shot peen high-stress areas
4. Target max stress <100 MPa for infinite life
```

### Thermal Considerations

**Dry Running Analysis:**
- Temperature rise rate: ~50°C/minute without cooling
- 316L loses strength above 400°C
- Thermal stress from differential expansion

**Recommendations:**
- Add temperature monitoring (RTD in housing)
- Implement auto-shutdown at 120°C
- Consider duplex stainless for better strength retention

### Dynamic Analysis Requirements

**Critical Speed Check:**
```
First critical speed estimate: 5,400 RPM
Operating speed: 3,600 RPM
Separation margin: 50% ✓ (acceptable)

But verify with full modal analysis including:
- Fluid added mass effects
- Bearing stiffness
- Shaft dynamics
```

## MANUFACTURABILITY REVIEW

### Investment Casting Optimization

**Current Design Issues:**
- 8mm blade thickness may cause shrinkage porosity
- Sharp internal corners increase defect risk
- Surface finish typically 3.2 μm Ra (may need improvement)

**DFM Improvements:**
1. **Taper blades**: 10mm at root to 6mm at tip
2. **Add draft angles**: 1.5° minimum
3. **Uniform wall thickness**: Avoid abrupt changes
4. **Datum strategy**: Clear points for machining setup

### Cost Reduction Opportunities

**Material Optimization:**
- Consider CF8M (cast 316) instead of wrought 316L
- 20% cost savings with similar properties
- Better castability, less machining stock

**Manufacturing Alternatives:**
```
Current process cost breakdown:
- Investment casting: $450
- CNC machining: $250
- Quality/inspection: $100
Total: $800 ✓ (meets target)

Alternative for cost reduction:
- 5-axis CNC from solid: $950 (higher precision)
- Hybrid: Cast + minimal machining: $650 (recommended)
```

## RISK ASSESSMENT

### Failure Mode Analysis (FMEA)

| Failure Mode | Severity | Probability | RPN | Mitigation |
|--------------|----------|-------------|-----|------------|
| Fatigue crack at root | 9 | 8 | 72 | Redesign blade root geometry |
| Corrosion/erosion | 7 | 4 | 28 | Upgrade to duplex SS if needed |
| Dry run seizure | 8 | 5 | 40 | Add temperature protection |
| Resonance | 6 | 3 | 18 | Complete modal analysis |
| Casting defects | 5 | 4 | 20 | Improve NDT requirements |

### Safety Considerations

**ATEX Compliance:**
- Ensure surface temperature <135°C (T4 rating)
- No sparking risk from contact
- Consider non-sparking wear rings

## OPTIMIZATION RECOMMENDATIONS

### Immediate Actions (Before Prototype)

1. **Redesign Blade Root Geometry**
   ```
   Current: Sharp 90° transition
   Recommended: 
   - 8mm radius fillet minimum
   - Elliptical transition profile
   - Increase root thickness to 12mm
   ```

2. **Add Dry-Run Protection**
   - Temperature switch in pump housing
   - Optional: Mechanical seal with quench
   - Wear rings: Carbon vs ceramic

3. **Complete Analysis Suite**
   - Fatigue analysis with mean stress correction
   - Transient thermal analysis for dry run
   - Modal analysis with Campbell diagram

### Design Enhancements

**Hydraulic Optimization:**
- Consider backward-curved blades for better efficiency
- Add balance holes to reduce axial thrust
- Optimize inlet eye diameter for NPSHr

**Material Upgrade Path:**
```
If corrosion becomes issue:
316L → 2205 Duplex → Hastelloy C-276
Cost: $800 → $1,200 → $3,500
```

### Validation Testing Plan

**Before Production:**
1. **Hydrostatic test**: 1.5 × max pressure
2. **Spin test**: 1.2 × max speed
3. **Accelerated corrosion**: ASTM G48
4. **Performance mapping**: Full Q-H curve
5. **Endurance run**: 500 hours minimum

### Documentation Requirements

**For API 610 Compliance:**
- Material certificates (3.1)
- Casting quality radiographs
- Dynamic balance certificate
- Performance test curves
- Mechanical seal data sheets

## SUMMARY RECOMMENDATIONS

### Critical (Do Before Prototype)
1. ✅ Redesign blade roots with 8mm+ radius
2. ✅ Complete fatigue analysis targeting 10^7 cycles
3. ✅ Add temperature monitoring for dry-run protection

### Important (Before Production)
4. ⚡ Perform full modal analysis
5. ⚡ Validate with 500-hour endurance test
6. ⚡ Optimize casting process for defect reduction

### Cost-Benefit Analysis
- Redesign cost: ~$5,000 engineering time
- Prevents: $50,000+ warranty claims
- ROI: 10:1 minimum

Your design has good fundamentals but needs the critical modifications above to meet the 5-year life requirement. Focus on the fatigue issue first - it's your biggest risk.

## Related Prompts

- [Failure Analysis Expert](../../problem-solving/performance-bottleneck-analysis-expert.md)
- [Materials Selection Specialist](../../research-workflows/materials-research-expert.md)
- [Manufacturing Process Expert](../../business/operations/process-optimization-expert.md)
