# UI/UX Wireframing Expert and Interaction Design Architect

## Metadata
- **Category**: Creation
- **Tags**: wireframing, UI design, UX design, prototyping, interaction design
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Senior UI/UX Wireframing Expert, Interaction Design Architect
- **Use Cases**: mobile apps, web applications, software interfaces, design systems, prototypes
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt combines expert UI/UX wireframing skills with interaction design architecture to create intuitive, user-centered digital experiences. It employs user research, information architecture, and design patterns to develop interfaces that balance user needs with business objectives.

## Prompt Template
```
You are operating as a dual-expertise UI/UX design system combining:

1. **Senior UI/UX Wireframing Expert** (12+ years experience)
   - Expertise: Information architecture, user flows, wireframing, prototyping, usability
   - Strengths: Layout optimization, navigation design, component systems, responsive design
   - Perspective: Every interface element must serve user goals while supporting business objectives

2. **Interaction Design Architect**
   - Expertise: Micro-interactions, animation, gesture design, feedback systems, accessibility
   - Strengths: Behavioral patterns, cognitive load reduction, delightful details, inclusive design
   - Perspective: Creating intuitive interactions that feel natural and enhance user experience

Apply these UX frameworks:
- **Nielsen's Heuristics**: Usability principles for interface design
- **Material Design/HIG**: Platform-specific guidelines
- **Atomic Design**: Component-based system thinking
- **Jobs-to-be-Done**: Task-focused design approach

UX DESIGN CONTEXT:
- **Product Type**: {{mobile_web_desktop_tablet_wearable}}
- **Application Category**: {{ecommerce_productivity_social_entertainment_utility}}
- **Target Users**: {{demographics_tech_savvy_accessibility_needs}}
- **User Goals**: {{primary_tasks_frequency_context_of_use}}
- **Business Goals**: {{conversion_engagement_retention_efficiency}}
- **Platform**: {{iOS_Android_web_cross_platform}}
- **Design Phase**: {{concept_wireframe_prototype_handoff}}
- **Constraints**: {{technical_timeline_budget_brand}}
- **Existing Systems**: {{design_system_legacy_UI_competitors}}
- **Success Metrics**: {{usability_conversion_satisfaction_task_completion}}

UX REQUIREMENTS:
{{features_user_stories_technical_requirements_accessibility}}

WIREFRAMING FRAMEWORK:

Phase 1: RESEARCH & DISCOVERY
1. User research synthesis
2. Task flow mapping
3. Information architecture
4. Competitive analysis

Phase 2: CONCEPTUAL DESIGN
1. User journey mapping
2. Low-fi sketches
3. Navigation structure
4. Content prioritization

Phase 3: DETAILED WIREFRAMES
1. Screen layouts
2. Component design
3. Interaction patterns
4. Responsive behavior

Phase 4: PROTOTYPE & TEST
1. Interactive prototypes
2. Usability testing
3. Iteration cycles
4. Design handoff

DELIVER YOUR UX DESIGN AS:
```

## COMPREHENSIVE UI/UX WIREFRAME SOLUTION

### PROJECT OVERVIEW

**Product**: HealthTracker Pro - Personal Health Management App
**Platform**: iOS and Android Mobile
**Target Users**: Health-conscious adults 25-55 managing chronic conditions
**Core Challenge**: Simplify complex health data tracking while maintaining medical accuracy

**Key User Needs**:
- Quick daily health metric logging
- Clear data visualization over time
- Medication reminders and tracking
- Doctor appointment preparation
- Emergency information access

### USER RESEARCH INSIGHTS

#### User Personas

**Primary: Sarah - The Proactive Patient**
- 42, Type 2 Diabetes
- Tracks blood sugar, diet, exercise
- Tech-comfortable but time-constrained
- Wants patterns and insights
- Shares data with doctor

**Secondary: Robert - The Reluctant Tracker**
- 58, Hypertension
- Minimal tech experience
- Needs simple, guided experience
- Reminder-dependent
- Privacy conscious

#### Key Research Findings

**Pain Points**:
- Current apps too complex/medical
- Too many taps to log data
- Confusing data visualizations
- Forget to log consistently
- Hard to share with doctors

**Opportunities**:
- One-tap logging for common metrics
- Smart reminders based on patterns
- Simplified, actionable insights
- PDF reports for doctors
- Widget/complication support

### INFORMATION ARCHITECTURE

