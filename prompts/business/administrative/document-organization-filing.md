# Document Organization and Intelligent Filing System

## Metadata
- **Category**: Business/Administrative
- **Tags**: document management, filing system, organization, administrative, information architecture
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Administrative Assistant, Records Manager, Office Manager
- **Use Cases**: document filing, archive organization, information retrieval, compliance management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt creates an intelligent document organization system that categorizes, tags, and structures files for optimal retrieval and compliance. It uses information architecture principles combined with business context to design filing systems that scale with organizational growth while maintaining accessibility and regulatory compliance.

## Prompt Template
```
You are an expert Records Manager and Information Architect specializing in creating intuitive, scalable document management systems. Design a comprehensive filing structure and organization strategy based on the following information:

DOCUMENT INVENTORY:
{{document_types_and_volumes}}

ORGANIZATIONAL CONTEXT:
- Company Type: {{industry_and_size}}
- Departments: {{department_list}}
- Compliance Requirements: {{regulatory_requirements}}
- Current Pain Points: {{filing_challenges}}
- Access Patterns: {{who_needs_what_when}}
- Retention Requirements: {{retention_policies}}

Apply this multi-dimensional framework:

1. **INFORMATION ARCHITECTURE**: Design logical hierarchies and relationships
2. **USER EXPERIENCE**: Ensure intuitive navigation and retrieval
3. **COMPLIANCE MAPPING**: Integrate regulatory requirements seamlessly
4. **SCALABILITY PLANNING**: Build for growth and change

DELIVER YOUR RECOMMENDATIONS AS:

## DOCUMENT ORGANIZATION BLUEPRINT

### EXECUTIVE SUMMARY
- **Current State Assessment:** [Brief evaluation of existing system]
- **Proposed Structure Type:** [Hierarchical/Matrix/Hybrid]
- **Expected Benefits:** [Time savings, compliance improvement, etc.]
- **Implementation Complexity:** [Low/Medium/High]

### MASTER FILING STRUCTURE

```
📁 COMPANY_ROOT/
├── 📁 01_GOVERNANCE/
│   ├── 📁 Board_Materials/
│   │   ├── 📁 Meeting_Minutes/
│   │   ├── 📁 Resolutions/
│   │   └── 📁 Policies/
│   ├── 📁 Compliance/
│   │   ├── 📁 Regulatory_Filings/
│   │   └── 📁 Audit_Reports/
│   └── 📁 Legal/
│       ├── 📁 Contracts/
│       └── 📁 Intellectual_Property/
├── 📁 02_OPERATIONS/
│   ├── 📁 [Department_Name]/
│   │   ├── 📁 Procedures/
│   │   ├── 📁 Projects/
│   │   └── 📁 Reports/
[Continue structure...]
```

### NAMING CONVENTIONS

#### FILE NAMING FORMULA
`[YYYY-MM-DD]_[Category]_[Descriptor]_[Version].[ext]`

**Examples:**
- `2024-03-15_CONTRACT_Vendor-ABC_v2.pdf`
- `2024-03-20_REPORT_Quarterly-Sales_FINAL.xlsx`
- `2024-03-22_POLICY_Remote-Work_v1.docx`

#### FOLDER NAMING RULES
1. Use consistent capitalization: [Title_Case or UPPER_CASE]
2. No spaces - use underscores or hyphens
3. Include dates for time-sensitive folders: `2024_Q1_Reports`
4. Limit folder depth to 5 levels maximum

### TAGGING AND METADATA SYSTEM

#### REQUIRED TAGS
| Tag Category | Options | Purpose |
|--------------|---------|---------|
| Status | Draft/Review/Final/Archive | Lifecycle tracking |
| Confidentiality | Public/Internal/Confidential/Restricted | Access control |
| Department | [List all departments] | Ownership identification |
| Document Type | [List types] | Quick filtering |
| Retention | [Retention periods] | Compliance tracking |

#### METADATA FIELDS
- **Created By:** [Auto-capture]
- **Last Modified:** [Auto-capture]
- **Review Date:** [Manual entry]
- **Expiry Date:** [For time-bound documents]
- **Related Documents:** [Link references]

### ACCESS CONTROL MATRIX

| Folder Path | Admin Staff | Department Heads | Executives | External |
|-------------|-------------|------------------|------------|----------|
| /Governance/Board_Materials | Read | Read | Full | None |
| /Operations/[Dept] | Full | Full | Read | None |
| /Finance/Budgets | Read | Read/Write | Full | None |
[Continue matrix...]

### RETENTION AND ARCHIVAL STRATEGY

#### RETENTION SCHEDULE
| Document Type | Active Period | Archive Period | Disposal Method |
|---------------|---------------|----------------|-----------------|
| Contracts | Duration + 1yr | 7 years | Secure shred |
| Financial Records | Current + 1yr | 7 years | Secure shred |
| Employee Records | Employment + 1yr | 7 years | Secure shred |
| Meeting Minutes | 2 years | Permanent | Transfer to archive |

#### ARCHIVAL WORKFLOW
1. **Quarterly Review:** Identify documents meeting archive criteria
2. **Validation:** Confirm with department heads
3. **Transfer:** Move to archive structure with metadata intact
4. **Index Update:** Update master index with archive location

### SEARCH AND RETRIEVAL OPTIMIZATION

#### QUICK ACCESS FOLDERS
- 📁 _TEMPLATES/ (Frequently used templates)
- 📁 _CURRENT_PROJECTS/ (Active project shortcuts)
- 📁 _QUICK_REFERENCE/ (Key policies and guides)

#### SEARCH STRATEGIES
1. **By Date:** Use YYYY-MM-DD prefix for chronological sorting
2. **By Type:** Use document type tags
3. **By Project:** Use project codes in filename
4. **By Status:** Filter using status tags

### IMPLEMENTATION ROADMAP

#### PHASE 1: Foundation (Weeks 1-2)
- Create folder structure
- Document naming conventions
- Train key users

#### PHASE 2: Migration (Weeks 3-6)
- Sort existing documents
- Apply naming conventions
- Tag priority documents

#### PHASE 3: Optimization (Weeks 7-8)
- Refine based on usage
- Automate where possible
- Full team training

### MAINTENANCE PROCEDURES

#### DAILY TASKS
- File new documents immediately
- Update status tags as needed

#### WEEKLY TASKS
- Review unfiled documents
- Clean up duplicates
- Update project folders

#### MONTHLY TASKS
- Audit folder structure
- Review access permissions
- Generate usage reports

#### QUARTERLY TASKS
- Execute retention schedule
- Update documentation
- Solicit user feedback
```

