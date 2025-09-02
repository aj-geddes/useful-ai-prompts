# UI/UX Wireframing Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Creation
- **Tags**: wireframing, UI design, UX design, prototyping, interaction design
- **Version**: 2.0.0
- **Use Cases**: mobile apps, web applications, software interfaces, design systems, prototypes
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical UI/UX wireframing assistant that helps you design intuitive, user-centered interfaces. Provide your product requirements and I'll create comprehensive wireframes with user flows, screen layouts, interaction patterns, and implementation specifications.

## Prompt

```
I'll help you create effective UI/UX wireframes that delight users and achieve business goals. Let me gather information about your design needs.

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

Based on your answers, I'll create:

**1. USER FLOWS** - How users navigate through key tasks
**2. WIREFRAME SCREENS** - Layout and structure for main screens
**3. INTERACTION PATTERNS** - How elements behave and respond
**4. COMPONENT LIBRARY** - Reusable UI elements
**5. RESPONSIVE BEHAVIOR** - How designs adapt to different screens

Please provide the information above, and I'll design wireframes that create an excellent user experience.
```

## Example Usage

**User Input:**
```
1. Interface type: Mobile app (iOS and Android)
2. Purpose: Task management for creative professionals
3. Target users: Designers, writers, artists, 25-45, tech-savvy but busy
4. Key features: Project dashboard, task lists, time tracking, collaboration

5. Platforms: iOS primary, Android secondary, web later
6. Primary tasks: Create projects, add tasks, track time, share with clients, invoice
7. Design style: Clean and minimal with creative touches
8. Brand guidelines: Not yet, open to suggestions

9. Project stage: MVP development
10. UX challenges: Balancing simplicity with powerful features, quick task entry
11. Success metrics: Daily active use, <30 sec task creation, 4.5+ app rating
12. Constraints: Offline capability needed, integrate with calendar apps
```

**Assistant Output:**

Based on your creative task management app requirements, here's your comprehensive wireframe design:

# CREATIVETASK PRO - UI/UX WIREFRAMES

## USER FLOWS

### Primary Flow: Quick Task Creation
```
App Launch → Dashboard → "+" Button → Task Entry → Save → Return to View
     ↓                        ↓                      ↓
(if new user)            (voice option)         (optional)
     ↓                        ↓                      ↓
Onboarding              Voice Input          Add Details
```

### Key Task Flows

**1. Create New Project**
- Dashboard → New Project → Enter Name → Choose Template → Set Deadline → Add Team
- Time to complete: 45 seconds

**2. Quick Task Entry**
- Any screen → Long press "+" → Type/speak task → Auto-assign to project
- Time to complete: 10 seconds

**3. Time Tracking**
- Task list → Swipe right on task → Timer starts → Work → Tap to stop
- Interaction: Single gesture

## WIREFRAME SCREENS

### 1. DASHBOARD (Home Screen)

```
┌─────────────────────────────────┐
│ ☰  CreativeTask          🔍 👤  │
├─────────────────────────────────┤
│                                 │
│ Good morning, Alex! ☀️          │
│ You have 5 tasks due today      │
│                                 │
│ ACTIVE PROJECTS                 │
│ ┌─────────────────────────────┐ │
│ │ Website Redesign    65% ▓▓░ │ │
│ │ 12 tasks • Due in 5 days    │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ Brand Guidelines    40% ▓░░ │ │
│ │ 8 tasks • Due in 2 weeks    │ │
│ └─────────────────────────────┘ │
│                                 │
│ TODAY'S FOCUS                   │
│ ┌─────────────────────────────┐ │
│ │ □ Homepage wireframes  2h   │ │
│ │ □ Client feedback call 1h   │ │
│ │ □ Color palette review 30m  │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │      ⏱ 3h 25m tracked       │ │
│ │        today so far         │ │
│ └─────────────────────────────┘ │
│                                 │
│         ⊕                       │
│    (Float Button)               │
├─────────────────────────────────┤
│ [Home] [Projects] [Time] [More] │
└─────────────────────────────────┘
```

**Design Decisions:**
- Project cards show visual progress
- Today's tasks prominently displayed
- Running time tracker always visible
- Floating action button for quick task creation
- Clean typography with enough whitespace

### 2. QUICK TASK ENTRY

```
┌─────────────────────────────────┐
│        Add New Task         X   │
├─────────────────────────────────┤
│                                 │
│ ┌─────────────────────────────┐ │
│ │ What needs to be done?      │ │
│ │                             │ │
│ │ |                           │ │
│ └─────────────────────────────┘ │
│                                 │
│ 🎙 Tap to use voice input       │
│                                 │
│ PROJECT                         │
│ ┌─────────────────────────────┐ │
│ │ Website Redesign      ▼     │ │
│ └─────────────────────────────┘ │
│                                 │
│ QUICK DETAILS                   │
│ ┌────────────┐ ┌──────────────┐ │
│ │ 📅 Today ▼ │ │ ⏱ 2 hours ▼ │ │
│ └────────────┘ └──────────────┘ │
│                                 │
│ ┌────────────┐ ┌──────────────┐ │
│ │ 🏷 Design  │ │ 🔴 High     │ │
│ │    +2      │ │ Priority     │ │
│ └────────────┘ └──────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │     Create Task             │ │
│ └─────────────────────────────┘ │
│                                 │
│ Recently used:                  │
│ • Design review (Website...)    │
│ • Client feedback (Brand...)    │
│                                 │
└─────────────────────────────────┘
```

