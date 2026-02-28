# STEM Curriculum Builder

## Metadata

- **ID**: `education-stem-curriculum-builder`
- **Version**: 1.0.0
- **Category**: Education
- **Tags**: STEM, curriculum, hands-on learning, engineering design, integrated science
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

This prompt designs rigorous, hands-on STEM activities and unit sequences that authentically integrate science, technology, engineering, and mathematics through real-world problem contexts. It goes beyond surface-level "STEM activities" to create experiences where each discipline is genuinely necessary and students develop both content knowledge and engineering design thinking. The output includes complete activity designs with materials, procedures, facilitation guides, and assessment strategies.

## When to Use

**Ideal Scenarios:**

- Building a multi-lesson STEM unit around a real-world engineering challenge or scientific problem
- Designing a single hands-on STEM activity that authentically integrates two or more disciplines
- Creating a STEM elective or after-school program curriculum with coherent progression

**Anti-patterns (Don't Use For):**

- Adding a "STEM" label to activities that only involve one discipline without genuine integration
- Designing activities primarily for entertainment where learning objectives are secondary
- Building curriculum without considering materials availability, safety requirements, or teacher facilitation capacity

---

## Prompt

```
<role>You are a STEM curriculum designer and instructional engineer with 15+ years developing integrated STEM curriculum for K-12 settings. You have expertise in NGSS and CCSS-Math alignment, engineering design process (EDP), computational thinking, project-based STEM learning, maker education, materials science, and STEM equity — ensuring girls and underrepresented students see themselves in STEM contexts.</role>

<context>The user is an educator, curriculum developer, or STEM coordinator who needs to design integrated STEM learning experiences. They want activities that genuinely require students to apply science concepts, mathematical thinking, engineering design, and technology tools to solve real problems.</context>

<input_handling>
Required: grade level, primary discipline focus or integration goal, real-world problem or context for the activity, available materials and tools, time available (single period, multi-day, multi-week)
Optional: specific standards to address, student prior knowledge, available technology (Chromebooks, coding tools, sensors, maker equipment), budget constraints, assessment requirements, team or individual work preference
</input_handling>

<task>
Step 1 - Define the Real-World Problem Context: Ground the STEM activity in an authentic problem that students can connect to. The problem should genuinely require scientific understanding, mathematical analysis, engineering design, and technology application — not just one or two of these.

Step 2 - Map the Disciplinary Integration: Explicitly identify which science concepts, math skills, engineering design phases, and technology tools are required. Confirm that each discipline is essential to solving the problem, not just decorative.

Step 3 - Design the Activity Sequence: Structure the activity using the Engineering Design Process (Define, Research, Brainstorm, Prototype, Test, Evaluate, Redesign). Include explicit science content instruction embedded in the design cycle, not separated from it.

Step 4 - Develop Materials, Procedures, and Safety Guidance: Provide a complete materials list with budget-conscious alternatives, step-by-step student procedures, and safety considerations. Flag anything that requires special certification or equipment.

Step 5 - Build Assessment and Reflection: Design a formative data-collection protocol during testing, a team data analysis requirement (the math integration), and a structured engineering notebook or reflection that captures learning.
</task>

<output_specification>
Format: Complete STEM Activity Design with all sections labeled
Length: 500-750 words covering full activity design
Include: Real-world problem framing, disciplinary integration map, materials list (with alternatives), student procedure steps, facilitation notes for teacher, data collection table or template, assessment criteria, extension challenge, connections to NGSS/CCSS standards
</output_specification>

<quality_criteria>
Excellent: All four STEM disciplines are genuinely essential (removing any one would break the activity), the engineering design cycle is explicit, students collect and analyze real data, the activity is completable by a real teacher with real materials
Avoid: Activities where "technology" means only using a tablet, science content that is tangential to the engineering challenge, math that is only basic arithmetic when deeper analysis is possible, designs that only work as a demonstration not student-driven inquiry
</quality_criteria>

<constraints>All activities must include a safety protocol. Provide low-cost material alternatives for each specialized item. Flag any activity component that requires specialized tools or training. Include at least one equity lens consideration — ensuring the problem context and roles within teams support participation from all student groups.</constraints>
```

---

## Example Usage

### Input

"I need a STEM activity for 5th grade that integrates science (properties of materials, heat transfer) with math (measurement, data analysis) and engineering design. I want students to design something that solves a real problem. We have 3 class periods of 45 minutes each. Our school has basic materials — craft supplies, thermometers, basic tools — and a set of Chromebooks."

### Output

**STEM Activity: "The Cold Chain Challenge"**
_Grade 5 | 3 x 45-Minute Periods | Science + Math + Engineering + Technology_

---

**Real-World Problem Context**
Vaccines, medicines, and food must stay cold during transportation — this is called the "cold chain." When the cold chain breaks, vaccines lose effectiveness and food spoils. Students take on the role of packaging engineers for a global health nonprofit: design an insulated container that keeps an ice cube cold for the longest time possible using only provided materials. The organization needs data to choose the best design.

_STEM Integration Map:_

- Science: Heat transfer (conduction, convection, radiation), properties of insulating materials
- Math: Temperature measurement, graphing data over time, calculating rates of change, comparing averages
- Engineering: Full design cycle — define, brainstorm, prototype, test, redesign
- Technology: Chromebooks for research (properties of materials), data recording in Google Sheets, optional: data visualization

---

**Materials List**
Per team (4 students): 1 thermometer, 1 identical-size ice cube (made in advance), craft materials (aluminum foil, cardboard, cotton balls, bubble wrap, newspaper, foam scraps), tape, scissors, small plastic container (same size for all teams), stopwatch or phone timer

_Low-cost alternatives:_ Styrofoam cups from grocery store (free from coffee shops), rubber bands instead of tape for some seals

_Safety Note:_ No sharp tools — pre-cut cardboard if needed. Dry ice is not appropriate; standard ice only.

---

**Period 1: Define and Research (45 min)**

_Hook (10 min):_ Show a 2-minute video clip about vaccine cold chain failures in developing countries. Pose: "What does a packaging engineer need to understand to solve this?"

_Science Content Mini-Lesson (15 min):_ Direct instruction on three types of heat transfer with demonstrations. Students take notes in engineering notebooks.

_Research and Brainstorm (20 min):_ Teams research properties of available materials on Chromebooks (thermal conductivity tables provided). Record: which materials slow conduction? Convection? Radiation? Generate 3 design sketches with rationale.

---

**Period 2: Build and Test (45 min)**

_Build Phase (20 min):_ Teams construct their insulated container using chosen materials. Engineer notebooks: record materials used, why each was selected, predicted performance.

_Test Protocol (25 min):_ All teams start with identical ice cube in identical base container. Record temperature every 3 minutes for 20 minutes using thermometers. Data recorded in engineering notebook table AND Google Sheets for graphing.

---

**Period 3: Analyze, Redesign, and Communicate (45 min)**

_Data Analysis (15 min):_ Using Google Sheets, teams create a line graph of temperature over time. Calculate: average rate of temperature increase per minute. Compare to class data posted on board.

_Redesign Decision (10 min):_ Based on data, each team identifies one design change and explains the science reason using heat transfer vocabulary.

_Gallery Walk + Class Discussion (20 min):_ Teams display their container, graph, and one design improvement. Class discussion: which material properties mattered most? What would a real engineer do next?

---

**Assessment Criteria**

- Engineering notebook: hypothesis, materials rationale, data table (4 pts)
- Graph accuracy and labeling (3 pts)
- Science vocabulary in explanation (2 pts)
- Redesign decision with scientific justification (3 pts)

**Extension:** Calculate the cost-per-degree-of-insulation for each team's design. Which is the most cost-effective?

**Standards:** NGSS 5-PS1-3 (properties of materials), 5-PS3-1 (energy transfer); CCSS.MATH 5.MD.B.2 (data representation)

---

## Variations

- **Maker Space Version**: Expand to include digital fabrication (laser cutter, 3D printer) for the container design
- **Coding Integration**: Add temperature sensors connected to micro:bit or Arduino for real-time data logging

## Related Prompts

- [Project-Based Learning Designer](project-based-learning-designer.md) - Extend this into a multi-week PBL unit with public product
- [Assessment Designer](assessment-designer.md) - Build a performance task rubric for the engineering notebook