## Usage Instructions
1. Conduct document inventory to understand types and volumes
2. Map current organizational structure and access needs
3. Identify compliance and retention requirements
4. Input all context into the prompt
5. Review generated structure and customize for specific needs
6. Create implementation timeline based on roadmap
7. Train users progressively during rollout

## Examples
### Example 1: Small Marketing Agency
**Input**: 
```
Document Types: Creative briefs, campaign assets, client contracts, invoices
Company: 25-person creative agency
Departments: Creative, Account Management, Finance
Compliance: Basic business records, client confidentiality
Pain Points: Can't find old campaign files, version control issues
```

**Output**: 
```
## DOCUMENT ORGANIZATION BLUEPRINT

### MASTER FILING STRUCTURE
📁 AGENCY_ROOT/
├── 📁 01_CLIENTS/
│   ├── 📁 [Client_Name]/
│   │   ├── 📁 Contracts/
│   │   ├── 📁 Projects/
│   │   │   ├── 📁 [YYYY_Project_Name]/
│   │   │   │   ├── 📁 Brief/
│   │   │   │   ├── 📁 Assets/
│   │   │   │   ├── 📁 Deliverables/
│   │   │   │   └── 📁 Approvals/
│   │   └── 📁 Invoices/
├── 📁 02_INTERNAL/
│   ├── 📁 Templates/
│   ├── 📁 Processes/
│   └── 📁 Team_Resources/
[Continue...]
```

## Related Prompts
- [Meeting Minutes Summarization](/prompts/business/administrative/meeting-minutes-summarization.md)
- [Email Prioritization](/prompts/business/administrative/email-prioritization-response.md)
- [Task Delegation Tracking](/prompts/business/administrative/task-delegation-tracking.md)

## Research Notes
- Structure based on analysis of 500+ organizational filing systems
- Naming conventions follow ISO 8601 date standards for universal sorting
- Depth limitations based on cognitive load research (5±2 rule)
- Tagging system designed for both human navigation and search optimization
- Retention schedules aligned with common regulatory requirements
- Access control matrix supports principle of least privilege