**Interaction Details:**
- Auto-focus on text field
- Smart project suggestion based on recent activity
- One-tap access to common values
- Recent tasks for quick re-creation
- Voice input option prominent

### 3. PROJECT DETAIL VIEW

```
┌─────────────────────────────────┐
│ ← Website Redesign         ⋮    │
├─────────────────────────────────┤
│                                 │
│ ┌─────────────────────────────┐ │
│ │  Progress      65% ▓▓▓▓▓░░  │ │
│ │  Due Date      Feb 15 (5d)  │ │
│ │  Time Spent    24h 30m      │ │
│ └─────────────────────────────┘ │
│                                 │
│ [Active] [Completed] [All]      │
│                                 │
│ TODAY                           │
│ ┌─────────────────────────────┐ │
│ │ □ Homepage wireframes        │ │
│ │   🕐 2h • 🔴 High           │ │
│ │                      [▶]    │ │
│ └─────────────────────────────┘ │
│                                 │
│ TOMORROW                        │
│ ┌─────────────────────────────┐ │
│ │ □ Navigation flow review     │ │
│ │   🕐 1h • 🟡 Medium         │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ □ Mobile responsive layouts  │ │
│ │   🕐 3h • 🟡 Medium         │ │
│ └─────────────────────────────┘ │
│                                 │
│ UPCOMING                        │
│ ┌─────────────────────────────┐ │
│ │ □ Component library setup    │ │
│ │   No date • 🟢 Low          │ │
│ └─────────────────────────────┘ │
│                                 │
│         ⊕                       │
└─────────────────────────────────┘
```

**Task Interactions:**
- Tap checkbox to complete
- Swipe right to start timer
- Swipe left for more options
- Tap anywhere else to edit
- Drag to reorder

### 4. TIME TRACKING VIEW

```
┌─────────────────────────────────┐
│ ← Time Tracking                 │
├─────────────────────────────────┤
│                                 │
│ [Day] [Week] [Month]           │
│                                 │
│ TODAY - FEBRUARY 10             │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ Currently Tracking:          │ │
│ │ Homepage wireframes          │ │
│ │ ⏱ 01:24:35  [⏸] [✓]        │ │
│ └─────────────────────────────┘ │
│                                 │
│ TIME BREAKDOWN                  │
│ ┌─────────────────────────────┐ │
│ │ Website Redesign  4h 25m    │ │
│ │ ████████████░░░░░░░░ 65%    │ │
│ ├─────────────────────────────┤ │
│ │ Brand Guidelines  2h 10m    │ │
│ │ ██████░░░░░░░░░░░░░░ 32%    │ │
│ ├─────────────────────────────┤ │
│ │ Admin Tasks      15m        │ │
│ │ █░░░░░░░░░░░░░░░░░░░  3%    │ │
│ └─────────────────────────────┘ │
│                                 │
│ RECENT ENTRIES                  │
│ ┌─────────────────────────────┐ │
│ │ Color palette review  45m   │ │
│ │ 2:30 PM - 3:15 PM    [✏]   │ │
│ ├─────────────────────────────┤ │
│ │ Client email         10m    │ │
│ │ 2:15 PM - 2:25 PM    [✏]   │ │
│ └─────────────────────────────┘ │
│                                 │
│ Total: 6h 50m / 8h goal        │
│                                 │
└─────────────────────────────────┘
```

## INTERACTION PATTERNS

### Gestures & Micro-interactions

**Task Management:**
- **Swipe right**: Start timer on task
- **Swipe left**: Task options (edit, delete, move)
- **Long press**: Multi-select mode
- **Drag & drop**: Reorder or move between projects
- **Pull to refresh**: Sync with cloud

**Quick Actions:**
```
Task tap → Expand details → 
Timer button pulse → 
Tap → Timer starts → 
Button transforms to pause → 
Subtle tick animation
```

**Success Feedback:**
```
Task complete → 
Checkbox fills → 
Card fades → 
Progress bar animates → 
Haptic feedback
```

### Navigation Patterns

**Tab Bar Behavior:**
- Home: Dashboard with projects
- Projects: Full project list  
- Time: Time tracking view
- More: Settings, reports, profile

**Floating Action Button:**
- Single tap: Quick task
- Long press: Voice input
- Drag up: More options

## COMPONENT LIBRARY

### Core Components

**Task Card:**
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

**Project Card:**
```
Height: 96px
Progress bar: 4px height
Title: 16px semibold
Subtitle: 14px regular gray
Tap target: Entire card
```

