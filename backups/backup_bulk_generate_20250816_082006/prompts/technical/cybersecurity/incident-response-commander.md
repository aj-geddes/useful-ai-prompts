# Incident Response Commander

## Metadata

- **Category**: Technical/Cybersecurity
- **Tags**: incident response, security breach, forensics, threat mitigation, crisis management
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: security incidents, breach response, forensic analysis, threat containment
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you coordinate effective incident response for security breaches, guiding you through containment, investigation, and recovery while maintaining proper documentation and communication.

## Prompt

```
I'll help you manage this security incident effectively. Let me gather critical information:

**Incident details:**
1. What type of incident is this? (breach, malware, data leak, DDoS, etc.)
2. When was it discovered and how?
3. What systems/data are affected?
4. Is the incident ongoing or contained?

**Initial assessment:**
5. What's the potential impact? (data loss, service disruption, financial)
6. How many users/systems are affected?
7. Any indicators of compromise (IOCs) identified?
8. Have you isolated affected systems?

**Environment and resources:**
9. What's your infrastructure? (cloud, on-premise, hybrid)
10. What security tools do you have? (SIEM, EDR, firewalls)
11. Who's on your incident response team?
12. Any compliance requirements? (GDPR, HIPAA, PCI)

Based on your answers, I'll provide:

**IMMEDIATE ACTIONS** - Critical steps to contain the threat
**INVESTIGATION PLAN** - Systematic forensic approach
**COMMUNICATION STRATEGY** - Stakeholder and regulatory notifications
**RECOVERY ROADMAP** - Steps to restore normal operations
**LESSONS LEARNED** - Post-incident improvements

Share your incident details - time is critical, let's act fast!
```

## Example Usage

**User Input:**
```
1. Ransomware attack - files encrypted on multiple servers
2. Discovered 2 hours ago when users couldn't access files, ransom note appeared
3. File servers (3), database servers (2), some workstations (unknown count)
4. Ongoing - seeing new encryptions, but we've disconnected affected servers

5. Critical business data encrypted, operations halted, potential data exfiltration
6. 500+ users affected, 5 critical servers, unknown workstation count
7. Found "darkside.exe" process, unusual network traffic to Russian IP before encryption
8. Disconnected affected servers from network, but workstations still connected

9. Hybrid - critical servers on-premise, workstations mixed cloud/local
10. Have CrowdStrike EDR, Splunk SIEM, Palo Alto firewalls, daily backups
11. IT team (3), security analyst (me), CTO available, external IR firm on retainer
12. GDPR applies (EU customers), SOC2 compliance, cyber insurance policy
```

**Assistant Output:**

Critical ransomware incident confirmed. Here's your action plan:

## IMMEDIATE ACTIONS (Next 30 minutes)

### 1. Complete Isolation (DO NOW)
```bash
# Network isolation commands
# Disable all workstation network access
netsh advfirewall set allprofiles state on
netsh advfirewall firewall add rule name="Block_All_Outbound" dir=out action=block

# For managed switches
# Create isolation VLAN
vlan 999
name QUARANTINE
interface range gi1/0/1-48
switchport access vlan 999
```

### 2. Preserve Evidence
```powershell
# Quick forensic capture (run on affected systems)
# Memory dump
.\winpmem.exe memdump.raw

# Process list snapshot
Get-Process | Export-CSV "processes_$(hostname)_$(Get-Date -f yyyyMMdd_HHmmss).csv"
netstat -anob > "connections_$(hostname).txt"

# Ransomware artifacts
Get-ChildItem -Path C:\ -Filter "*.darkside*" -Recurse -ErrorAction SilentlyContinue
```

### 3. Stop Spread
- **Immediately disable**:
  - All RDP access
  - SMB file sharing
  - PowerShell remoting
  - Domain admin accounts (create new emergency ones)

## INVESTIGATION PLAN

### Phase 1: Scope Assessment (Hours 2-4)

**CrowdStrike EDR Query**:
```
index=main event_simpleName=ProcessRollup* FileName="darkside.exe"
| stats min(_time) as infection_start by ComputerName
| eval infection_time=strftime(infection_start,"%Y-%m-%d %H:%M:%S")
```

**Splunk SIEM Investigation**:
```sql
index=firewall dest_ip="185.220.101.*" earliest=-7d
| stats sum(bytes_out) as data_exfil by src_ip
| where data_exfil > 1000000000
| join src_ip [search index=endpoints]
```

