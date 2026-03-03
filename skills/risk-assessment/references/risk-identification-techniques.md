# Risk Identification Techniques

## Risk Identification Techniques

```python
# Risk identification framework

class RiskIdentification:
    RISK_CATEGORIES = {
        'Technical': [
            'Technology maturity',
            'Integration complexity',
            'Performance requirements',
            'Security vulnerabilities',
            'Data integrity'
        ],
        'Resource': [
            'Team skill gaps',
            'Staff availability',
            'Budget constraints',
            'Equipment/infrastructure',
            'Vendor availability'
        ],
        'Schedule': [
            'Unrealistic deadlines',
            'Dependency delays',
            'Scope creep',
            'Approval delays',
            'Resource conflicts'
        ],
        'External': [
            'Regulatory changes',
            'Market conditions',
            'Vendor stability',
            'Political/economic factors',
            'Natural disasters'
        ],
        'Organizational': [
            'Stakeholder misalignment',
            'Priority changes',
            'Organizational restructuring',
            'Politics/conflicts',
            'Requirement changes'
        ]
    }

    @staticmethod
    def brainstorm_risks(project_context):
        """
        Facilitated brainstorming session to identify risks
        """
        risks = []
        for category, risk_types in RiskIdentification.RISK_CATEGORIES.items():
            for risk_type in risk_types:
                risks.append({
                    'category': category,
                    'description': risk_type,
                    'identified_by': [],
                    'probability': None,
                    'impact': None
                })

        return risks

    @staticmethod
    def analyze_assumptions_as_risks(assumptions):
        """
        Convert project assumptions into potential risks
        """
        assumption_risks = []
        for assumption in assumptions:
            assumption_risks.append({
                'risk_type': 'Assumption Violation',
                'description': f"Assumption '{assumption}' is invalid",
                'trigger': f"Evidence that {assumption} is false",
                'impact': 'High' if assumption.startswith('Critical') else 'Medium'
            })

        return assumption_risks
```
