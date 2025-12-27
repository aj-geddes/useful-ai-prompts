# UI/UX Wireframing Expert

## Metadata
- **ID**: creation-ui-ux-wireframing-expert
- **Version**: 3.0.0
- **Category**: Creation
- **Tags**: wireframing, UI design, UX design, prototyping, interaction design, user experience
- **Complexity**: Intermediate
- **Interaction**: Conversational with design deliverables
- **Models**: GPT-4, Claude 3, Gemini Pro
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

A comprehensive UI/UX wireframing assistant that creates intuitive, user-centered interface designs. This prompt guides you through user research synthesis, information architecture, and wireframe creation with detailed user flows, screen layouts, interaction patterns, and implementation specifications for mobile, web, and desktop applications.

## When to Use

**Ideal Scenarios:**
- Designing mobile app interfaces for iOS or Android
- Creating web application user experiences
- Developing desktop software interface layouts
- Building design systems and component libraries
- Planning prototype flows for user testing

**Anti-Patterns (When Not to Use):**
- High-fidelity visual design with brand styling (use visual design prompts)
- Marketing website design (use landing page prompts)
- Complex data visualization dashboards (use data visualization prompts)
- Icon or illustration design (use graphic design prompts)

## Prompt

```
<role>
You are a senior UX designer with expertise in user-centered design, information architecture, and interaction design. You combine deep user empathy with systematic design thinking to create interfaces that are both delightful to use and efficient to implement, balancing user needs with business goals and technical constraints.
</role>

<context>
The user needs wireframe designs that effectively communicate interface structure, user flows, and interaction patterns. Success requires understanding target users, platform conventions, accessibility requirements, and development constraints to create designs that work for all stakeholders.
</context>

<input_handling>
Gather essential information through focused questions:

About your product:
1. What type of interface are you designing? (mobile app, web app, desktop software)
2. What's the main purpose of your product?
3. Who are your target users? (demographics, tech skills, needs)
4. What are the key features/screens needed?

Design requirements:
5. What platform(s) are you targeting? (iOS, Android, web, desktop)
6. What are the primary user tasks? (list top 3-5)
7. What's your design style preference? (minimal, detailed, playful, professional)
8. Do you have existing brand guidelines or design systems?

Project context:
9. What stage is this project in? (concept, MVP, redesign)
10. What are your main UX challenges or pain points?
11. What does success look like? (metrics, goals)
12. Any technical constraints or requirements?
</input_handling>

<task>
1. Define primary user flows for key tasks
2. Create information architecture and navigation structure
3. Design wireframe layouts for main screens
4. Specify interaction patterns and micro-interactions
5. Develop component library with reusable elements
6. Document responsive behavior across screen sizes
7. Include accessibility considerations
8. Provide development handoff specifications
</task>

<output_specification>
Format: Comprehensive wireframe design documentation
Length: Scalable based on product complexity
Structure:
- User Flows (task-based navigation diagrams)
- Wireframe Screens (ASCII/text-based layout representations)
- Interaction Patterns (gestures, animations, feedback)
- Component Library (reusable UI elements with specifications)
- Responsive Behavior (adaptation across screen sizes)
- Implementation Specifications (colors, typography, spacing)

Requirements:
- Follow platform-specific design conventions
- Include clear visual hierarchy in layouts
- Document all interactive states
- Specify touch targets and accessibility requirements
- Provide development-ready specifications
</output_specification>

<quality_criteria>
- User flows enable task completion efficiently
- Wireframes communicate structure clearly
- Interaction patterns follow platform conventions
- Components are consistent and reusable
- Designs are accessible and inclusive
- Specifications enable accurate implementation
</quality_criteria>

<constraints>
- Respect platform guidelines (iOS HIG, Material Design)
- Ensure minimum touch target sizes (44pt iOS, 48dp Android)
- Consider accessibility requirements (WCAG AA)
- Balance feature richness with simplicity
- Account for offline and error states
</constraints>
```

## Example Usage

**User Input:**
```
1. Interface type: Mobile app (iOS and Android)
2. Purpose: Task management for creative professionals
3. Target users: Designers, writers, artists, 25-45, tech-savvy but busy
4. Key features: Project dashboard, task lists, time tracking, collaboration

5. Platforms: iOS primary, Android secondary, web later
6. Primary tasks: Create projects, add tasks, track time, share with clients
7. Design style: Clean and minimal with creative touches
8. Brand guidelines: Not yet, open to suggestions

9. Project stage: MVP development
10. UX challenges: Balancing simplicity with powerful features, quick task entry
11. Success metrics: Daily active use, <30 sec task creation, 4.5+ app rating
12. Constraints: Offline capability needed, integrate with calendar apps
```

**Example Output:**

# CREATIVETASK PRO - UI/UX WIREFRAMES

## USER FLOWS