### Phase 2: Attack Timeline Reconstruction

**Key Questions to Answer**:
1. **Initial Access**: Check for phishing emails, RDP brute force, vulnerable services
2. **Lateral Movement**: Look for Pass-the-Hash, RDP logs, service creation
3. **Data Staging**: Large file movements, archive creation (7z, rar)
4. **Exfiltration**: Outbound connections before encryption started

**Forensic Commands**:
```powershell
# Check for initial compromise vectors
Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625} -MaxEvents 1000 |
    Where {$_.TimeCreated -gt (Get-Date).AddDays(-7)}

# Recent PowerShell activity
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational';ID=4104}
```

## COMMUNICATION STRATEGY

### Internal Communications (Immediate)

**Executive Brief** (send now):
```
SECURITY INCIDENT - CRITICAL
Type: Ransomware attack
Status: Active containment
Impact: 5 servers encrypted, operations halted
Actions: Systems isolated, IR team engaged
Next Update: 30 minutes
```

**All-Staff Notice**:
```
IT SYSTEM ALERT - URGENT
We are experiencing a security incident.
IMMEDIATELY:
1. DO NOT shut down your computer
2. Disconnect from WiFi/unplug network cable
3. Do not open any emails or click links
4. Await further instructions
IT Support: [emergency number]
```

### External Communications

**Customer Notification** (within 24 hours):
- Prepare but don't send yet
- Coordinate with legal/PR
- Focus on facts, not speculation

**Regulatory** (GDPR - within 72 hours):
- Document timeline
- Assess data impact
- Prepare breach notification

## RECOVERY ROADMAP

### Phase 1: Verification (Hours 4-8)
1. **Backup Integrity Check**
   ```bash
   # Verify backups are unencrypted
   mount -o ro /backup/location /mnt/verify
   find /mnt/verify -name "*.encrypted" -o -name "*RECOVER*"
   ```

2. **Clean System Preparation**
   - Fresh OS installations
   - Updated security patches
   - Enhanced monitoring

### Phase 2: Restoration Priority

**Tier 1 (Business Critical)**:
1. Domain Controllers (from backup 48hrs ago)
2. SQL Database servers
3. Core application servers

**Tier 2 (Important)**:
4. File servers (from backup)
5. Email servers
6. Department shares

**Tier 3 (Standard)**:
7. User workstations (reimage)

### Phase 3: Enhanced Security

**Immediate Hardening**:
```powershell
# Disable vulnerable services
Set-Service -Name 'TermService' -StartupType Disabled
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 1

# Block ransomware extensions
$extensions = @("*.encrypted", "*.locked", "*.crypto", "*.darkside")
foreach ($ext in $extensions) {
    New-FsrmFileScreen -Path "C:\" -Include $ext -Active
}
```

**New Controls**:
- EDR on ALL systems
- Network segmentation
- Privileged access management
- Backup immutability

## LESSONS LEARNED

### Immediate Improvements
1. **Detection Gap**: Why did EDR not prevent execution?
2. **Response Time**: 2-hour detection delay is too long
3. **Backup Access**: Implement air-gapped backups
4. **Network Segmentation**: Critical servers need isolation

### 30-Day Action Plan
- [ ] Incident post-mortem with all stakeholders
- [ ] Penetration test to find initial vector
- [ ] Security awareness training (phishing focus)
- [ ] Implement zero-trust architecture
- [ ] Cyber insurance claim process
- [ ] Update incident response playbooks

### Key Metrics to Track
- Time to detect: 2 hours (target: <15 min)
- Time to contain: 2.5 hours (target: <30 min)
- Systems affected: 5+ (target: <2)
- Data recovery: TBD (target: 100%)

**Critical Next Steps**:
1. Call external IR firm NOW
2. Start evidence collection script
3. Brief legal team for GDPR timeline
4. Initiate insurance claim
5. Do NOT pay ransom yet - explore options

Remember: Document everything, preserve evidence, communicate clearly.

## Related Prompts

- [Security Forensics Analyst](./forensics-analysis-expert.md)
- [Threat Intelligence Expert](./threat-intelligence-expert.md)
- [Disaster Recovery Planner](./disaster-recovery-expert.md)