# User-Centered Design Guide

## Metadata

- **Category**: Creativity & Innovation
- **Tags**: user-centered design, UX design, human-centered design, accessibility, user research
- **Created**: 2025-07-21
- **Version**: 2.0.0
- **Use Cases**: product design, service design, app development, website design, experience design
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical user-centered design guide that helps you create products and experiences truly designed for your users. Provide your project details and I'll guide you through a human-centered design process.

## Prompt

```
I'll help you apply user-centered design principles to create experiences that truly serve your users' needs. Let me gather information about your project and users.

About your project:
1. What are you designing? (app, website, service, product, etc.)
2. What problem does it solve for users?
3. What stage are you at? (concept, design, redesign, optimization)
4. What are your main design challenges?

About your users:
5. Who are your primary users? (demographics, context, needs)
6. What accessibility requirements do you have?
7. How tech-savvy are your users?
8. What emotional state are users in when using your product?

About constraints:
9. What technical constraints do you have?
10. What's your timeline and budget?

Based on your answers, I'll provide:

**1. USER RESEARCH PLAN** - How to understand your users deeply
**2. DESIGN PRINCIPLES** - Core principles tailored to your users
**3. ACCESSIBILITY STRATEGY** - Making it work for everyone
**4. DESIGN SOLUTIONS** - Specific recommendations for your challenge
**5. TESTING APPROACH** - How to validate with real users

I'll help you create designs that are:
- Intuitive and easy to use
- Accessible to all users
- Emotionally resonant
- Solving real user problems
- Tested and validated

Please provide the information above to get started.
```

## Example Usage

**User Input:**
```
1. Designing: Mobile app for medication management for elderly users
2. Problem: Seniors often forget medications, take wrong doses, or get confused with multiple prescriptions
3. Stage: Early design phase, have done initial research
4. Challenges: Making it simple enough for 70+ users, handling poor eyesight, avoiding tech overwhelm

5. Primary users: Seniors 65-85, living independently, managing 3-10 medications daily
6. Accessibility: Must work for users with arthritis, poor vision, mild cognitive decline
7. Tech-savvy: Low - many struggle with smartphones, some have never used apps
8. Emotional state: Often anxious about health, frustrated with technology, worried about making mistakes

9. Technical constraints: Must work offline, integrate with pharmacy systems
10. Timeline: 6 months to launch, $200K budget
```

**Assistant Output:**

Perfect! Let's design a medication management app that truly serves elderly users. Based on your inputs, here's a comprehensive user-centered approach:

**USER RESEARCH PLAN**

**1. Deep Empathy Research (2 weeks)**
- **In-home observations**: Watch 10 seniors manage medications in their real environment
- **Medication journey mapping**: Document entire process from prescription to taking pills
- **Family interviews**: Understand caregiver perspectives and concerns
- **Pharmacy partnerships**: Learn about prescription processes and common errors

**Key Research Questions:**
- How do they currently organize medications?
- What causes the most confusion or errors?
- What existing systems work well for them?
- How do vision/motor issues affect medication taking?

**DESIGN PRINCIPLES**

Based on elderly users' needs:

**1. "Bigger is Better"**
- Minimum 16pt fonts (preferably 18-20pt)
- Touch targets at least 44x44px (prefer 60x60px)
- High contrast ratios (7:1 minimum)
- Extra whitespace between elements

**2. "One Thing at a Time"**
- Single-task screens
- No multi-step processes on one screen
- Clear, linear navigation
- Always show where user is in process

**3. "Familiar Metaphors"**
- Use real-world analogies (pill bottles, calendars)
- Avoid tech jargon completely
- Voice-first interactions where possible
- Physical-like interactions (sliding, not swiping)

**4. "Fail-Safe Design"**
- Multiple confirmations for critical actions
- Undo options everywhere
- Clear error recovery
- Impossible to "break" anything

**ACCESSIBILITY STRATEGY**

**Vision Support:**
- **Adjustable text size**: 16pt to 32pt options
- **High contrast mode**: Pure black on white
- **Color-blind safe**: Never rely on color alone
- **Voice output**: Read all text aloud option
- **Large, clear icons**: With text labels always

**Motor Support:**
- **Large tap areas**: 60x60px minimum
- **Gesture alternatives**: Tap instead of swipe
- **Confirmation delays**: Prevent accidental taps
- **Voice input**: "Take blue pill" commands
- **Steady-hand mode**: Ignore minor shakes

**Cognitive Support:**
- **Simple language**: 5th-grade reading level
- **Visual medication identification**: Pill photos
- **Step-by-step guidance**: One instruction at a time
- **Routine reinforcement**: Same flow daily
- **Caregiver mode**: Family can help setup

**DESIGN SOLUTIONS**

**Core Screen: Daily Medication View**
```
Morning (8:00 AM)
[Large pill image] Heart Medicine
                   1 white round pill
                   [✓ TAKEN] or [TAKE NOW]

[Large pill image] Blood Pressure
                   2 blue oval pills
                   [TAKE NOW - Large Green Button]
```

**Key Features:**

1. **Visual Pill Identifier**
   - Actual photos of user's pills
   - Size reference (shown next to penny)
   - Color and shape clearly visible

2. **Time-Based Reminders**
   - Large clock showing current time
   - "Morning/Afternoon/Evening" not specific times
   - Gentle escalating reminders

3. **Confirmation System**
   - Big "I took it" button
   - Photo confirmation option
   - Automatic pharmacy refill alerts

4. **Emergency Features**
   - "Call my doctor" one-touch button
   - "I feel sick" quick access
   - Medication information in large print

**TESTING APPROACH**

**Phase 1: Paper Prototype Testing (Week 3-4)**
- Test with 15 seniors at senior center
- Use large printed screens
- Observe without helping
- Note every confusion point

**Phase 2: Interactive Testing (Week 8-10)**
- In-home testing with 10 users
- 1-week diary study
- Daily check-in calls
- Family member feedback

**Key Metrics:**
- Task completion without help
- Error rate (wrong medication)
- Time to complete daily routine
- Comfort level (1-10 scale)
- Would they recommend to friend?

**IMPLEMENTATION RECOMMENDATIONS**

**1. Onboarding Strategy**
- In-person setup at pharmacy
- Family member involvement
- Practice mode with candy "pills"
- Printed quick-start guide

**2. Voice-First Features**
- "What pills do I take now?"
- "I took my morning pills"
- "Call my daughter"
- "When is my next dose?"

**3. Progressive Disclosure**
- Start with just pill reminders
- Add features as users get comfortable
- Hide complex features by default
- "Simple mode" always available

**RISK MITIGATION**

- **Tech anxiety**: Start with pharmacy setup assistance
- **Adoption resistance**: Free trial with family support
- **Error prevention**: Multiple confirmation steps
- **Emergency scenarios**: Direct hotline to pharmacist

Would you like me to detail any specific aspect, such as the exact screen layouts or the voice interaction design?

## Related Prompts

- [Accessibility Checker](../evaluation-assessment/accessibility-evaluation-expert.md)
- [User Research Guide](../research/user-research-expert.md)
- [Prototyping Coach](./prototyping-methodology-expert.md)