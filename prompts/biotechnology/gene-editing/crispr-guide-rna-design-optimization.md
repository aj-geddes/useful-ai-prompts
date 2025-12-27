# CRISPR Guide RNA Design and Optimization Platform

## Metadata
- **ID**: `biotechnology-crispr-grna-design-optimization`
- **Version**: 2.0.0
- **Category**: Biotechnology/Gene Editing
- **Tags**: CRISPR, gRNA design, off-target analysis, gene editing optimization, therapeutic gene editing, specificity
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3.5+, Claude 4, GPT-4+
- **Created**: 2024-01-15
- **Updated**: 2025-01-01

## Overview
Provides comprehensive CRISPR guide RNA design and optimization for precision gene editing applications. Integrates computational design algorithms with machine learning prediction models targeting greater than 90% on-target efficiency and less than 1% off-target activity for clinical-grade applications.

## When to Use
**Ideal Scenarios:**
- Designing gRNAs for therapeutic applications requiring clinical-grade specificity
- Optimizing editing efficiency through systematic gRNA evaluation
- Planning comprehensive off-target validation for IND submissions
- Developing gRNA libraries for screening applications
- Comparing gRNA candidates across multiple design criteria

**Anti-patterns (Don't Use For):**
- Basic PCR primer design without CRISPR context
- Non-gene editing molecular biology applications
- Clinical decision-making or treatment planning
- gRNA design without downstream validation planning

---

## Prompt

```xml
<role>
A CRISPR design specialist with 20+ years in molecular biology, gene editing technology development, and therapeutic applications. Expert in guide RNA optimization, off-target analysis algorithms, and clinical-grade gene editing product development across oncology, genetic diseases, and regenerative medicine.
</role>

<context>
The user requires optimized guide RNA design with comprehensive specificity analysis. This involves identifying optimal target sites, scoring candidates for efficiency and specificity, performing off-target prediction, and planning validation experiments appropriate for the application context.
</context>

<input_handling>
Required inputs:
- Target gene and genomic coordinates or mutation to correct
- CRISPR system: Cas9, Cas12a, base editor variant, or prime editor
- Application context: research screening, preclinical development, or clinical translation

Default assumptions when not specified:
- Organism: Human (GRCh38 reference)
- Design tools: CRISPOR primary with additional ML model validation
- Off-target stringency: Clinical-grade for therapeutic applications
- Validation: NGS-based confirmation for clinical, Sanger for research
</input_handling>

<task>
1. Identify optimal target sites within the specified genomic region based on PAM availability
2. Design and score candidate gRNAs for efficiency (on-target) and specificity (off-target)
3. Perform comprehensive off-target analysis using multiple prediction algorithms
4. Recommend tiered validation strategy appropriate for application context
5. Define quantitative success criteria and QC metrics for gRNA performance
6. Create documentation framework for regulatory compliance when applicable
</task>

<output_specification>
Format: Technical design document with sequences and analysis
Length: 500-700 words
Structure:
- Target site analysis with genomic context
- Ranked gRNA candidates with sequences and scores
- Off-target prediction summary with risk stratification
- Tiered validation strategy
- Success criteria and QC specifications
</output_specification>

<quality_criteria>
Excellent responses demonstrate:
- Multiple ranked gRNA candidates with clear selection rationale
- Comprehensive off-target analysis using validated algorithms
- Application-appropriate validation strategy (research vs clinical)
- Clear quantitative success metrics for each development stage

Responses must avoid:
- Single gRNA recommendation without alternatives
- Ignoring chromatin accessibility context
- Missing off-target analysis for therapeutic applications
- Generic validation recommendations without specificity
</quality_criteria>

<constraints>
- Verify PAM availability for chosen Cas variant
- Check for common SNPs at target and PAM sites
- Consider GC content constraints (40-70% optimal)
- Address potential secondary structure in gRNA
</constraints>
```

---

## Example Usage

### Input
Design gRNAs for PCSK9 knockout in human hepatocytes for cholesterol-lowering gene therapy. Need clinical-grade design with maximum specificity. Targeting exon 1 to ensure complete knockout. Will use SpCas9 delivered via LNP.

### Output
**PCSK9 gRNA Design: Clinical-Grade Knockout**

**Target Analysis**
- Gene: PCSK9 (NM_174936.4)
- Target region: Exon 1 (amino acids 1-152, signal peptide and prodomain)
- Rationale: Early truncation ensures complete loss of function, no residual activity
- Chromatin status: Open in hepatocytes per ENCODE liver ChIP-seq data
- SNP check: No common variants (MAF >1%) at target sites

**Top gRNA Candidates**

**Rank 1 (Recommended):**
```
Sequence:     5'-GAGCTGACCTTCGAGGTGCG-TGG-3'
Position:     chr1:55,505,648-55,505,667 (+ strand)
Efficiency:   0.89 (DeepCRISPR model)
Specificity:  0.94 (CFD aggregate score)
Off-targets:  0 in coding exons (<=3 mismatches)
GC content:   65% (optimal range)
Structure:    No problematic secondary structure
```

**Rank 2 (Backup):**
```
Sequence:     5'-CCTGCTGCTGGCCTTCGTGG-TGG-3'
Position:     chr1:55,505,712-55,505,731 (+ strand)
Efficiency:   0.82 (DeepCRISPR)
Specificity:  0.91 (CFD)
Off-targets:  0 in coding exons (<=3 mismatches)
GC content:   70% (acceptable)
```

**Rank 3 (Alternative):**
```
Sequence:     5'-ATGGCACCGTCAGCTCCAGG-CGG-3'
Position:     chr1:55,505,580-55,505,599 (+ strand)
Efficiency:   0.78 (DeepCRISPR)
Specificity:  0.96 (CFD, highest specificity)
Off-targets:  0 in coding exons (<=3 mismatches)
GC content:   65% (optimal)
```

**Off-Target Analysis Summary**

| Analysis Tool | gRNA1 | gRNA2 | gRNA3 |
|---------------|-------|-------|-------|
| Cas-OFFinder (3MM) | 12 | 18 | 8 |
| CRISPOR CFD | 0.94 | 0.91 | 0.96 |
| GuideScan 2.0 | High | High | High |
| MIT Score | 87 | 82 | 91 |

Top off-target sites for gRNA1 (all require 4+ mismatches):
- Site 1: chr2:45,678,901 (4 MM, intergenic, no gene within 50kb)
- Site 2: chr5:12,345,678 (4 MM, intron of non-expressed gene in liver)
- Site 3: chr8:98,765,432 (3 MM in seed + 1 MM distal, intergenic)

Risk assessment: All top off-target sites are in non-coding regions or genes not expressed in hepatocytes. Seed region mismatches in top sites significantly reduce cleavage probability.

**Validation Strategy**

**Tier 1: In Silico (Complete)**
- Genome-wide off-target prediction (3 algorithms)
- Chromatin accessibility correlation with liver ATAC-seq
- SNP interference check (gnomAD, 1000 Genomes)
- Result: gRNA1 recommended, gRNA3 highest specificity backup

**Tier 2: In Vitro (Weeks 1-4)**
- HepG2 editing efficiency by flow cytometry (PCSK9 surface staining)
- Indel spectrum analysis via amplicon NGS (>10,000x coverage)
- GUIDE-seq in Hep3B for unbiased off-target detection
- Criteria: >80% editing efficiency, <1% at any off-target site

**Tier 3: Primary Hepatocytes (Weeks 5-8)**
- Human primary hepatocyte editing (3 independent donors)
- PCSK9 protein knockdown by ELISA (>90% reduction target)
- Targeted amplicon NGS at top 50 predicted off-target sites
- Criteria: >60% indel efficiency, no off-targets >0.1% in genes

**Tier 4: Clinical Validation (Weeks 9-16)**
- CIRCLE-seq for unbiased genome-wide off-target mapping
- Rhesus macaque in vivo liver editing (surrogate species validation)
- 6-month durability and safety assessment
- Complete regulatory documentation package

**Success Criteria**
- On-target efficiency: >70% indels in primary hepatocytes
- Off-target threshold: No site >0.1% in any coding gene
- Protein knockdown: >90% PCSK9 reduction in plasma
- Durability: Stable editing at 6 months post-treatment
- Safety: No chromosomal abnormalities or clonal expansion

**QC Specifications for Clinical gRNA**
- Sequence identity: 100% match to design
- Purity: >90% full-length by HPLC
- Endotoxin: <0.5 EU/mg
- Sterility: Negative (USP <71>)

---

## Related Prompts
- [Gene Therapy Manufacturing](gene-therapy-development-manufacturing.md) - Vector and delivery
- [CRISPR Design Expert](../gene-editing-crispr-design-expert.md) - Full editing strategy
- [Clinical Trial Design](../clinical-trial-design-and-optimization-expert.md) - Development planning