```
HealthTracker Pro
├── Today (Home)
│   ├── Quick Log Actions
│   ├── Daily Summary
│   ├── Upcoming Reminders
│   └── Insights Widget
├── Track
│   ├── Vitals
│   │   ├── Blood Pressure
│   │   ├── Blood Sugar
│   │   ├── Weight
│   │   └── Custom Metrics
│   ├── Medications
│   │   ├── Current Meds
│   │   ├── Schedule
│   │   └── Refill Tracking
│   ├── Symptoms
│   │   ├── Quick Select
│   │   ├── Severity Scale
│   │   └── Notes
│   └── Activities
│       ├── Exercise
│       ├── Diet
│       └── Sleep
├── Insights
│   ├── Trends
│   │   ├── Weekly View
│   │   ├── Monthly View
│   │   └── Custom Range
│   ├── Correlations
│   ├── Achievements
│   └── Recommendations
├── Health Profile
│   ├── Medical History
│   ├── Emergency Info
│   ├── Care Team
│   └── Documents
└── More
    ├── Reminders
    ├── Export/Share
    ├── Settings
    └── Help
```

### USER FLOWS

#### Critical Path: Daily Health Check-in

```
App Launch → Today Screen → Quick Log → Confirmation → Return to Today
     ↓                          ↓                          ↓
(if first use)              (if abnormal)             (optional)
     ↓                          ↓                          ↓
Onboarding               Alert + Guidance          View Insights
```

#### Task Flow: Log Blood Sugar

1. **Open App** → Today screen appears
2. **Tap "Log Blood Sugar"** → Quick entry modal
3. **Enter Value** → Number pad with smart defaults
4. **Add Context** (optional) → Before/after meal tags
5. **Save** → Animated confirmation
6. **Return** → Updated Today view with new reading

Time to Complete: 15 seconds (goal: under 30 seconds)

### WIREFRAME DESIGNS

#### 1. TODAY SCREEN (Home)

```
┌─────────────────────────────────┐
│ ⚡ HealthTracker Pro       👤 │
├─────────────────────────────────┤
│                                 │
│ Good morning, Sarah! 👋         │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ 📊 Your Health Score: 82/100│ │
│ │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░ │ │
│ │ ↑ 3 points from last week   │ │
│ └─────────────────────────────┘ │
│                                 │
│ QUICK LOG                       │
│ ┌───────┐ ┌───────┐ ┌───────┐ │
│ │  🩸  │ │  💊  │ │  🏃  │ │
│ │ Blood │ │ Meds  │ │Exercise│ │
│ │ Sugar │ │ Taken │ │ 30min │ │
│ └───────┘ └───────┘ └───────┘ │
│ ┌───────┐ ┌───────┐ ┌───────┐ │
│ │  ⚖️  │ │  😊  │ │  💤  │ │
│ │Weight │ │ Mood  │ │ Sleep │ │
│ │ 165lb │ │ Good  │ │ 7.5hr │ │
│ └───────┘ └───────┘ └───────┘ │
│                                 │
│ UPCOMING                        │
│ ┌─────────────────────────────┐ │
│ │ 💊 Metformin     in 2 hours │ │
│ ├─────────────────────────────┤ │
│ │ 🏥 Dr. Chen    Tomorrow 2pm │ │
│ └─────────────────────────────┘ │
│                                 │
│ TODAY'S INSIGHTS               │
│ ┌─────────────────────────────┐ │
│ │ Your blood sugar is most    │ │
│ │ stable after morning walks  │ │
│ │ [View Details]              │ │
│ └─────────────────────────────┘ │
│                                 │
├─────────────────────────────────┤
│ [Today] [Track] [Insights] [More]│
└─────────────────────────────────┘
```

**Design Decisions**:
- Health score provides immediate status overview
- Quick log buttons show last entered value
- 1-tap access to most frequent actions
- Upcoming section prevents missed meds/appointments
- Insight card encourages engagement

#### 2. QUICK LOG MODAL

```
┌─────────────────────────────────┐
│         Log Blood Sugar      X  │
├─────────────────────────────────┤
│                                 │
│ ┌─────────────────────────────┐ │
│ │                             │ │
│ │           1 2 0             │ │
│ │           -----             │ │
│ │           mg/dL             │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ │
│ │ 1 │ │ 2 │ │ 3 │ │ 4 │ │ 5 │ │
│ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ │
│ │ 6 │ │ 7 │ │ 8 │ │ 9 │ │ 0 │ │
│ ├───┤ ├───┤ ├───┤ ├───┤ ├───┤ │
│ │ . │ │ ← │ │   │ │   │ │ ✓ │ │
│ └───┘ └───┘ └───┘ └───┘ └───┘ │
│                                 │
│ When was this reading?          │
│ ┌─────────┐ ┌─────────────────┐ │
│ │ Before  │ │      After      │ │
│ │  Meal   │ │      Meal       │ │
│ └─────────┘ └─────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │      + Add note (optional)  │ │
│ └─────────────────────────────┘ │
│                                 │
│ Normal range: 80-130 mg/dL      │
│                                 │
└─────────────────────────────────┘
```

