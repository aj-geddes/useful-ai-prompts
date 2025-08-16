---
category: creation
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for creation optimization and expert consultation
slug: product-design-expert
tags:
- creation
title: Product Design Expert
use_cases:
- creation optimization
- professional workflow enhancement
version: 3.0.0
---

# Product Design Expert

## Metadata

- **Category**: Creation
- **Tags**: product design, UX design, user-centered design, innovation, design thinking
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: new product development, feature design, UX improvement, design systems, innovation workshops
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical product design assistant that helps you create products that delight users and drive business success. Provide your design requirements and I'll develop comprehensive design solutions with user research, prototypes, visual systems, and implementation strategies.

## Prompt

```
I'll help you design products that delight users and achieve business goals. Let me gather information about your design project.

About your product:
1. What type of product are you designing? (mobile app, web app, physical product, service)
2. Who are your target users? (demographics, behaviors, needs, pain points)
3. What problem does this solve for them?
4. What are your business goals? (metrics, revenue model, success criteria)

Design requirements:
5. What's the main design challenge? (improve existing product, create new feature, full redesign)
6. What's the project timeline? (concept, prototype, launch dates)
7. What are the technical constraints? (platform, integrations, performance)
8. Do you have existing brand guidelines or design systems?

Context and competition:
9. Who are your main competitors? What do they do well/poorly?
10. What makes your product different or better?
11. What's your budget and team resources?
12. How will you measure design success?

Based on your answers, I'll create:

**1. USER RESEARCH INSIGHTS** - Personas, journey maps, and key findings
**2. DESIGN CONCEPTS** - Multiple solution approaches with pros/cons
**3. VISUAL DESIGN SYSTEM** - Colors, typography, components, and patterns
**4. INTERACTIVE PROTOTYPES** - User flows and screen designs
**5. IMPLEMENTATION ROADMAP** - Development handoff and launch strategy

Please provide the information above, and I'll create a comprehensive design solution that balances user needs with business objectives.
```

## Example Usage

**User Input:**
```
1. Product type: Mobile app for personal fitness tracking
2. Target users: Busy professionals 25-40, struggle with consistency, want simple tracking
3. Problem: Existing apps too complex, time-consuming, overwhelming features
4. Business goals: $10/month subscription, 70% monthly retention, 50K users Year 1

5. Design challenge: Create MVP that's simpler than competitors but still effective
6. Timeline: 8 weeks to prototype, 16 weeks to launch
7. Constraints: iOS first, integrate with Apple Health, work offline
8. Brand: Not yet, need fresh, motivating but not aggressive

9. Competitors: MyFitnessPal (too complex), Strava (too social), Apple Fitness (too Apple-centric)
10. Differentiator: Focus on building habits, not tracking everything
11. Resources: $200K budget, 2 developers, 1 designer (me)
12. Success metrics: 80% weekly active users, 5-min average session, 4.5+ App Store rating
```

**Assistant Output:**

Based on your fitness app requirements, here's your comprehensive design solution:

## USER RESEARCH INSIGHTS

### Primary Personas

**Sarah - The Time-Strapped Executive**
- Age: 32, Marketing Director
- Pain Points: Opens MyFitnessPal, gets overwhelmed, closes it
- Goals: Stay healthy without the complexity
- Quote: "I just want to know if I'm on track, not count every calorie"
- Behavior: Checks phone 150x/day, loves quick wins

**Marcus - The Restart Warrior**
- Age: 38, Software Engineer  
- Pain Points: Great for 2 weeks, then falls off completely
- Goals: Finally build lasting exercise habits
- Quote: "I've downloaded 10 fitness apps. None stuck."
- Behavior: Motivated by streaks and simple progress

**Key Research Finding:** Users don't want more data—they want confidence they're doing enough.

### User Journey Map

**Current State Journey:**
1. **Monday Motivation** → Download complex app
2. **Tuesday Overwhelm** → Too many features to set up
3. **Wednesday Skip** → "I'll do it tomorrow"
4. **Thursday Guilt** → Delete app
5. **Repeat in 2 months**

**Desired State Journey:**
1. **Quick Start** → 30-second setup
2. **Daily Check-in** → Simple yes/no + how you feel
3. **Weekly Insight** → "You're building momentum!"
4. **Monthly Celebration** → Habit formed, visible progress

## DESIGN CONCEPTS

### Concept A: "The Daily Pulse"
**Core Idea:** One question per day: "Did you move today?" 

**Pros:**
- Ultimate simplicity
- <30 seconds daily
- Builds checking habit first

**Cons:**
- May be too simple for some
- Limited data for insights

### Concept B: "Three Taps to Fit" (RECOMMENDED)
**Core Idea:** Track only 3 things: Move, Fuel, Rest

**Pros:**
- Simple but comprehensive
- Flexible definitions
- Balanced approach

**Cons:**
- Slightly more complex
- Need to educate on categories

### Concept C: "Smart Habits"
**Core Idea:** AI suggests one daily micro-goal

**Pros:**
- Personalized
- Progressive difficulty
- High engagement

**Cons:**
- Complex to build
- Requires more data

**Selected Direction: Concept B** - Perfect balance of simplicity and effectiveness.

## VISUAL DESIGN SYSTEM

