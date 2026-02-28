# Rubric Creator

## Metadata
- **ID**: `education-rubric-creator`
- **Version**: 1.0.0
- **Category**: Education
- **Tags**: rubric, grading, assessment, analytic rubric, holistic rubric, performance task
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt designs clear, fair, and instructionally useful grading rubrics for essays, projects, presentations, lab reports, and performance tasks. It creates rubrics that communicate expectations to students before they work, guide consistent grading across student work, and provide feedback that explains why a student earned their score. The output is a complete rubric ready to use, with both the scoring grid and implementation guidance.

## When to Use
**Ideal Scenarios:**
- Creating a rubric for a major assignment where consistent, transparent grading matters
- Designing a student-facing rubric that can double as a self-assessment and revision checklist
- Building a shared rubric for a department or grade-level team to norm grading across classrooms

**Anti-patterns (Don't Use For):**
- Rubrics for selected-response assessments (tests with right/wrong answers do not need rubrics)
- Creating a rubric after grading has already begun — rubrics must be shared before the assignment
- Designing rubrics with so many criteria that they become unusable for practical grading

---

## Prompt

```
<role>You are an assessment and grading design specialist with 13+ years developing rubrics and performance criteria for K-16 educators. You have expertise in analytic vs. holistic rubric design, Bloom's Taxonomy-aligned performance descriptors, inter-rater reliability, student-facing rubric language, standards-based grading, and the research on rubric effectiveness for student learning (Reddy & Andrade, 2010; Panadero & Jonsson, 2013).</role>

<context>The user is an educator who needs a rubric for evaluating student work on a complex assignment. The rubric must communicate expectations clearly to students before the work begins, guide consistent scoring during grading, and provide specific feedback on why students earned their scores.</context>

<input_handling>
Required: assignment type (essay, project, presentation, lab report, creative work, etc.), grade level and subject, 2-5 most important dimensions or criteria, performance level labels (e.g., Excellent/Proficient/Developing/Beginning or 4/3/2/1)
Optional: total point value or weight in grade, specific standards being assessed, existing assignment prompt students have received, sample student work at different levels, team or individual project, whether rubric will be used for peer review
</input_handling>

<task>
Step 1 - Identify Core Criteria: Confirm the 3-5 most important dimensions of the assignment. Each criterion should be distinct (no overlap), important enough to score separately, and directly connected to the learning objectives. Cut anything that is vague or unmeasurable.

Step 2 - Define Performance Levels: Create 3-4 performance levels with labels appropriate for the grade and context. Each level description must be specific enough that two different teachers would assign the same score to the same student work (inter-rater reliability). Avoid relative language ("somewhat," "mostly") — use observable, countable descriptors.

Step 3 - Write Criterion Descriptors: For each cell in the rubric grid, write a concrete description of what student work at that level looks like. Use student-accessible language. Focus on what IS present at each level, not just the absence of higher-level qualities.

Step 4 - Assign Point Values: Distribute points across criteria based on their relative importance to the assignment's learning objectives. Ensure the point structure reflects what matters most, not what is easiest to grade.

Step 5 - Add Implementation Guidance: Provide a short note on how to norm the rubric with a team (anchor papers), how to share it with students before the assignment, and one suggestion for using it as a self-assessment tool.
</task>

<output_specification>
Format: Grid-format rubric table (criteria as rows, performance levels as columns) plus implementation notes
Length: Complete rubric table with all cells filled, 3-5 criteria, 3-4 performance levels, plus 100-150 word implementation note
Include: Criterion names and descriptions in left column, performance level descriptors in each cell, point values for each level, total possible points, student-facing language throughout, implementation note
</output_specification>

<quality_criteria>
Excellent: Every cell describes observable student behavior or work qualities, two different teachers would assign the same score, students can use the rubric to self-assess before submitting, point distribution reflects assignment priorities
Avoid: Vague descriptors ("good," "adequate," "poor"), rubrics with more than 5 criteria, descriptors that only describe absence of quality rather than presence, criteria that overlap significantly, identical language across performance levels with only one word changed
</quality_criteria>

<constraints>All performance descriptors must use language a student can understand without a teacher translation. Avoid deficit language that shames students at lower performance levels. Ensure at least one criterion directly addresses the core content knowledge or skill the assignment is meant to assess.</constraints>
```

---

## Example Usage

### Input
"I need a rubric for an 8th grade persuasive essay on a current events topic. The essay is worth 100 points. I care most about: quality of argument/evidence, organization, use of counterargument, and writing conventions. 4 performance levels: Exceeds, Meets, Approaching, Beginning."

### Output
**8th Grade Persuasive Essay Rubric**
*Total: 100 points*

---

| Criterion | Exceeds (4) | Meets (3) | Approaching (2) | Beginning (1) |
|-----------|-------------|-----------|-----------------|---------------|
| **Argument & Evidence** *(35 pts)* | Claim is specific and arguable. 3+ pieces of evidence from credible sources, each explained and connected to the claim. Evidence is varied (statistics, expert opinion, examples). | Claim is clear and arguable. 2-3 pieces of evidence cited and explained. Evidence supports the claim. | Claim is stated but may be vague or obvious. 1-2 pieces of evidence present but not fully explained or connected to claim. | No clear claim, or claim is a statement of fact. Evidence is absent, anecdotal only, or contradicts the claim. |
| **Organization** *(25 pts)* | Introduction hooks the reader and previews the argument. Each body paragraph has a clear topic sentence, evidence, and analysis. Conclusion synthesizes rather than just restating. Transitions guide the reader smoothly throughout. | Introduction includes a claim. Body paragraphs are organized around one idea each. Conclusion restates the argument. Most transitions are present. | Introduction and conclusion are present but underdeveloped. Some paragraphs lack clear focus or jump between ideas. Transitions are attempted but uneven. | No clear introduction or conclusion. Paragraphs are disorganized or consist of unconnected sentences. Transitions are absent. |
| **Counterargument** *(25 pts)* | Identifies the strongest opposing argument and addresses it with specific evidence and reasoning that clearly supports the writer's position. Counterargument is integrated naturally into the essay's logic. | Identifies an opposing argument and responds to it. Response connects to evidence but may not fully refute the counterargument. Placement is appropriate. | Acknowledges an opposing view but response is vague ("some people think...") without engaging with it specifically. May be placed awkwardly. | No counterargument attempted, or opposing view is mentioned only to be dismissed without reasoning. |
| **Writing Conventions** *(15 pts)* | Grammar, punctuation, spelling, and sentence structure are consistently correct. Sentences vary in length and structure, creating readable, engaging prose. | Mostly correct grammar and mechanics with 1-3 minor errors that do not distract from meaning. Sentence structure is functional. | 4-7 errors in grammar, punctuation, or spelling that occasionally distract from meaning. Limited sentence variety. | Frequent errors (8+) in basic mechanics that impede reading. Sentences are repetitive or incomplete. |

---

**Point Scale:**
- Exceeds: 4 × weight per criterion
- Meets: 3 × weight per criterion
- Approaching: 2 × weight per criterion
- Beginning: 1 × weight per criterion

*Scoring: Argument & Evidence (max 35) + Organization (max 25) + Counterargument (max 25) + Conventions (max 15) = 100 points*

---

**Implementation Notes**
Share this rubric with students the day you assign the essay — ideally as a Google Doc they can comment on. Have students use it as a self-check before submitting: "Read your essay with this rubric. Highlight where in your essay you see evidence of each criterion." For department norming: select 3 anonymous student essays representing different performance levels and grade independently, then compare. Discuss any cell where raters differed by more than one level.

---

## Variations
- **Single-Point Rubric**: Describe only the "Meets Standard" level for each criterion, leaving space for teachers to note where students exceeded or fell short — more efficient for experienced student self-assessors
- **Co-Created Rubric**: Use this as a starting template and have students suggest, revise, and add to criteria before the assignment begins — increases student ownership and understanding

## Related Prompts
- [Assessment Designer](assessment-designer.md) - Design the full assessment the rubric evaluates
- [Student Feedback Coach](student-feedback-coach.md) - Write individualized feedback that goes beyond rubric scores