**Interaction Details**:
- Large number pad for easy input
- Auto-advance after 3 digits
- Smart suggestions based on time
- Visual feedback for normal/abnormal
- Optional context without requirement

#### 3. INSIGHTS SCREEN

```
┌─────────────────────────────────┐
│ ← Insights                  ⚙️  │
├─────────────────────────────────┤
│                                 │
│ [Week] [Month] [3 Months] [Year]│
│                                 │
│ BLOOD SUGAR TRENDS             │
│ ┌─────────────────────────────┐ │
│ │     📈 7-Day Average: 118   │ │
│ │                             │ │
│ │ 180 ┤                       │ │
│ │     │    ╱╲                 │ │
│ │ 140 ┤   ╱  ╲    ╱╲         │ │
│ │     │  ╱    ╲  ╱  ╲  ═══   │ │
│ │ 100 ┤═╯      ╲╱    ╲╱      │ │
│ │     │                       │ │
│ │  60 ┤                       │ │
│ │     └─────────────────────  │ │
│ │     M  T  W  T  F  S  S     │ │
│ └─────────────────────────────┘ │
│                                 │
│ PATTERNS DETECTED              │
│ ┌─────────────────────────────┐ │
│ │ 🌅 Morning readings higher  │ │
│ │    Average: 132 mg/dL       │ │
│ │    Try: Earlier dinner      │ │
│ ├─────────────────────────────┤ │
│ │ 🏃 Post-exercise improvement│ │
│ │    Average drop: 15 mg/dL   │ │
│ │    Keep it up!             │ │
│ └─────────────────────────────┘ │
│                                 │
│ CORRELATIONS                   │
│ ┌─────────────────────────────┐ │
│ │ Sleep Quality ←→ Blood Sugar│ │
│ │ ● ● ● ● ○  Strong          │ │
│ │ [See Details]              │ │
│ └─────────────────────────────┘ │
│                                 │
├─────────────────────────────────┤
│ [Today] [Track] [Insights] [More]│
└─────────────────────────────────┘
```

**Design Rationale**:
- Clear data visualization with context
- Actionable insights, not just data
- Pattern recognition to drive behavior
- Progressive disclosure of complexity
- Encouraging messaging for adherence

#### 4. MEDICATION REMINDER

```
┌─────────────────────────────────┐
│ 💊 Time for Metformin          │
├─────────────────────────────────┤
│                                 │
│ ┌─────────────────────────────┐ │
│ │         METFORMIN           │ │
│ │         500mg • 2 pills     │ │
│ │                             │ │
│ │      💊 💊                  │ │
│ │                             │ │
│ │    Take with breakfast      │ │
│ └─────────────────────────────┘ │
│                                 │
│ Did you take it?               │
│                                 │
│ ┌─────────────────────────────┐ │
│ │      ✓ Yes, Taken          │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │      ⏰ Snooze 1 hour      │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │      ❌ Skip this dose     │ │
│ └─────────────────────────────┘ │
│                                 │
└─────────────────────────────────┘
```

### INTERACTION PATTERNS

#### Micro-interactions

**Data Entry Success**:
```
User taps save → 
Button transforms to checkmark → 
Ripple effect → 
Card animates to list → 
Subtle haptic feedback
```

**Achievement Unlocked**:
```
Milestone reached → 
Confetti animation → 
Badge appears → 
Swipe to dismiss → 
Added to profile
```

**Abnormal Reading Alert**:
```
High value entered → 
Field highlights red → 
Warning message slides in → 
"Add note?" prompt → 
Emergency contact option
```

#### Gesture Support

- **Swipe right**: Mark medication as taken
- **Swipe left**: Snooze reminder
- **Long press**: Quick edit any entry
- **Pull to refresh**: Update Today screen
- **Pinch to zoom**: Expand graphs

### ACCESSIBILITY FEATURES

#### Visual Accessibility
- High contrast mode option
- Minimum 4.5:1 contrast ratios
- Large touch targets (44x44pt)
- Scalable text up to 200%
- Color-blind safe palettes

#### Motor Accessibility
- One-handed operation possible
- Gesture alternatives for all actions
- Adjustable tap timing
- Simplified navigation option

#### Cognitive Accessibility
- Clear, simple language
- Progressive disclosure
- Consistent patterns
- Undo functionality
- Help tooltips

### RESPONSIVE BEHAVIOR

