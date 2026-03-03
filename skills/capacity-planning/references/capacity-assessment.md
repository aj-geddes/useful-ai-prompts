# Capacity Assessment

## Capacity Assessment

```python
# Team capacity calculation and planning

class CapacityPlanner:
    # Standard work hours per week
    STANDARD_WEEK_HOURS = 40

    # Activities that reduce available capacity
    OVERHEAD_HOURS = {
        'meetings': 5,           # standups, 1-on-1s, planning
        'training': 2,           # learning new tech
        'administrative': 2,     # emails, approvals
        'support': 2,            # helping teammates
        'contingency': 2         # interruptions, emergencies
    }

    def __init__(self, team_size, sprint_duration_weeks=2):
        self.team_size = team_size
        self.sprint_duration_weeks = sprint_duration_weeks
        self.members = []

    def calculate_team_capacity(self):
        """Calculate available capacity hours"""
        # Base capacity
        base_hours = self.team_size * self.STANDARD_WEEK_HOURS * self.sprint_duration_weeks

        # Subtract overhead
        overhead = sum(self.OVERHEAD_HOURS.values()) * self.team_size * self.sprint_duration_weeks

        # Subtract absences
        absence_hours = self.calculate_absences()

        # Available capacity
        available_capacity = base_hours - overhead - absence_hours

        return {
            'base_hours': base_hours,
            'overhead_hours': overhead,
            'absence_hours': absence_hours,
            'available_capacity': available_capacity,
            'utilization_target': '85%',  # Leave 15% buffer
            'target_commitment': available_capacity * 0.85
        }

    def calculate_absences(self):
        """Account for vacation, sick, etc."""
        absence_days = 0

        # Standard absences
        vacation_days = 15  # annual
        sick_days = 5       # annual
        holidays = 10       # annual

        # Convert to per-sprint
        absence_days = (vacation_days + sick_days + holidays) / 52 * self.sprint_duration_weeks

        absence_hours = absence_days * 8 * self.team_size
        return absence_hours

    def allocate_to_projects(self, projects, team):
        """Allocate capacity across multiple projects"""
        allocation = {}
        total_allocation = 0

        # Allocate by priority
        for project in sorted(projects, key=lambda p: p.priority):
            required_hours = project.effort_hours
            available = self.calculate_team_capacity()['available_capacity'] - total_allocation

            if available >= required_hours:
                allocation[project.id] = {
                    'project': project.name,
                    'allocated': required_hours,
                    'team_members': int(required_hours / (self.STANDARD_WEEK_HOURS * self.sprint_duration_weeks)),
                    'allocation_percent': (required_hours / available * 100)
                }
                total_allocation += required_hours
            else:
                allocation[project.id] = {
                    'project': project.name,
                    'allocated': available,
                    'status': 'Insufficient capacity',
                    'shortfall': required_hours - available,
                    'recommendation': 'Add resources or defer scope'
                }
                total_allocation = available

        return allocation

    def identify_bottlenecks(self, skills, projects):
        """Find skill constraints"""
        bottlenecks = []

        for skill in skills:
            people_with_skill = sum(1 for p in self.members if skill in p.skills)
            projects_needing_skill = sum(1 for p in projects if skill in p.required_skills)

            utilization = (projects_needing_skill / people_with_skill * 100) if people_with_skill > 0 else 0

            if utilization > 100:
                bottlenecks.append({
                    'skill': skill,
                    'people_available': people_with_skill,
                    'projects_needing': projects_needing_skill,
                    'utilization': utilization,
                    'severity': 'Critical',
                    'actions': ['Cross-train team', 'Hire specialist', 'Adjust scope']
                })

        return bottlenecks
```
