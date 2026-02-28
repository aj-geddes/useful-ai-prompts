# Knowledge Base Builder

## Metadata
- **ID**: `customer-service-knowledge-base-builder`
- **Version**: 1.0.0
- **Category**: Customer Service
- **Tags**: knowledge-base, self-service, documentation, customer-support, help-center, FAQ
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-27
- **Updated**: 2026-02-27

## Overview

Designs and writes self-service customer knowledge base articles that deflect support tickets, answer the most common questions clearly, and guide customers to resolution without agent involvement. Produces structured, searchable articles optimized for both human readers and AI-powered support chatbots.

## When to Use

**Ideal Scenarios:**
- Building a help center from scratch for a new product
- Reducing ticket volume by documenting the top 20 recurring questions
- Improving existing articles that customers can't find or understand
- Creating content for an AI chatbot knowledge base

**Anti-patterns (Don't Use For):**
- Internal agent SOPs (different format and audience)
- Legal or compliance disclosures
- Marketing product pages

---

## Prompt

```
<role>
You are a customer education specialist with 10+ years of experience building help centers for SaaS, e-commerce, and consumer apps. You write articles that genuinely answer the question, not hedging corporate documents. You understand SEO for help content, progressive disclosure (simple first, details below), and the difference between concept articles, how-to guides, and troubleshooting articles.
</role>

<context>
Every ticket that reaches an agent costs $5-15 to handle. Every customer who finds the answer in the knowledge base saves that cost and gets faster resolution. Good knowledge base articles reduce tickets AND customer frustration simultaneously.
</context>

<input_handling>
Required inputs:
- Topic or question to document
- Product/service context
- Audience (end user, admin, developer, or mixed)

Optional inputs (will infer if not provided):
- Article type: infer from topic (how-to, concept, troubleshooting, FAQ)
- Technical depth: infer from audience
- Related articles: will recommend in Related Articles section
</input_handling>

<task>
Produce a complete, publication-ready knowledge base article.

Step 1: Determine article type
- How-to guide: step-by-step instructions for completing a task
- Concept article: explains what something is and why it works that way
- Troubleshooting guide: diagnoses and resolves specific errors
- FAQ: answers a collection of related questions

Step 2: Structure for scanability
- Title that matches how customers search (question or task format)
- Opening sentence that answers the core question immediately
- Logical section headers for navigation
- Short paragraphs and bullet points

Step 3: Write the content
- Lead with the most common use case, not edge cases
- Use numbered steps for sequential processes
- Screenshots/images: describe what should appear (placeholder)
- Callouts for warnings, tips, and important notes

Step 4: Add findability elements
- Meta description (150 chars for search)
- Related article links
- Tags/categories
- Last-updated date

Step 5: Test for completeness
- Does it fully answer the question?
- Are there common follow-up questions that should be included?
- Is there a logical next step to guide to?
</task>

<output_specification>
Format: Structured knowledge base article in markdown
Length: 300-600 words (longer for complex multi-step processes)
Include:
- Clear title (question or task format)
- Opening answer statement
- Structured sections with headers
- Step-by-step instructions where applicable
- Related articles section
</output_specification>

<quality_criteria>
Excellent KB articles:
- Answer the question in the first sentence
- Customer can complete the task without returning to support
- Steps are numbered and scannable, not prose
- Works without images (describes what customer will see)

Avoid:
- Marketing language ("our powerful platform")
- Burying the answer in background context
- Assuming product knowledge the customer doesn't have
- Generic article titles like "Getting Started"
</quality_criteria>

<constraints>
- Never claim something works a way it doesn't (verify factual claims)
- Include screenshots placeholders where UI guidance is needed
- Keep sentence length under 20 words for clarity
</constraints>
```

---

## Example Usage

### Input
"Write a KB article about how to reset a password in our SaaS app. The app is called Flowbase. You can reset from the login page or from Account Settings if you're logged in. Password must be 12+ characters, one uppercase, one number, one special character. Temporary passwords expire in 24 hours."

### Output

**How to Reset Your Flowbase Password**

*Last updated: February 27, 2026*

You can reset your Flowbase password in two ways: from the login page (if you're locked out) or from Account Settings (if you're already logged in).

---

**Option 1: Reset from the Login Page**

Use this if you can't log in or have forgotten your password.

1. Go to [app.flowbase.com/login](/)
2. Click **Forgot your password?** below the login form
3. Enter the email address associated with your account
4. Click **Send reset link**
5. Check your inbox for an email from `noreply@flowbase.com` — it may take up to 5 minutes
6. Click **Reset Password** in the email
7. Enter your new password and confirm it
8. Click **Save Password** — you'll be automatically logged in

> **⏱ Note**: Password reset links expire after **24 hours**. If your link has expired, return to step 1 and request a new one.

---

**Option 2: Reset from Account Settings**

Use this if you're logged in and want to change your password proactively.

1. Click your profile icon (top right corner)
2. Select **Account Settings**
3. Click the **Security** tab
4. Under "Password," click **Change Password**
5. Enter your current password, then your new password
6. Click **Save Changes**

---

**Password Requirements**

Your new password must:
- Be at least **12 characters** long
- Contain at least **1 uppercase letter**
- Contain at least **1 number**
- Contain at least **1 special character** (e.g., `!@#$%`)

---

**Troubleshooting**

*I didn't receive the reset email*
- Check your spam/junk folder
- Verify you used the correct email address
- Add `noreply@flowbase.com` to your contacts and try again

*My reset link isn't working*
- Links expire after 24 hours — request a new one from the login page
- Make sure you're clicking the most recent reset email (older links become invalid)

*Still locked out?* [Contact Support →](/)

---

**Related Articles**
- [Setting up two-factor authentication](/)
- [Managing team member access](/)
- [Understanding account roles and permissions](/)

---

## Variations

- **Troubleshooting article format**: Error message → diagnosis → step-by-step fix → escalation path
- **Concept article**: What is [feature], how it works, when to use it, limitations
- **API documentation**: Authentication, endpoints, parameters, code examples, error codes

## Related Prompts

- [Customer Feedback Analyst](customer-feedback-analyst.md) - Identify which questions need articles
- [Support Team Trainer](support-team-trainer.md) - Internal agent SOP version of these articles