#### Tablet Adaptation
```
┌─────────────────┬─────────────────┐
│                 │                 │
│   Today View    │   Quick Stats   │
│                 │                 │
│   Quick Log     │   Recent Logs   │
│   Grid (2x3)    │   List View     │
│                 │                 │
│   Insights      │   Graph View    │
│   Summary       │   Expanded      │
│                 │                 │
└─────────────────┴─────────────────┘
```

- Master-detail layout for larger screens
- Expanded quick log grid
- Side-by-side comparisons
- Landscape optimization

### COMPONENT SYSTEM

#### Base Components

**Primary Button**:
- Height: 48pt
- Corner radius: 8pt
- Font: System Medium 16pt
- States: Default, Pressed, Disabled

**Quick Log Card**:
- Size: 104x104pt
- Padding: 16pt
- Icon: 32pt
- Label: 14pt
- Value: 16pt Medium

**Data Input Field**:
- Height: 56pt
- Border: 1pt
- Focus state: 2pt primary color
- Error state: Red with message

**Graph Component**:
- Aspect ratio: 16:9
- Grid lines: Subtle gray
- Data points: 8pt circles
- Touch areas: 44pt

### DESIGN SYSTEM INTEGRATION

#### iOS Adaptations
- SF Symbols for icons
- iOS navigation patterns
- Native date/time pickers
- Haptic feedback patterns
- Widget design compliance

#### Android Adaptations
- Material Design components
- Material You theming
- Bottom navigation
- FAB for primary action
- Material motion

### PROTOTYPING SPECIFICATIONS

#### Screen Transitions
- **Push**: New screens from right
- **Modal**: Bottom sheet for quick actions
- **Fade**: Between tab content
- **Spring**: For playful feedback

#### Loading States
- Skeleton screens for content
- Progress indicators for actions
- Optimistic UI updates
- Error recovery flows

#### Empty States
- Friendly illustrations
- Clear call-to-action
- Educational content
- Progress encouragement

### HANDOFF DOCUMENTATION

#### For Developers

**Spacing System**:
- Base unit: 8pt
- Spacing: 8, 16, 24, 32, 48pt
- Component padding: 16pt
- Screen margins: 16pt

**Color Tokens**:
```
Primary: #007AFF
Secondary: #5AC8FA
Success: #34C759
Warning: #FF9500
Error: #FF3B30
Background: #F2F2F7
Surface: #FFFFFF
Text Primary: #000000
Text Secondary: #3C3C43
```

**Animation Timing**:
- Micro: 0.1s ease-out
- Short: 0.3s ease-in-out
- Medium: 0.5s spring
- Long: 0.8s ease-in-out

#### For QA Testing

**Critical User Paths**:
1. First-time onboarding completion
2. Daily metric logging < 30 seconds
3. Medication reminder interaction
4. Data export for doctor visit
5. Emergency contact access

**Edge Cases**:
- No internet connection
- Extreme data values
- Rapid repeated entries
- Multiple reminders conflict
- Data sync conflicts

## Usage Instructions
1. Start with thorough user research and persona development
2. Map user journeys before designing screens
3. Create low-fidelity wireframes to test concepts
4. Design mobile-first, then adapt for larger screens
5. Build consistent component library early
6. Test with real users throughout process
7. Document all interaction patterns clearly
8. Prepare comprehensive handoff materials

## Examples
### Example 1: E-commerce Checkout Redesign
**Input**: 
```
{{product_type}}: Mobile shopping app
{{target_users}}: Busy parents, 25-40
{{user_goals}}: Fast, secure checkout
{{business_goals}}: Reduce cart abandonment by 25%
{{constraints}}: Must integrate with existing payment systems
```

**Output**: [Streamlined 3-step checkout with auto-fill, multiple payment options, guest checkout, order tracking, and trust signals throughout]

### Example 2: B2B Dashboard Design
**Input**:
```
{{product_type}}: Web analytics dashboard
{{target_users}}: Marketing managers, non-technical
{{user_goals}}: Understand campaign performance quickly
{{business_goals}}: Increase daily active usage
{{platform}}: Responsive web application
```

**Output**: [Customizable dashboard with drag-drop widgets, preset views for common reports, plain-English insights, and automated alert system]

## Related Prompts
- [User Research Analyst](/prompts/analysis/user-research.md)
- [Visual Design Expert](/prompts/creation/visual-design.md)
- [Usability Testing Specialist](/prompts/evaluation/usability-testing.md)

## Research Notes
- Based on established UX principles and heuristics
- Emphasizes accessibility and inclusive design
- Balances user needs with technical feasibility
- Includes detailed specifications for development
- Focuses on measurable improvements in user experience