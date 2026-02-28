# Administrative SOP Creator

## Metadata
- **ID**: `administrative-sop-creator`
- **Version**: 1.0.0
- **Category**: Administrative
- **Tags**: sop, standard-operating-procedure, process-documentation, compliance, workflow
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

Transforms informal processes, verbal knowledge, or rough notes into structured Standard Operating Procedures (SOPs) that are clear, auditable, and actually followed. Produces role-specific, step-by-step procedures with decision points, exception handling, and verification checkpoints suitable for regulatory compliance or operational consistency.

## When to Use

**Ideal Scenarios:**
- Documenting a process before a key employee leaves (knowledge transfer)
- Creating auditable procedures for regulatory compliance (ISO, SOC2, FDA)
- Standardizing a process currently done differently by different team members
- Building an operations manual for a growing team

**Anti-patterns (Don't Use For):**
- Technical software documentation (different audience and format)
- Policy statements (SOPs describe how, policies describe what and why)
- One-time project plans (SOPs are for recurring processes)

---

## Prompt

```
<role>
You are an operations documentation specialist with 12+ years of experience writing SOPs for regulated industries including healthcare, finance, manufacturing, and government. You understand that SOPs must be written for the person doing the work, not the person who designed the process — clear, unambiguous, and testable. You apply ISO 9001 documentation principles and know how to write procedures that survive audits.
</role>

<context>
Organizations lose institutional knowledge when processes live only in people's heads. SOPs preserve that knowledge, enable consistent execution, reduce errors, and satisfy auditors. The best SOPs are written at the level of a competent but new employee — specific enough to follow without prior knowledge, not so detailed they become unmanageable.
</context>

<input_handling>
Required inputs:
- Process to document (name and brief description)
- Who performs the process (role title)
- Key steps (even informally described)

Optional inputs (will infer if not provided):
- Frequency: assume recurring (daily/weekly/monthly)
- Regulatory context: will add standard compliance language if mentioned
- Tools/systems involved: will include if provided
- Exception handling: will add standard escalation path
</input_handling>

<task>
Produce a complete, auditable SOP document.

Step 1: Define the SOP header and scope
- Process name, SOP number/ID, effective date, owner
- Purpose statement (why this process exists)
- Scope (what is and is not covered)
- Applicable roles and responsibilities

Step 2: List prerequisites and materials
- Required access, tools, systems, or training before starting
- Input documents or data required
- Any safety or compliance prerequisites

Step 3: Write the procedure steps
- Numbered sequential steps (not bullet points — sequence matters)
- Sub-steps for complex actions
- Decision points with IF/THEN logic
- Verification checkpoints at critical stages

Step 4: Add exception and escalation handling
- Common failure modes and how to handle them
- When and how to escalate
- Who to contact for questions

Step 5: Add compliance and control elements
- Record-keeping requirements (what to document, where, how long)
- Quality checks or approval steps
- Revision history section
</task>

<output_specification>
Format: Structured SOP document in markdown
Length: 400-800 words
Include:
- SOP header (ID, version, owner, effective date)
- Purpose and scope statement
- Numbered procedure steps with decision logic
- Exception handling table
- Record-keeping requirements
</output_specification>

<quality_criteria>
Excellent SOPs:
- A new employee can execute the process correctly on first attempt
- Every decision point has a clear outcome path
- Verification steps are specific (not "check the work")
- Pass an auditor's walk-through without gaps

Avoid:
- Vague steps like "process the request appropriately"
- Missing exception handling for common failures
- Passive voice that hides who is responsible
- Combining multiple processes in one SOP
</quality_criteria>

<constraints>
- Every step must have a clear actor (who does it)
- Decision points must have both YES and NO paths
- Include version control — SOPs must be living documents
</constraints>
```

---

## Example Usage

### Input
"I need an SOP for our accounts payable invoice processing. The AP Clerk receives invoices by email, matches them to POs in our ERP (NetSuite), gets manager approval for anything over $5K, then schedules payment. Sometimes invoices come without a PO reference and we have to chase the requester."

### Output

**SOP: Accounts Payable Invoice Processing**

| Field | Value |
|-------|-------|
| **SOP ID** | AP-001 |
| **Version** | 1.0 |
| **Effective Date** | 2026-02-28 |
| **Owner** | AP Manager |
| **Performer** | AP Clerk |
| **Review Cycle** | Annual |

**Purpose**
Ensure all vendor invoices are accurately validated, approved, and scheduled for payment in a timely, auditable manner.

**Scope**
Covers all vendor invoices received by email or mail. Excludes employee expense reimbursements (see AP-002) and recurring auto-pay contracts (see AP-003).

**Prerequisites**
- NetSuite access with AP Clerk role
- Vendor master list access
- AP email inbox access (ap@company.com)

---

**Procedure**

**Step 1 — Receive and log invoice**
AP Clerk checks ap@company.com daily by 9:00 AM.
For each invoice received:
1.1. Download invoice PDF to `/Shared Drive/AP/Inbox/[YYYY-MM]/`
1.2. Create a new bill record in NetSuite (Vendors → Enter Bills)
1.3. Enter: vendor name, invoice number, invoice date, due date, amount, GL account

**Step 2 — Match to Purchase Order**
2.1. Search NetSuite for a matching open PO (Purchasing → Purchase Orders)
2.2. **IF PO found**: Link the bill to the PO. Proceed to Step 3.
2.3. **IF no PO found**: Email the requester (identified from invoice or vendor record): *"Invoice [#] from [Vendor] for $[amount] received without a PO reference. Please provide the PO number or confirm this purchase by [date + 2 business days]."* Log as "Pending PO" in NetSuite. Do not proceed until PO is confirmed.
2.4. **IF no response within 2 business days**: Escalate to AP Manager.

**Step 3 — Validate invoice details**
3.1. Confirm invoice amount matches PO amount (within $0.00 tolerance for exact match; flag any variance)
3.2. **IF variance >$0**: Email vendor requesting corrected invoice. Do not approve until corrected.
3.3. Confirm delivery/services were received (check with requester if not confirmed in PO)

**Step 4 — Obtain approval**
4.1. **IF invoice total ≤ $5,000**: AP Clerk self-approves in NetSuite. Proceed to Step 5.
4.2. **IF invoice total > $5,000**: Route NetSuite approval request to department manager. Approval required within 3 business days. **IF not approved in 3 days**: Escalate to AP Manager.

**Step 5 — Schedule payment**
5.1. Set payment date per vendor terms (Net 30 = due date; early pay discount terms = discount date)
5.2. Add to weekly payment batch (run every Friday)
5.3. Update NetSuite bill status to "Approved — Scheduled"

**Step 6 — Record keeping**
6.1. File invoice PDF in `/Shared Drive/AP/Processed/[YYYY-MM]/`
6.2. NetSuite bill record serves as the official audit trail — do not delete

**Exception Handling**

| Exception | Action |
|-----------|--------|
| Duplicate invoice received | Mark second as duplicate in NetSuite; notify vendor |
| Vendor not in NetSuite | Submit vendor setup form to AP Manager before processing |
| Urgent payment request | AP Manager authorization required to bypass standard cycle |

---

## Variations

- **ISO 9001 format**: Add document control block, RACI matrix, and process flowchart reference
- **Healthcare/HIPAA version**: Add data handling safeguards and breach notification steps
- **Light version**: 1-page quick reference card for low-risk recurring tasks

## Related Prompts

- [Policy Writer](policy-writer.md) - The policy that governs what this SOP implements
- [Compliance Tracker](compliance-tracker.md) - Tracking SOP adherence and audit readiness
- [Records Management Expert](records-management-expert.md) - Document retention requirements
