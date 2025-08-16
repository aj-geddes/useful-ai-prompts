# Document Organization & Filing Expert

## Metadata

- **Category**: Business/Administrative
- **Tags**: document management, filing system, organization, administrative, information architecture
- **Created**: 2025-07-20
- **Version**: 3.0.0
- **Use Cases**: document filing, archive organization, information retrieval, compliance management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you create an organized, searchable document management system that saves time, ensures compliance, and scales with your organization's growth.

## Prompt

```
I'll help you design a practical document organization system that works for your team. Let me understand your current situation:

**About your organization:**
1. What type/size of organization are you? (startup, SMB, enterprise, non-profit)
2. How many people need access to shared documents?
3. What departments or teams are involved?
4. Do you have any compliance requirements? (HIPAA, SOX, etc.)

**Current document situation:**
5. How many documents do you estimate you have?
6. Where are documents currently stored? (drives, cloud, physical files)
7. What's your biggest document-related frustration right now?
8. How much time is wasted looking for documents daily?

**Usage patterns:**
9. What types of documents do you work with most? (contracts, reports, etc.)
10. Who needs access to what kinds of documents?
11. How often do you need to find documents older than 1 year?
12. Any documents that must be kept for legal/regulatory reasons?

Based on your answers, I'll provide:

**ORGANIZATION SYSTEM** - Logical folder structure and naming conventions
**SEARCH STRATEGY** - How to make documents findable instantly
**ACCESS CONTROLS** - Who can see/edit what documents
**RETENTION POLICY** - What to keep, archive, or delete and when
**IMPLEMENTATION PLAN** - Step-by-step migration and training approach

Please describe your current document chaos so I can help organize it!
```

## Example Usage

**User Input:**
```
1. Mid-size marketing agency, 45 employees
2. All 45 need some access, but different levels
3. Creative, Account Management, Operations, Finance, Leadership
4. No specific compliance, but client confidentiality is important

5. Probably 50,000+ files across everything
6. Mix of Google Drive, Dropbox, local computers, some physical files
7. Can't find client assets, version confusion, duplicate files everywhere
8. Probably 2-3 hours per day across the team

9. Client briefs, creative assets, contracts, presentations, reports
10. Everyone needs access to templates, teams need their client files
11. Often - need to reference old campaigns and contracts
12. Contracts for 7 years, financial records for 7 years

Current mess: 
- Google Drive has 15 different "Client Work" folders
- Dropbox has random stuff from 3 years ago
- Desktop folders like "Final_FINAL_v3"
- No one knows where the brand guidelines are
```

**Assistant Output:**

Based on your 45-person agency with 50K+ scattered files, here's your document organization overhaul:

## MASTER FOLDER STRUCTURE

```
📁 AGENCY_DOCS/
├── 📁 01_CLIENTS/
│   ├── 📁 [ClientName]_[StartYear]/
│   │   ├── 📁 01_Contracts & Legal
│   │   ├── 📁 02_Briefs & Strategy
│   │   ├── 📁 03_Creative Assets
│   │   ├── 📁 04_Campaigns
│   │   └── 📁 05_Reports & Analytics
│   └── 📁 _ARCHIVED_CLIENTS/
├── 📁 02_BUSINESS_OPS/
│   ├── 📁 Contracts & Legal
│   ├── 📁 Finance & Accounting  
│   ├── 📁 HR & Personnel
│   └── 📁 Operations
├── 📁 03_MARKETING/
│   ├── 📁 Brand Assets
│   ├── 📁 Website & Digital
│   └── 📁 Proposals & Pitches
├── 📁 04_TEMPLATES/
│   ├── 📁 Client Deliverables
│   ├── 📁 Internal Documents
│   └── 📁 Presentations
└── 📁 05_ARCHIVE/
    └── 📁 [Year] Archives
```

## NAMING CONVENTIONS

**Client Files:**
- `YYYY-MM-DD_ClientName_DocumentType_Version`
- Examples:
  - `2025-01-15_Nike_CreativeBrief_v1`
  - `2025-01-20_Nike_LogoConcepts_Final`
  - `2025-02-01_Nike_CampaignReport_Q1`

