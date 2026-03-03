# Skills Library

A collection of 259 specialized skills for AI assistants, each providing expert guidance on a specific technical or professional domain. Skills are structured for both programmatic indexing and human browsing.

## For AI Assistants: How to Use This Library

### Finding the Right Skill

Each subdirectory is a self-contained skill identified by its kebab-case folder name (e.g., `api-error-handling`, `docker-containerization`). To find a relevant skill:

1. **By name** — Scan directory names; they match the task domain directly
2. **By frontmatter** — Read the YAML frontmatter in any `SKILL.md` for the `name` and `description` fields:
   ```yaml
   ---
   name: api-error-handling
   description: >
     Implement comprehensive API error handling with standardized error
     responses, logging, monitoring, retry logic, and validation patterns.
   ---
   ```
3. **By keyword search** — Search `description` fields across all skills to match user intent

### Reading a Skill

Each skill follows **Progressive Disclosure Architecture**:

```
skill-name/
├── SKILL.md              # Hub document — start here
├── references/           # Deep-dive content by topic
│   ├── topic-one.md
│   └── topic-two.md
├── scripts/              # Domain-specific utilities (optional)
└── templates/            # Starter boilerplate (optional)
```

**Always start with `SKILL.md`**. It contains:

| Section | Purpose |
|---|---|
| **Overview** | What this skill covers (1-2 sentences) |
| **When to Use** | Matching criteria — use this to decide relevance |
| **Quick Start** | Minimal working example to get started immediately |
| **Reference Guides** | Table linking to deep-dive documents in `references/` |
| **Best Practices** | DO and DON'T lists for quality guidance |

**Load references on demand.** Only read files from `references/` when the user needs depth on a specific topic. The hub's Reference Guides table describes what each file contains.

### Programmatic Indexing

To build an index of all skills:

```python
import os, yaml

skills = []
for entry in sorted(os.listdir("skills")):
    skill_path = os.path.join("skills", entry, "SKILL.md")
    if not os.path.isfile(skill_path):
        continue
    with open(skill_path) as f:
        content = f.read()
    # Extract YAML frontmatter between --- markers
    if content.startswith("---"):
        _, fm, _ = content.split("---", 2)
        meta = yaml.safe_load(fm)
        skills.append({
            "id": entry,
            "name": meta.get("name", entry),
            "description": meta.get("description", ""),
            "has_references": os.path.isdir(os.path.join("skills", entry, "references")),
            "has_scripts": os.path.isdir(os.path.join("skills", entry, "scripts")),
            "has_templates": os.path.isdir(os.path.join("skills", entry, "templates")),
        })
```

### Skill Selection Algorithm

When a user asks for help on a topic:

1. Tokenize the user's request into keywords
2. Score each skill by matching keywords against `name` and `description`
3. Select the highest-scoring skill (or present top 3 if ambiguous)
4. Read the selected skill's `SKILL.md` hub
5. Load specific `references/` files only as needed for depth

## For Humans: Browsing the Library

### Domain Distribution

| Domain | Count | Examples |
|---|---|---|
| API & Web Services | 40 | api-error-handling, api-rate-limiting, graphql-schema-design |
| Infrastructure | 32 | docker-containerization, kubernetes-deployment, terraform-iac |
| Frontend | 31 | react-component-design, css-grid-layout, angular-module-design |
| Database | 30 | sql-query-optimization, mongodb-schema-design, redis-caching |
| Testing | 28 | unit-testing, integration-testing, load-testing |
| Security | 21 | api-security-hardening, access-control-rbac, vulnerability-scanning |
| CI/CD | 16 | jenkins-pipeline, github-actions, gitlab-ci |
| Process | 13 | agile-sprint-planning, code-review, stakeholder-communication |
| Monitoring | 9 | alert-management, application-logging, performance-monitoring |
| Documentation | 5 | api-reference-documentation, technical-writing |
| Data Science | 2 | ab-test-analysis, anomaly-detection |

### Skill Structure

**228 skills** use the full Progressive Disclosure Architecture (hub + references). The remaining 31 skills are single-file (under 150 lines of content — too concise to warrant splitting).

Every restructured skill includes:
- **Hub SKILL.md** — Concise overview (typically 80-130 lines)
- **references/** — 2-7 deep-dive documents per skill (1,084 reference docs total)
- **scripts/** — Domain-specific utilities with TODO stubs (209 skills)
- **templates/** — Starter boilerplate files (237 skills)

### Quick Start

Pick any skill directory and read its `SKILL.md`:

```bash
cat skills/docker-containerization/SKILL.md
```

To see what reference docs are available:

```bash
ls skills/docker-containerization/references/
```

## Validation

The skill-builder tool (`.claude/skills/skill-builder/`) can validate any skill against 18 quality gates:

```bash
bash .claude/skills/skill-builder/scripts/validate-skill.sh skills/my-skill
```

Quality gates cover hub structure (frontmatter, TOC, required sections), hub quality (line count, reference table), reference quality (titles, minimum content, link integrity), and directory structure.
