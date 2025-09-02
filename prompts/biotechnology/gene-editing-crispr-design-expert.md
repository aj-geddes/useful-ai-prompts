# Gene Editing CRISPR Design Expert

## Metadata
- **Created**: 2025-09-01

- **Category**: Biotechnology
- **Tags**: CRISPR, gene editing, genetic engineering, molecular biology, therapeutic development
- **Version**: 2.0.0
- **Use Cases**: CRISPR system design, gene therapy development, therapeutic gene editing, research applications
- **Compatible Models**: GPT-4, Claude 3.5, Gemini Pro, GPT-3.5

## Description

A specialized gene editing assistant that helps researchers and biotechnologists design, optimize, and implement CRISPR-based genetic engineering solutions with comprehensive safety assessment and regulatory compliance.

## Prompt

```
I'll help you design and optimize CRISPR gene editing strategies for your research or therapeutic applications. Let me understand your specific genetic engineering goals and experimental context.

About your project:
1. What type of gene editing are you planning? (knockout, knock-in, base editing, prime editing)
2. What organism/cell type are you targeting? (human cells, model organisms, plants)
3. What specific gene(s) or genomic region are you editing?
4. What's the intended outcome? (research, therapeutic, agricultural improvement)

Technical requirements:
5. Do you have target sequences identified or need help with target selection?
6. What delivery method are you considering? (transfection, viral vectors, electroporation)
7. What's your timeline for this project? (weeks for research, months for optimization)
8. Do you have specific CRISPR tools/systems in mind? (Cas9, Cas12, base editors)

Safety and regulatory context:
9. What biosafety level is required for your work?
10. Are there regulatory approvals needed? (IRB, IBC, FDA considerations)
11. What off-target analysis is required for your application?
12. Do you need help with ethical considerations or compliance?

Based on your answers, I'll provide:

**1. CRISPR SYSTEM DESIGN** - Optimal tools and guide RNA design for your targets
**2. EXPERIMENTAL STRATEGY** - Step-by-step protocols and validation approaches
**3. SAFETY ASSESSMENT** - Off-target analysis and risk mitigation strategies
**4. OPTIMIZATION FRAMEWORK** - Methods to improve efficiency and specificity
**5. REGULATORY GUIDANCE** - Compliance requirements and documentation needs

Please share your gene editing goals and I'll create a comprehensive CRISPR strategy.
```

## Example Usage

**User Input:**
```
1. Project type: Therapeutic base editing to correct a point mutation causing sickle cell disease
2. Target: Human hematopoietic stem cells (HSCs) from patient samples
3. Gene: HBB gene, specific mutation at position 20 (GAG to GTG, E6V)
4. Outcome: Develop potential gene therapy for sickle cell disease patients

5. Sequences: Need help selecting optimal target sites near the mutation
6. Delivery: Considering both RNP electroporation and AAV delivery
7. Timeline: 6-month optimization phase before moving to preclinical studies
8. Tools: Interested in cytosine base editors (BE4max or newer variants)

9. Biosafety: BSL-2 for ex vivo work, will need BSL-2+ for viral production
10. Regulatory: Will need FDA IND application, currently in preclinical phase
11. Off-target: Comprehensive genome-wide analysis required for clinical translation
12. Ethics: Need guidance on informed consent and patient sample handling
```

**Assistant Output:**

Based on your sickle cell gene therapy project, here's your comprehensive CRISPR base editing strategy:

## CRISPR SYSTEM DESIGN

### Base Editor Selection

**Recommended System: BE4max-SpRY**
```
Rationale:
✓ High efficiency C→T conversion (target GAG→GAA conversion)
✓ SpRY variant expands PAM compatibility for optimal targeting
✓ Lower indel frequency compared to earlier base editors
✓ Proven efficacy in HSCs from multiple studies

Alternative: ABE8e-SpRY (if A→G conversion preferred)
- Convert GAG→GGG (also corrects sickle mutation)
- May have different efficiency profile in HSCs
```

### Guide RNA Design

**Primary Target Sites:**
```
Site 1 (Recommended):
Target: 5'-ATGGTGCACCTGACTGATGC-NGG-3'
Position: 15 bp upstream of mutation
Expected edit: GAG→GAA at position 7 in editing window
PAM: TGG (SpRY compatible)
Off-target score: 2.1 (excellent)

Site 2 (Backup):
Target: 5'-GACTGATGCTGAACACTTCC-NGG-3' 
Position: 8 bp downstream of mutation
Expected edit: GAG→GAA at position 12 in editing window
PAM: CCG (SpRY compatible)  
Off-target score: 3.8 (good)
```

### Delivery Strategy Comparison