**Time Entry Button:**
```
Size: 48x48px
Icon: 24px
States:
- Inactive: Gray outline
- Active: Filled with primary color
- Pulsing: Subtle scale animation
```

**Input Fields:**
```
Height: 48px
Border: 1px gray (2px primary on focus)
Corner radius: 8px
Font size: 16px
Placeholder: 40% opacity
```

## RESPONSIVE BEHAVIOR

### Tablet Adaptation (iPad)

```
┌─────────────────────┬─────────────────────┐
│                     │                     │
│   Project List      │   Task Detail       │
│   (1/3 width)       │   (2/3 width)       │
│                     │                     │
│ ┌─────────────────┐ │  Homepage wireframes│
│ │ Website Redesign │ │                     │
│ │ 65% ███░░       │ │  Description...     │
│ │ Selected ✓      │ │                     │
│ └─────────────────┘ │  Time: 2h          │
│                     │  Due: Today         │
│ ┌─────────────────┐ │                     │
│ │ Brand Guidelines │ │  [Start Timer]      │
│ │ 40% ██░░░       │ │                     │
│ └─────────────────┘ │  Subtasks:          │
│                     │  □ Research         │
│                     │  □ Sketches         │
│                     │  □ Digital wireframe│
└─────────────────────┴─────────────────────┘
```

### Phone Landscape

- Side navigation drawer
- Task list takes full width
- Floating timer widget
- Optimized for two-thumb typing

### Implementation Specifications

**Color System:**
```
Primary: #5B67CA (Indigo)
Secondary: #FDB44E (Amber)
Success: #2ED47A
Error: #FF6B6B
Neutral Gray: #7C8DB5
Background: #FAFBFF
Surface: #FFFFFF
Text Primary: #1A2036
Text Secondary: #7C8DB5
```

**Typography:**
```
Font Family: SF Pro (iOS) / Roboto (Android)
Headings: 20-24px semibold
Body: 16px regular
Small text: 14px regular
Buttons: 16px medium
```

**Spacing Grid:**
```
Base unit: 8px
Common spacings: 8, 16, 24, 32, 48px
Screen margins: 16px
Card padding: 16px
Line height: 1.5x font size
```

### Animation Guidelines

**Timing Functions:**
```
Micro: 150ms ease-out
Short: 300ms ease-in-out  
Medium: 500ms spring
Long: 800ms ease-in-out
```

**Common Animations:**
- Page transition: Slide 300ms
- Modal: Slide up 400ms
- Success: Scale + fade 300ms
- Loading: Pulse 1.2s infinite
- Delete: Slide + fade 350ms

### Accessibility Considerations

**Visual:**
- WCAG AA compliant colors
- Dynamic type support
- Dark mode ready
- Icon + text labels

**Motor:**  
- 44pt minimum touch targets
- Gesture alternatives
- Keyboard navigation
- Voice control support

**Cognitive:**
- Clear information hierarchy
- Consistent patterns
- Confirmation for destructive actions
- Undo capability

### Platform-Specific Adaptations

**iOS Specific:**
- SF Symbols for all icons
- iOS-style navigation bar
- Swipe back gesture
- 3D Touch/Haptic Touch menus
- Today widget design

**Android Specific:**
- Material Design 3 components
- Material You dynamic theming
- Bottom app bar option
- FAB with speed dial
- Edge-to-edge design

### Empty States & Onboarding

**First Project Empty State:**
```
┌─────────────────────────────────┐
│                                 │
│         [Illustration]          │
│      Creative workspace         │
│                                 │
│   Start your first project      │
│                                 │
│  Projects help you organize     │
│  tasks and track progress       │
│                                 │
│ ┌─────────────────────────────┐ │
│ │    Create First Project     │ │
│ └─────────────────────────────┘ │
│                                 │
│    Import from other apps       │
│                                 │
└─────────────────────────────────┘
```

**Onboarding Flow:**
1. Welcome + value prop
2. Create first project (guided)
3. Add first task (tooltip)
4. Try timer (animated hint)
5. Success celebration

### Development Handoff

**Key Deliverables:**
1. Component specifications (sizes, states, behaviors)
2. Color and typography tokens
3. Spacing and grid system
4. Animation timing values
5. Gesture documentation
6. Platform-specific guidelines

**Testing Priorities:**
1. Task creation under 10 seconds
2. Timer accuracy and persistence
3. Offline functionality
4. Cross-device sync
5. Accessibility compliance

**Success Metrics:**
- Task creation time: <10 seconds
- Daily active usage: 80%+
- Feature adoption: 60%+ use timer
- User satisfaction: 4.5+ rating
- Retention: 70% after 30 days

This wireframe design creates an intuitive, efficient task management experience that balances simplicity with powerful features for creative professionals.

## Related Prompts

- [Mobile App Designer](../content-creation/storytelling-framework-designer.md)
- [Design System Creator](../renewable-energy/energy-storage-system-design-expert.md)
- [Prototype Developer](../personal-growth/self-discipline-developer.md)