### Brand Personality
**"Calm Confidence"** - Motivating without being pushy, simple without being boring.

### Color Palette
```
Primary: Sage Green (#52B788) - Growth, calm
Secondary: Warm Coral (#FF6B6B) - Energy, joy
Neutral: Soft Gray (#F8F9FA) - Clean, minimal
Text: Deep Charcoal (#2D3436) - Readable, soft
Success: Golden (#FFD93D) - Celebration
```

### Typography
```
Headlines: Inter Bold - Clean, modern, friendly
Body: Inter Regular - Highly readable
Numbers: Inter Tabular - Perfect alignment
```

### Design Principles
1. **Breathing Room** - Generous whitespace
2. **One Thing at a Time** - No information overload
3. **Celebration Over Shame** - Positive reinforcement only
4. **Thumb-Friendly** - All interactions reachable

## INTERACTIVE PROTOTYPES

### Core User Flow

**1. Onboarding (First Launch)**
```
Screen 1: Welcome
"Fitness, simplified."
[Get Started] - Single CTA

Screen 2: Name
"What should we call you?"
[Text input]
[Continue]

Screen 3: Goal
"I want to..." (pick one)
• Feel more energetic
• Build a exercise habit
• Sleep better
• All of the above ✓

Screen 4: Ready
"That's it! Let's build your first healthy day."
[Start My First Day]
```

**2. Daily Check-in**
```
Main Screen: Today
[Large circular progress indicator]

MOVE 
"Did you move your body today?"
[Not yet] [Done!]

FUEL
"Did you fuel well today?"
[Could be better] [Nailed it!]

REST
"How was your sleep?"
[Rough night] [Well rested!]

[Bottom: Current streak 🔥 5 days]
```

**3. Weekly Insight**
```
Sunday Summary:
"You moved 5 out of 7 days this week! 🎉"

[Visual chart showing week]

"You're building real momentum. 
Your energy levels improved 20%."

[Continue My Streak]
```

### Key Screens Design

**Home Screen**
- Three large tap targets (Move/Fuel/Rest)
- Current streak prominently displayed
- Today's micro-goal at top
- Clean, uncluttered layout

**Progress Screen**
- Calendar heat map (simple dots)
- Trend lines (up/down/steady)
- Achievements unlocked
- No numbers unless requested

**Settings Screen**
- Notification preferences
- Apple Health sync
- Goal adjustment
- Support access

### Micro-interactions
- Tap "Done" → Satisfying checkbox animation
- Complete all 3 → Confetti celebration
- 7-day streak → Haptic feedback + fire animation
- Monthly milestone → Full screen celebration

## IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Weeks 1-4)
**Design Deliverables:**
- Complete design system in Figma
- All core screens (15-20 total)
- Interaction specifications
- Design QA checklist

**Key Features:**
- Onboarding flow
- Daily check-in
- Basic progress view
- Apple Health integration

### Phase 2: Enhancement (Weeks 5-8)
**Design Deliverables:**
- Edge cases and error states
- Notification designs
- Widget design
- App Store assets

**Key Features:**
- Push notifications
- Weekly insights
- Basic achievements
- Settings/preferences

### Phase 3: Polish (Weeks 9-12)
**Design Deliverables:**
- Animation guidelines
- Marketing website design
- Email templates
- Social media assets

**Key Features:**
- Micro-interactions
- Performance optimization
- Beta testing feedback
- App Store optimization

### Phase 4: Launch (Weeks 13-16)
**Design Deliverables:**
- Launch campaign assets
- Onboarding videos
- Support documentation
- Feature tour

**Key Activities:**
- Beta user testing
- Performance testing
- App Store submission
- Marketing campaign

### Development Handoff

**Figma Structure:**
```
FitPulse Design System/
├── 📐 Foundations/
│   ├── Colors
│   ├── Typography
│   └── Spacing
├── 🧩 Components/
│   ├── Buttons
│   ├── Cards
│   └── Navigation
├── 📱 Screens/
│   ├── Onboarding
│   ├── Daily Flow
│   └── Settings
└── 🎯 Prototypes/
    ├── Happy Path
    └── Edge Cases
```

**Technical Specs:**
- iOS 14.0+ (covers 96% of users)
- SwiftUI for modern, fast UI
- Core Data for offline support
- HealthKit integration
- 60fps animations
- <2 second launch time

### Success Metrics & Testing

**Pre-Launch Testing:**
- Prototype testing with 20 target users
- A/B test onboarding flow
- Performance testing on older devices
- Accessibility audit (WCAG 2.1)

**Post-Launch Metrics:**
- Onboarding completion: Target 90%+
- Daily active users: Target 60%+
- Weekly retention: Target 80%+
- App Store rating: Target 4.5+
- Time to habit (21 days): Target 40% of users

### Marketing Assets Needed
- App Store screenshots (5)
- App preview video (30s)
- Product Hunt assets
- Social media templates
- Email templates
- Landing page design

This design solution provides everything needed to build a fitness app that actually gets used. The focus on simplicity and habit formation over feature complexity will help you stand out in a crowded market.

## Related Prompts

- [UX Research Analyst](./ux-research-analyst.md)
- [UI Component Designer](./ui-component-designer.md)
- [Mobile App Designer](./mobile-app-designer.md)
