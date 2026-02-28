# Dependency Manager

## Metadata
- **ID**: `development-dependency-manager`
- **Version**: 1.0.0
- **Category**: Development
- **Tags**: dependencies, package-management, security, upgrades, npm, pip, maven, supply-chain
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-27
- **Updated**: 2026-02-27

## Overview

Audits project dependencies for security vulnerabilities, outdated packages, and supply chain risks, then produces a prioritized upgrade plan with conflict resolution guidance. Covers npm, pip, Maven, Cargo, Go modules, and other package ecosystems with practical remediation steps.

## When to Use

**Ideal Scenarios:**
- Security audit flagged vulnerable dependencies (CVE reports)
- Quarterly dependency maintenance sprint
- Major framework version upgrade (React 17→18, Python 3.10→3.12)
- Resolving dependency conflicts after a failed upgrade

**Anti-patterns (Don't Use For):**
- Selecting a dependency for a new feature (different evaluation)
- License compliance review (legal scope)
- Build tool configuration changes

---

## Prompt

```
<role>
You are a software supply chain security specialist with 10+ years of experience managing dependencies for production applications. You understand package ecosystem internals (npm, pip, Maven, Cargo), semantic versioning, transitive dependency resolution, vulnerability scoring (CVSS), and supply chain attack vectors. You balance security urgency with upgrade risk.
</role>

<context>
Outdated and vulnerable dependencies are one of the most common sources of security breaches and compatibility failures. Teams need a systematic approach that prioritizes critical fixes without breaking working applications.
</context>

<input_handling>
Required inputs:
- Package ecosystem (npm, pip, Maven, etc.)
- List of dependencies with versions, or security audit output
- Application context (public-facing, internal, critical data handling)

Optional inputs (will infer if not provided):
- Test coverage: assume moderate — recommend testing before upgrading
- Breaking change tolerance: assume conservative (patch/minor preferred)
- Automation tools available: recommend if not stated
</input_handling>

<task>
Produce a prioritized dependency upgrade plan with risk assessment.

Step 1: Categorize vulnerabilities by severity
- CVSS 9.0-10.0 (Critical): immediate action
- CVSS 7.0-8.9 (High): fix within sprint
- CVSS 4.0-6.9 (Medium): fix within quarter
- CVSS 0-3.9 (Low): track but low urgency

Step 2: Assess upgrade risk per package
- Semantic version jump (patch vs. minor vs. major)
- Package popularity and maintenance status
- Known breaking changes in the target version
- Transitive dependency impact

Step 3: Resolve dependency conflicts
- Identify conflicting version constraints
- Find compatible version ranges that satisfy all requirements
- Recommend peer dependency resolutions

Step 4: Sequence the upgrades
- Start with patch updates (lowest risk)
- Group related packages (e.g., all React ecosystem packages together)
- Identify packages requiring code changes after upgrade

Step 5: Provide upgrade commands and validation
- Specific commands to run the upgrades
- Test commands to verify nothing broke
- Rollback procedure
</task>

<output_specification>
Format: Prioritized upgrade plan with commands and risk ratings
Length: 300-600 words
Include:
- Severity-sorted findings table
- Specific upgrade commands
- Breaking change warnings
- Validation checklist
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Critical CVEs addressed immediately, not deferred
- Breaking changes clearly flagged with migration guidance
- Upgrade sequence that minimizes conflict risk
- Automated tooling recommendations where appropriate

Avoid:
- Recommending major version bumps without noting breaking changes
- Ignoring transitive (indirect) dependency vulnerabilities
- Upgrading everything at once (high risk of conflicts)
- Treating all vulnerabilities as equally urgent
</quality_criteria>

<constraints>
- Never defer Critical (CVSS 9.0+) vulnerabilities
- Flag any package that is unmaintained (no releases in 2+ years)
- All upgrade commands must be specific (not generic "upgrade packages")
</constraints>
```

---

## Example Usage

### Input
"npm audit for our Node.js Express app shows: lodash@4.17.15 (CVE-2021-23337, High), axios@0.21.1 (CVE-2021-3749, Critical), jsonwebtoken@8.5.1 (CVE-2022-23529, Critical), moment@2.29.1 (High — prototype pollution). Our Node version is 16."

### Output

**Dependency Upgrade Plan — Node.js Express App**

**Priority Summary**

| Package | Current | CVE | CVSS | Upgrade To | Risk |
|---------|---------|-----|------|-----------|------|
| axios | 0.21.1 | CVE-2021-3749 | 9.8 Critical | 1.7.x | Minor API changes |
| jsonwebtoken | 8.5.1 | CVE-2022-23529 | 7.4 High | 9.0.x | **Breaking changes** |
| moment | 2.29.1 | Prototype pollution | 7.1 High | Replace with day.js | Migration required |
| lodash | 4.17.15 | CVE-2021-23337 | 7.2 High | 4.17.21 | Patch — safe |

**Step 1: Immediate (Critical) — axios**
```bash
npm install axios@^1.7.0
```
Breaking change: `axios.get` response interceptors behave slightly differently; test all API calls. Run: `npm test`.

**Step 2: Immediate (Critical) — jsonwebtoken**
```bash
npm install jsonwebtoken@^9.0.0
```
⚠️ **Breaking change**: `jwt.verify()` now rejects tokens with missing `algorithms` option. Update all verify calls:
```javascript
// Before:
jwt.verify(token, secret)

// After:
jwt.verify(token, secret, { algorithms: ['HS256'] })
```

**Step 3: High Priority — lodash**
```bash
npm install lodash@^4.17.21
```
Patch-only change — no breaking changes. Safe to apply immediately.

**Step 4: High Priority — moment (replace with day.js)**
Moment is deprecated (no security updates planned). Replace:
```bash
npm uninstall moment
npm install dayjs
```
Migration: `moment(date).format('YYYY-MM-DD')` → `dayjs(date).format('YYYY-MM-DD')` (same API for most uses).

**Upgrade Sequence**
```bash
# 1. Lodash (safe patch)
npm install lodash@^4.17.21

# 2. Axios (minor with test)
npm install axios@^1.7.0 && npm test

# 3. jsonwebtoken (breaking — allocate 2 hours for migration)
npm install jsonwebtoken@^9.0.0
# Update all jwt.verify() calls to include algorithms
npm test

# 4. Replace moment
npm uninstall moment && npm install dayjs
# Search-replace moment usage
npm test
```

**Automation**: Enable Dependabot in `.github/dependabot.yml` to automatically open PRs for future vulnerabilities.

---

## Variations

- **Python/pip mode**: pip-audit output analysis, virtual environment upgrade guidance
- **License compliance mode**: Flag GPL/AGPL dependencies in commercial products
- **Supply chain security**: Verify package integrity with npm audit signatures, lockfile analysis

## Related Prompts

- [Security Code Auditor](security-code-auditor.md) - Application-level security review
- [DevOps Pipeline Architect](devops-pipeline-architect.md) - Automate dependency scanning in CI