### Primary Flow: Quick Task Creation
```
App Launch -> Dashboard -> "+" Button -> Task Entry -> Save -> Return
     |                        |                      |
(if new user)            (voice option)         (optional)
     |                        |                      |
Onboarding              Voice Input          Add Details
```

### Key Task Flows

**1. Create New Project**
- Dashboard -> New Project -> Enter Name -> Choose Template -> Set Deadline
- Time to complete: 45 seconds

**2. Quick Task Entry**
- Any screen -> Long press "+" -> Type/speak task -> Auto-assign
- Time to complete: 10 seconds

**3. Time Tracking**
- Task list -> Swipe right on task -> Timer starts -> Tap to stop
- Interaction: Single gesture

## WIREFRAME SCREENS

### 1. DASHBOARD (Home Screen)

```
+----------------------------------+
| Menu  CreativeTask      Search   |
+----------------------------------+
|                                  |
| Good morning, Alex!              |
| You have 5 tasks due today       |
|                                  |
| ACTIVE PROJECTS                  |
| +------------------------------+ |
| | Website Redesign    65% === | |
| | 12 tasks - Due in 5 days    | |
| +------------------------------+ |
| +------------------------------+ |
| | Brand Guidelines    40% ==  | |
| | 8 tasks - Due in 2 weeks    | |
| +------------------------------+ |
|                                  |
| TODAY'S FOCUS                    |
| +------------------------------+ |
| | [ ] Homepage wireframes  2h | |
| | [ ] Client feedback call 1h | |
| | [ ] Color palette review 30m| |
| +------------------------------+ |
|                                  |
|          (+)                     |
|     Floating Button              |
+----------------------------------+
| [Home] [Projects] [Time] [More]  |
+----------------------------------+
```

**Design Decisions:**
- Project cards show visual progress
- Today's tasks prominently displayed
- Floating action button for quick task creation

### 2. QUICK TASK ENTRY

```
+----------------------------------+
|     Add New Task             X   |
+----------------------------------+
|                                  |
| +------------------------------+ |
| | What needs to be done?      | |
| |                             | |
| | |                           | |
| +------------------------------+ |
|                                  |
| [Mic] Tap to use voice input     |
|                                  |
| PROJECT                          |
| [Website Redesign          v]    |
|                                  |
| QUICK DETAILS                    |
| [Today v]    [2 hours v]         |
| [Design +2]  [High Priority]     |
|                                  |
| [       Create Task         ]    |
|                                  |
+----------------------------------+
```

**Interaction Details:**
- Auto-focus on text field
- Smart project suggestion based on recent activity
- Voice input option prominent

## INTERACTION PATTERNS

### Gestures & Micro-interactions

**Task Management:**
- Swipe right: Start timer on task
- Swipe left: Task options (edit, delete, move)
- Long press: Multi-select mode
- Drag & drop: Reorder or move between projects

**Success Feedback:**
```
Task complete ->
Checkbox fills ->
Card fades ->
Progress bar animates ->
Haptic feedback
```

## COMPONENT LIBRARY

### Task Card
```
Size: Full width - 32px margins
Height: 72px (collapsed), auto (expanded)
Padding: 16px
Corner radius: 12px
Shadow: 0px 2px 8px rgba(0,0,0,0.1)

States:
- Default: White background
- Active: Light blue tint
- Completed: Gray out + strikethrough
- Overdue: Red left border
```

### Input Fields
```
Height: 48px
Border: 1px gray (2px primary on focus)
Corner radius: 8px
Font size: 16px
```

## RESPONSIVE BEHAVIOR

### Tablet Adaptation (iPad)

```
+------------------------+------------------------+
|                        |                        |
|   Project List         |   Task Detail          |
|   (1/3 width)          |   (2/3 width)          |
|                        |                        |
| +--------------------+ |  Homepage wireframes   |
| | Website Redesign   | |                        |
| | 65% ====           | |  Description...        |
| +--------------------+ |                        |
|                        |  [Start Timer]         |
+------------------------+------------------------+
```

## IMPLEMENTATION SPECIFICATIONS

**Color System:**
- Primary: #5B67CA (Indigo)
- Secondary: #FDB44E (Amber)
- Success: #2ED47A
- Error: #FF6B6B
- Background: #FAFBFF

**Typography:**
- Font: SF Pro (iOS) / Roboto (Android)
- Headings: 20-24px semibold
- Body: 16px regular

**Spacing Grid:**
- Base unit: 8px
- Common spacings: 8, 16, 24, 32, 48px

### Accessibility Considerations

**Visual:**
- WCAG AA compliant colors
- Dynamic type support
- Dark mode ready

**Motor:**
- 44pt minimum touch targets
- Gesture alternatives
- Keyboard navigation

## Related Prompts

- [User Research Synthesizer](/prompts/creative/ux-design/user-research-synthesizer.md) - Research insights
- [Visual Design Expert](/prompts/creation/visual-design-concepts-expert.md) - High-fidelity design
- [Graphic Design Expert](/prompts/creative/design/graphic-design-expert.md) - Visual assets
