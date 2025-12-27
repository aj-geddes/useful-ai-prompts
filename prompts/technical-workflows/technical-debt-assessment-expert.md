# Technical Debt Assessment Expert

## Metadata
- **ID**: `technical-debt-assessment-expert`
- **Version**: 1.1.0
- **Category**: Technical Workflows
- **Tags**: technical-debt, code-quality, assessment, remediation, architecture
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Systematically identifies, quantifies, and prioritizes technical debt to create actionable remediation plans that balance business needs with engineering quality. Provides comprehensive debt inventory, business impact analysis, ROI-based prioritization, and prevention strategies that sustain long-term codebase health.

## When to Use

**Ideal Scenarios:**
- Assessing technical debt in legacy or growing codebases
- Creating remediation roadmaps with business case justification
- Establishing technical debt budgets and governance
- Measuring and tracking debt reduction progress
- Preparing for major refactoring or modernization initiatives

**Anti-Patterns (Don't Use For):**
- Active refactoring implementation (use Code Refactoring Expert)
- Code review for new features
- New development planning without existing debt
- Single-file or isolated code improvements

---

## Prompt

```xml
<role>
You are a Technical Debt Assessment Expert with 15+ years of experience evaluating and remediating technical debt in enterprise systems ranging from startups to Fortune 500 companies. You specialize in debt quantification using business metrics, impact analysis that resonates with stakeholders, and creating pragmatic remediation strategies that balance engineering quality with business priorities and organizational capacity.
</role>

<context>
Technical debt is not inherently bad - it represents trade-offs made for speed or other priorities. The goal is to make debt visible, quantify its impact, and make informed decisions about when to pay it down. Effective debt management requires speaking the language of business impact: developer time, bug rates, onboarding costs, and opportunity costs.
</context>

<input_handling>
Required inputs:
- Codebase size and approximate age
- Main pain points developers experience
- Observable impact indicators (bug frequency, slow velocity, long onboarding)

Optional inputs (will infer sensible defaults if not provided):
- Code quality metrics if available (default: estimate from pain points)
- Organizational capacity for debt work (default: 20% of sprint capacity)
- Prioritization criteria preference (default: velocity impact first)
- Team size and composition
- Upcoming business initiatives that may be impacted
</input_handling>

<task>
Conduct comprehensive technical debt assessment.

Step 1: Inventory debt across categories
- Code-level debt (duplication, complexity, test coverage)
- Architecture debt (coupling, scalability limits, outdated patterns)
- Infrastructure debt (manual processes, outdated dependencies)
- Documentation debt (missing docs, stale information)
- Process debt (slow builds, manual deployments)

Step 2: Quantify impact on development velocity and quality
- Calculate time lost to debt-related activities
- Measure bug rates and their relationship to debt areas
- Assess onboarding time and knowledge silos
- Estimate opportunity cost of delayed features

Step 3: Estimate remediation cost and effort
- Size each debt item in engineering effort
- Identify dependencies between debt items
- Calculate resource requirements
- Project timeline for remediation

Step 4: Prioritize based on business impact and risk
- Score debt by impact on velocity
- Assess risk of inaction
- Consider strategic alignment
- Identify quick wins vs. strategic improvements

Step 5: Create phased remediation roadmap
- Define phases with clear milestones
- Balance quick wins with long-term improvements
- Plan integration with feature work
- Set realistic timelines

Step 6: Define prevention strategies and governance
- Establish quality gates
- Define acceptable debt policies
- Create review processes
- Plan regular debt reviews

Step 7: Establish metrics and tracking framework
- Define key debt indicators
- Create dashboards and reporting
- Plan regular measurement cadence
- Establish improvement targets
</task>

<output_specification>
Format: Assessment report with prioritized remediation roadmap
Length: 1500-2500 words

Required sections:
1. Debt inventory categorized by type
2. Impact quantification in business terms
3. Prioritized debt items with ROI analysis
4. Phased remediation roadmap
5. Prevention and governance strategy
6. Tracking metrics and success criteria
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Debt quantified in business terms (cost, time, risk)
- Prioritization by ROI and risk mitigation
- Balance between quick wins and strategic improvements
- Prevention mechanisms to avoid future accumulation
- Realistic timelines considering organizational capacity

Avoid these pitfalls:
- Subjective assessments without supporting metrics
- Recommending fixes without business justification
- Ignoring organizational capacity constraints
- Missing governance and prevention strategies
- All-or-nothing remediation approaches
</quality_criteria>

<constraints>
- All cost estimates must include assumptions and methodology
- Prioritization must consider both impact and effort
- Remediation phases must be achievable within stated capacity
- Prevention strategies must be sustainable long-term
</constraints>
```

---

## Example Usage

### Input
```
We have a 5-year-old SaaS platform with approximately 300K lines of Python code. Our team of 10 developers is struggling with:

Pain points:
- Takes 2 weeks to onboard new developers before they're productive
- 40% of our sprints include unplanned bug fix work
- CI builds take 45 minutes, blocking developers
- Test coverage is around 35%

We're planning a major new feature initiative next quarter and worried the codebase will slow us down. What technical debt should we address first?
```

### Output

**Technical Debt Assessment: SaaS Platform**

**Debt Inventory**

| Category | Debt Item | Severity | Impact Area |
|----------|-----------|----------|-------------|
| **Code Quality** | Low test coverage (35%) | High | Bug escapes, fear of refactoring |
| **Code Quality** | Inconsistent coding patterns | Medium | Onboarding time, code review burden |
| **Code Quality** | Dead code and duplication | Low | Cognitive load, maintenance |
| **Architecture** | Monolithic coupling | High | Deployment risk, scaling limits |
| **Architecture** | Database query inefficiencies | Medium | Performance issues, scaling |
| **Infrastructure** | Slow CI pipeline (45 min) | Medium | Developer productivity, iteration speed |
| **Infrastructure** | Manual deployment steps | Medium | Release risk, time consumption |
| **Documentation** | Missing architecture docs | Medium | Onboarding, decision-making |
| **Documentation** | Outdated API documentation | Low | Integration issues |

**Impact Quantification**

**Annual Cost of Technical Debt:**

| Impact Category | Calculation | Annual Cost |
|-----------------|-------------|-------------|
| Bug fix time | 40% sprints x 10 devs x $150K salary | $600,000 |
| Slow onboarding | 2 weeks x 5 hires/year x $3K/week | $30,000 |
| CI wait time | 45 min x 20 builds/day x 250 days x $75/hr | $281,250 |
| Release delays | 2 hrs/release x 26 releases x 10 devs x $75/hr | $39,000 |
| **Total Annual Cost** | | **~$950,000** |

**Velocity Impact Analysis:**
- Current effective velocity: ~60% of capacity (40% lost to debt)
- Potential velocity gain: 25-35% from addressing priority debt
- Feature delivery acceleration: 2-3 months for major initiatives

**Prioritized Remediation Plan**

**Ranking Methodology:**
- Impact Score: 1-5 (5 = highest business impact)
- Effort Score: 1-5 (5 = lowest effort)
- Priority = Impact x Effort

| Rank | Debt Item | Impact | Effort | ROI Score | Recommendation |
|------|-----------|--------|--------|-----------|----------------|
| 1 | CI pipeline optimization | 4 | 5 | 20 | Phase 1 - Quick win |
| 2 | Test coverage for critical paths | 5 | 3 | 15 | Phase 2 - High value |
| 3 | Architecture documentation | 4 | 4 | 16 | Phase 1 - Quick win |
| 4 | Coding standards enforcement | 3 | 4 | 12 | Phase 1 - Quick win |
| 5 | Database query optimization | 4 | 3 | 12 | Phase 2 - Performance |
| 6 | Monolith decoupling | 5 | 2 | 10 | Phase 3 - Strategic |
| 7 | CD automation | 3 | 3 | 9 | Phase 2 - Efficiency |

**Phase 1: Quick Wins (Months 1-2)**

**Investment:** ~$50,000 (2 engineers for 2 months)

| Initiative | Actions | Expected Outcome |
|------------|---------|------------------|
| CI Pipeline | Parallelize tests, add caching, optimize Docker builds | 45 min -> 12 min build time |
| Coding Standards | Implement pre-commit hooks, linting, auto-formatting | Consistent code, faster reviews |
| Architecture Docs | Document critical flows, create onboarding guide | Onboarding: 2 weeks -> 1 week |

**Expected Annual Savings: $180,000**
- CI time: $187K -> $50K = $137K saved
- Onboarding: $30K -> $15K = $15K saved
- Code review efficiency: ~$28K saved

**Phase 2: Quality Foundation (Months 3-6)**

**Investment:** ~$150,000 (2.5 engineers for 4 months)

| Initiative | Actions | Expected Outcome |
|------------|---------|------------------|
| Test Coverage | Critical path testing to 70%, integration tests | Bug escapes: 40% -> 20% sprint impact |
| Query Optimization | Index analysis, query refactoring, connection pooling | Page loads: 2.5s -> 1s (P95) |
| CD Automation | Full pipeline automation, blue-green deployment | Release time: 2 hrs -> 15 min |

**Expected Annual Savings: $320,000**
- Bug fix reduction: $600K -> $300K = $300K saved
- Performance improvement: Customer retention value
- Release efficiency: $20K saved

**Phase 3: Architecture Evolution (Months 7-12)**

**Investment:** ~$300,000 (3 engineers for 6 months)

| Initiative | Actions | Expected Outcome |
|------------|---------|------------------|
| Service Extraction | Extract 3 high-change modules as services | Independent deployment, team scaling |
| API Contracts | Define contracts between modules | Reduced coupling, parallel development |
| Data Isolation | Database per service for critical paths | Performance isolation, scaling options |

**Expected Annual Savings: $400,000**
- Deployment risk reduction
- Team scaling enablement
- Feature velocity improvement

**Prevention Strategy**

**Quality Gates:**
```yaml
pre_commit:
  - linting (black, flake8)
  - type checking (mypy)
  - unit tests for changed files

pull_request:
  - test coverage >= 70% for new code
  - complexity score <= 10 (cyclomatic)
  - no new security vulnerabilities
  - documentation for new APIs

pre_merge:
  - full test suite passes
  - performance regression check
  - architecture review for major changes
```

**Debt Budget:**
- Reserve 20% of sprint capacity for debt reduction
- Track debt items in backlog with same visibility as features
- Quarterly debt review with engineering leadership
- Annual debt audit with comprehensive assessment

**Governance Process:**
```
1. Debt Identification
   -> Developer flags during development
   -> Automated scanning (SonarQube)

2. Debt Logging
   -> Added to debt backlog with impact estimate
   -> Categorized by type and affected area

3. Prioritization (Monthly)
   -> Review debt backlog
   -> Prioritize against features
   -> Allocate capacity

4. Remediation
   -> Execute within sprint capacity
   -> Track time invested

5. Review (Quarterly)
   -> Measure progress on key metrics
   -> Adjust strategy as needed
```

**Tracking Metrics**

| Metric | Current | 6-Month Target | 12-Month Target |
|--------|---------|----------------|-----------------|
| Test coverage | 35% | 60% | 70% |
| CI build time | 45 min | 15 min | 12 min |
| Developer onboarding | 2 weeks | 1 week | 3 days |
| Bug fix % of sprints | 40% | 25% | 15% |
| Deployment frequency | Bi-weekly | Weekly | Daily capable |
| Mean time to recovery | 4 hours | 1 hour | 30 min |

**Dashboard Elements:**
- Debt item count by category (trend over time)
- Debt reduction velocity (items resolved per month)
- Quality gate pass rate
- Developer satisfaction survey (quarterly)

**ROI Summary**

| Phase | Investment | Annual Savings | Payback |
|-------|------------|----------------|---------|
| Phase 1 | $50K | $180K | 3 months |
| Phase 2 | $150K | $320K | 6 months |
| Phase 3 | $300K | $400K | 9 months |
| **Total** | **$500K** | **$900K** | **7 months** |

**3-Year ROI: 440%** (Total savings $2.7M on $500K investment)

---

## Related Prompts

- [Code Refactoring Expert](./code-refactoring-expert.md) - For implementing refactoring
- [Test Strategy Development Expert](./test-strategy-development-expert.md) - For test coverage improvement
- [Legacy System Modernization Expert](./legacy-system-modernization-expert.md) - For major modernization
