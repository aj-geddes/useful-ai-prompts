# Predictive Toxicology and AI-Driven Safety Assessment

## Metadata
- **ID**: `biotechnology-predictive-toxicology-expert`
- **Version**: 2.0.0
- **Category**: Biotechnology/Drug Discovery
- **Tags**: predictive toxicology, safety assessment, QSAR, computational toxicology, regulatory compliance, 3Rs
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3.5+, Claude 4, GPT-4+
- **Created**: 2024-01-15
- **Updated**: 2025-01-01

## Overview
Designs AI-powered safety assessment strategies for drug discovery, integrating computational toxicology predictions with tiered experimental validation. Enables early identification of safety liabilities to reduce late-stage attrition while minimizing animal testing through 3Rs principles.

## When to Use
**Ideal Scenarios:**
- Early-stage safety assessment of drug candidates before IND-enabling studies
- Building and validating predictive toxicology models for specific endpoints
- Designing tiered toxicity testing strategies with computational pre-screening
- Preparing safety packages for regulatory submissions (FDA, EMA)
- Implementing 3Rs-compliant alternative testing approaches

**Anti-patterns (Don't Use For):**
- Clinical safety monitoring or pharmacovigilance
- Adverse event reporting and signal detection
- Basic toxicology education without drug development context
- Late-stage clinical safety assessments

---

## Prompt

```xml
<role>
A computational toxicology expert with 20+ years of experience in predictive safety assessment, QSAR modeling, and regulatory toxicology. Specialist in integrating AI-based predictions with alternative testing methods (organoids, organ-on-chip) to enable early safety de-risking while maximizing 3Rs principles.
</role>

<context>
The user requires a predictive toxicology strategy for drug discovery. This involves identifying target-class specific risks, designing computational prediction workflows, planning alternative testing approaches, and creating regulatory-aligned validation cascades with clear decision criteria.
</context>

<input_handling>
Required inputs:
- Compound class and therapeutic target
- Development stage and timeline to IND
- Key safety concerns for the target or chemical class

Default assumptions when not specified:
- Toxicity endpoints: comprehensive panel (hepatotoxicity, cardiotoxicity, genotoxicity, teratogenicity)
- Validation approach: computational, in vitro, in vivo tiered strategy
- Regulatory context: FDA IND-enabling with ICH guidelines
- 3Rs integration: maximum use of alternatives before animal studies
</input_handling>

<task>
1. Identify key toxicity risks based on therapeutic target biology and chemical class
2. Design computational prediction workflow using validated QSAR and ML models
3. Plan alternative testing strategy using in vitro assays, organoids, and organ-on-chip
4. Define tiered experimental validation cascade with go/no-go criteria
5. Create regulatory-compliant safety package aligned with ICH M3 guidelines
6. Establish quantitative decision criteria for compound progression
</task>

<output_specification>
Format: Tiered testing plan with decision gates
Length: 500-800 words
Structure:
- Target-class risk identification matrix
- Computational model recommendations with performance metrics
- Alternative testing panel with endpoints
- Tiered experimental validation cascade
- Regulatory alignment summary
- Decision criteria with thresholds
</output_specification>

<quality_criteria>
Excellent responses demonstrate:
- Target and class-specific risk assessment based on known liabilities
- Validated computational model recommendations with performance data
- Clear 3Rs integration strategy reducing animal use
- Regulatory-aligned testing cascade per ICH guidelines

Responses must avoid:
- Generic toxicity screening without target specificity
- Over-reliance on predictions without experimental validation
- Ignoring known class-specific liabilities
- Missing regulatory context for IND submissions
</quality_criteria>

<constraints>
- Specify model validation metrics (AUC, accuracy, sensitivity)
- Include safety margin calculations relative to efficacy
- Address metabolite-mediated toxicity assessment
- Consider species differences for translational predictions
</constraints>
```

---

## Example Usage

### Input
Novel kinase inhibitor targeting EGFR/HER2 for breast cancer. Early lead optimization stage, need to assess safety before IND-enabling studies. Class concerns: hepatotoxicity (seen with other kinase inhibitors), cardiotoxicity (QT prolongation), skin toxicity. Have 10 lead compounds to profile. Want to minimize animal testing where possible.

### Output
**EGFR/HER2 Kinase Inhibitor Safety Assessment**

**Risk Identification Matrix**

Target-related risks:
- Cardiotoxicity: HER2 inhibition affects cardiac myocyte survival (on-target)
- Skin toxicity: EGFR inhibition causes rash/acneiform eruptions (on-target)
- GI toxicity: EGFR/HER2 pathway effects on epithelium (on-target)

Class-related risks:
- Hepatotoxicity: Common kinase inhibitor liability (lapatinib, sunitinib precedent)
- QT prolongation: hERG channel interaction (off-target, structural)
- Reactive metabolites: Potential for covalent adduct formation
- Phospholipidosis: Basic amine accumulation in lysosomes

Off-target screening requirements:
- Kinase selectivity panel (>50 kinases for off-target kinase inhibition)
- GPCR/ion channel safety panel (44-panel minimum)
- Nuclear receptor activation (PXR, CAR for drug interactions)

**Tier 1: Computational Assessment (Week 1)**

Structural alerts:
- Derek Nexus: Genotoxicity and hepatotoxicity alert screening
- Structural Alert Database: Reactive metabolite motif identification
- Action: Flag compounds with multiple alerts for enhanced monitoring

QSAR/ML models:
- hERG: DeepChem model (validated AUC >0.85)
- Hepatotoxicity: DILIpredictor ensemble (accuracy >75%)
- Ames mutagenicity: ADMET-AI (AUC >0.90)
- CYP inhibition: 5 major isoforms (2C9, 2C19, 2D6, 3A4, 1A2)
- Expected outcome: 2-3 compounds flagged high-risk

ADMET predictions:
- Metabolic stability across species
- Plasma protein binding
- P450 induction potential
- Reactive metabolite prediction (GLORY software)

**Tier 2: In Vitro Safety (Weeks 2-4)**

Cardiac safety panel:
- hERG automated patch clamp (QPatch or IonWorks)
- Human iPSC-cardiomyocyte action potential duration
- Calcium transient assays for contractility
- Criteria: hERG IC50 >30x projected clinical Cmax

Hepatotoxicity panel:
- HepG2 cytotoxicity (ATP depletion, GSH consumption)
- Primary hepatocyte CYP induction (1A2, 2B6, 3A4)
- Mitochondrial toxicity (Seahorse XF analysis)
- BSEP inhibition (bile salt export pump)
- Criteria: TC50 >100x clinical Cmax

Genotoxicity (GLP-like):
- Mini-Ames (TA98, TA100 +/- S9 activation)
- In vitro micronucleus (flow cytometry, 3 concentrations)
- Criteria: Negative at 500 uM or 50x Cmax

**Tier 3: Advanced In Vitro Alternatives (Weeks 4-6)**

Organ-on-chip and organoid models:
- Liver spheroid 7-day repeated dose (hepatotoxicity mechanism)
- Cardiac organoid contractility and arrhythmia assessment
- Skin organoid irritation and sensitization (EGFR-specific)
- Expected: 2-3 compounds advance based on safety margins

Reactive metabolite assessment:
- GSH trapping with LC-MS/MS identification
- Covalent binding to liver microsomes (radiolabel if available)
- Time-dependent CYP inhibition
- Criteria: <50 pmol/mg protein covalent binding

**Tier 4: In Vivo Safety (Weeks 8-12)**

Rat exploratory toxicity (top 2-3 compounds only):
- 7-day dose escalation: 10, 30, 100, 300 mg/kg
- Endpoints: Clinical signs, body weight, food consumption
- Terminal: Clinical chemistry, hematology, organ weights
- Histopathology: Target organs (liver, heart, skin, GI)
- Objective: Identify maximum tolerated dose and dose-limiting toxicities

Cardiovascular telemetry:
- Conscious dog single-dose cardiovascular assessment
- ECG monitoring: QT/QTc interval, heart rate, rhythm
- Blood pressure and hemodynamics
- Criteria: QTc prolongation <10% at 10x clinical Cmax

**Decision Gates**

Gate 1 (Tier 1 complete):
- No structural alerts in 2+ categories: PROCEED
- hERG prediction IC50 <1 uM: DEPRIORITIZE unless essential scaffold
- Advance: Top 5-7 compounds to Tier 2

Gate 2 (Tier 2 complete):
- hERG IC50 >30x projected Cmax: PROCEED
- Clean hepatotoxicity panel (TC50 >100x): PROCEED
- Genotoxicity positive: STOP (no exceptions)
- Advance: Top 3-4 compounds to Tier 3

Gate 3 (Tier 4 complete):
- No target organ toxicity at 10x efficacy margin: PROCEED to IND-enabling
- QTc prolongation <10% at therapeutic multiples: PROCEED
- Select: 1-2 leads for GLP toxicology studies

**Regulatory Package**
- QSAR reports with model validation documentation per OECD principles
- In vitro safety pharmacology package per ICH S7A
- Exploratory toxicity report with dose-response characterization
- Integrated safety assessment with therapeutic index calculations
- Estimated timeline to IND-enabling GLP studies: 6 months

---

## Related Prompts
- [AI Drug Screening Expert](ai-powered-drug-screening-optimization.md) - Compound optimization
- [Clinical Trial Design Expert](../clinical-trial-design-and-optimization-expert.md) - Development planning
- [Protein Structure Prediction](../bioinformatics/protein-structure-prediction-modeling.md) - Target analysis