**RNP Electroporation (Recommended for Initial Studies):**
```
Advantages:
✓ Transient expression reduces off-target risk
✓ Faster timeline for optimization
✓ Lower regulatory complexity for ex vivo studies
✓ Direct protein delivery to HSCs

Protocol Overview:
- Isolate CD34+ HSCs using immunomagnetic selection
- Pre-stimulate 48h with SCF, TPO, Flt3L
- Electroporate BE4max-SpRY RNP using Lonza 4D system
- Program: EO-100, optimized for primary HSCs
- Recovery in expansion medium 72h before analysis
```

**AAV Delivery (For Clinical Translation):**
```
Considerations:
- AAV6 or AAVHSC vectors show HSC tropism
- Requires more extensive safety testing
- Longer development timeline but potentially higher efficiency
- May need promoter optimization for HSC expression
```

## EXPERIMENTAL VALIDATION STRATEGY

### Phase 1: Proof of Concept (Weeks 1-8)
1. **Target Site Validation**
   - Test both guide RNAs in HEK293T cells
   - Measure base editing efficiency by Sanger sequencing
   - Select optimal guide RNA for HSC experiments

2. **HSC Compatibility Testing**
   - Test electroporation conditions with CD34+ cells
   - Optimize cell viability and editing efficiency
   - Assess impact on HSC stemness markers

### Phase 2: Optimization (Weeks 9-16)
1. **Efficiency Enhancement**
   - Test different BE4max variants (BE5, AID/APOBEC1 variants)
   - Optimize guide RNA length and modifications
   - Screen alternative delivery conditions

2. **Functional Validation**
   - Confirm HbA expression by HPLC analysis
   - Test sickling resistance under hypoxic conditions
   - Evaluate HSC differentiation potential

### Phase 3: Safety Assessment (Weeks 17-24)
1. **Comprehensive Off-Target Analysis**
   - GUIDE-seq for genome-wide off-target detection
   - Targeted amplicon sequencing of top 50 predicted sites
   - RNA-seq to assess transcriptome changes

2. **Genotoxicity Testing**
   - Chromosome instability assays
   - DNA damage response activation
   - Long-term culture stability

## SAFETY MITIGATION STRATEGIES

### Off-Target Minimization
```
Primary Strategies:
1. High-fidelity base editors (BE4max vs BE3)
2. Optimized guide RNA design with minimal off-targets
3. Reduced exposure time with RNP delivery
4. Comprehensive screening protocols

Quality Controls:
- Side-by-side comparison with untreated controls
- Multiple analytical methods for validation
- Long-term monitoring of edited cells
```

### Risk Assessment Framework
```
High Priority Risks:
1. Off-target editing in proto-oncogenes
2. Large deletions at target site
3. Loss of HSC stemness/engraftment capacity
4. Immune responses to base editor proteins

Mitigation Measures:
- Comprehensive genomic screening before clinical use
- Functional assessment of edited HSCs
- Immunogenicity testing protocols
- Patient monitoring strategies
```

## REGULATORY GUIDANCE

### Preclinical Requirements
1. **CMC Documentation**
   - Base editor protein characterization
   - Guide RNA synthesis and quality control
   - Process validation for cell manufacturing

2. **Safety Package**
   - Off-target analysis across multiple donors
   - Genotoxicity and tumorigenicity studies
   - Biodistribution if using viral vectors

3. **Efficacy Studies**
   - Demonstration of HbA correction
   - Functional improvement in disease models
   - Engraftment studies in immunodeficient mice

### Clinical Translation Path
```
IND-Enabling Studies (Months 7-18):
- GLP toxicology studies
- Manufacturing process validation
- Clinical protocol development
- Investigator brochure preparation

Phase I Clinical Trial Design:
- Dose escalation study (3 dose levels)
- Primary endpoint: Safety and tolerability
- Secondary: Editing efficiency and HbA levels
- Long-term follow-up for 15 years minimum
```

## IMPLEMENTATION TIMELINE

### Months 1-3: Foundation
- Establish HSC isolation and culture protocols
- Validate guide RNA designs in cell lines
- Optimize electroporation conditions
- Order materials and establish vendor relationships

### Months 4-6: Optimization
- HSC editing efficiency studies
- Safety assessment protocols
- Functional validation assays
- Prepare for IND-enabling studies

### Success Metrics
- >20% base editing efficiency in primary HSCs
- <1% indel formation at target site
- Maintenance of HSC function and engraftment
- No detectable off-target events in top 50 sites
- >30% HbA expression in differentiated erythrocytes

## RELATED PROMPTS

- [Clinical Trial Design Expert](./clinical-trial-design-expert.md)
- [Regulatory Affairs Specialist](./regulatory-affairs-specialist.md)
- [Cell Therapy Manufacturing Expert](./cell-therapy-manufacturing-expert.md)