**Internal Files:**
- `YYYY-MM-DD_Department_Topic_Status`
- Examples:
  - `2025-01-15_Finance_Q4Budget_Draft`
  - `2025-01-20_HR_PolicyUpdate_Final`

**Asset Files:**
- `ClientName_AssetType_Description_Specs`
- Examples:
  - `Nike_Logo_Primary_RGB`
  - `Nike_Typography_Headline_OpenSans`

## ACCESS CONTROL MATRIX

| Folder | Leadership | Account Mgmt | Creative | Finance | Operations |
|--------|------------|--------------|----------|---------|------------|
| All Clients | View All | View Assigned | View Assigned | View Contracts | View All |
| Business Ops | Full Access | View Relevant | View Relevant | Full Access | Full Access |
| Templates | Edit | Use | Edit | Use | Edit |
| Archive | View All | View Assigned | View All | View All | Full Access |

## 30-DAY IMPLEMENTATION PLAN

### Week 1: Foundation
**Days 1-2**: Create master folder structure in Google Drive
**Days 3-4**: Set up access permissions and sharing rules  
**Day 5**: Train leadership team on new system

### Week 2: Client Files Migration
**Days 1-3**: Move active client files to new structure
**Days 4-5**: Update file names to new convention
**Weekend**: Team reviews their assigned client folders

### Week 3: Internal Files & Templates
**Days 1-2**: Organize business operations files
**Days 3-4**: Create/update template library
**Day 5**: Department training sessions

### Week 4: Archive & Polish
**Days 1-3**: Move old files to archive with year folders
**Days 4-5**: Final cleanup and documentation
**End of week**: System go-live celebration

## SEARCH & RETRIEVAL SYSTEM

**Google Drive Search Operators:**
```
Find Nike creative assets: "Nike" type:image
Find Q4 reports: "Q4" "report" type:pdf
Find contracts from 2024: "contract" after:2024/1/1 before:2024/12/31
Find all templates: parent:"04_TEMPLATES"
```

**File Tagging Strategy:**
- Add keywords to file descriptions
- Use consistent terminology across teams
- Tag frequently accessed files with star/priority

## RETENTION & CLEANUP POLICY

**Keep Forever:**
- Final signed contracts
- Brand assets and templates
- Completed campaign deliverables

**Keep 7 Years:**
- Financial records and invoices
- Tax-related documents
- Legal correspondence

**Keep 3 Years:**
- Project briefs and internal communications
- Draft versions of important documents
- Meeting notes and recordings

**Monthly Cleanup:**
- Delete files in "Trash" folder > 30 days
- Archive completed projects > 1 year old
- Review and delete duplicate files

## AUTOMATION RECOMMENDATIONS

1. **Google Drive Rules:**
   - Auto-move files uploaded to root into "00_INBOX"
   - Alert when files haven't been moved from inbox in 48 hours
   
2. **Slack Integration:**
   - Daily reminder to file documents properly
   - Weekly folder structure reminder in #general

3. **Monthly Audits:**
   - Report on files not following naming convention
   - Identify large files that could be archived
   - List files with no activity in 6 months

**Expected Results:**
- Document search time: 2-3 hrs/day → 15 mins/day (85% reduction)
- Version confusion: Eliminated with clear naming
- Client onboarding: 2 hours → 30 minutes (template system)
- Compliance confidence: From "hope we have it" → "I know exactly where it is"

## TRAINING MATERIALS CREATED

1. **Quick Reference Card:** Folder structure and naming guide
2. **Video Tutorials:** 5-minute walkthroughs for each team
3. **Search Cheat Sheet:** Common search operators and tips
4. **New Employee Onboarding:** Document system overview

Would you like help implementing any specific part of this system?
```

## Related Prompts

- [Task Delegation Expert](./task-delegation-tracking.md)
- [Meeting Minutes Expert](./meeting-minutes-summarization.md)
- [Email Management Expert](./email-prioritization-response.md)