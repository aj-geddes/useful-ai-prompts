# Migration Assessment and Planning

## Migration Assessment and Planning

```python
# Cloud migration assessment tool
from enum import Enum
from typing import Dict, List, Tuple
from dataclasses import dataclass

class MigrationStrategy(Enum):
    LIFT_AND_SHIFT = "lift_and_shift"  # Rehost
    REPLATFORM = "replatform"          # Rehost with optimizations
    REFACTOR = "refactor"              # Rebuild for cloud
    REPURCHASE = "repurchase"          # Switch to SaaS
    RETIRE = "retire"                  # Decommission

class ApplicationComplexity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class ApplicationAssessment:
    name: str
    complexity: ApplicationComplexity
    dependencies: List[str]
    estimated_effort: int  # days
    business_criticality: int  # 1-10
    current_costs: float  # annual
    cloud_costs_estimate: float  # annual

class CloudMigrationPlanner:
    def __init__(self):
        self.applications: List[ApplicationAssessment] = []
        self.total_effort = 0
        self.total_cost_savings = 0

    def add_application(self, app: ApplicationAssessment):
        """Add application to migration assessment"""
        self.applications.append(app)

    def recommend_migration_strategy(self, app: ApplicationAssessment) -> MigrationStrategy:
        """Recommend migration strategy based on application characteristics"""
        if app.complexity == ApplicationComplexity.LOW:
            return MigrationStrategy.LIFT_AND_SHIFT

        elif app.complexity == ApplicationComplexity.MEDIUM:
            # Check if cost savings justify refactoring
            annual_savings = app.current_costs - app.cloud_costs_estimate
            refactor_cost = app.estimated_effort * 500  # cost per day
            payback_months = (refactor_cost / annual_savings) * 12 if annual_savings > 0 else float('inf')

            if payback_months < 6:
                return MigrationStrategy.REFACTOR
            else:
                return MigrationStrategy.REPLATFORM

        else:  # HIGH complexity
            # Evaluate if modernization is worthwhile
            if app.business_criticality >= 8:
                return MigrationStrategy.REFACTOR
            else:
                return MigrationStrategy.RETIRE  # Consider retiring

    def create_migration_wave_plan(self) -> Dict:
        """Create phased migration plan"""
        # Sort by criticality and dependencies
        sorted_apps = sorted(
            self.applications,
            key=lambda x: (len(x.dependencies), -x.business_criticality)
        )

        waves = {
            'wave_1': [],  # Low-risk, few dependencies
            'wave_2': [],  # Medium-risk
            'wave_3': []   # High-risk or critical
        }

        migrated = set()

        for app in sorted_apps:
            # Check if dependencies are satisfied
            deps_satisfied = all(dep in migrated for dep in app.dependencies)

            if not deps_satisfied:
                continue

            if app.complexity == ApplicationComplexity.LOW:
                waves['wave_1'].append(app.name)
            elif app.complexity == ApplicationComplexity.MEDIUM:
                waves['wave_2'].append(app.name)
            else:
                waves['wave_3'].append(app.name)

            migrated.add(app.name)

        return {
            'waves': waves,
            'total_applications': len(self.applications),
            'migrated_count': len(migrated),
            'total_effort_days': sum(app.estimated_effort for app in self.applications)
        }

    def calculate_roi(self) -> Dict:
        """Calculate migration ROI"""
        total_current_costs = sum(app.current_costs for app in self.applications)
        total_cloud_costs = sum(app.cloud_costs_estimate for app in self.applications)
        annual_savings = total_current_costs - total_cloud_costs

        # Estimate migration costs
        total_effort = sum(app.estimated_effort for app in self.applications)
        migration_cost = total_effort * 250  # cost per day

        payback_months = (migration_cost / annual_savings) * 12 if annual_savings > 0 else float('inf')

        return {
            'total_current_costs': total_current_costs,
            'total_cloud_costs': total_cloud_costs,
            'annual_savings': annual_savings,
            'migration_cost': migration_cost,
            'payback_months': payback_months,
            'year1_savings': annual_savings - migration_cost,
            'year3_savings': (annual_savings * 3) - migration_cost
        }

# Usage
planner = CloudMigrationPlanner()

app1 = ApplicationAssessment(
    name="Web Frontend",
    complexity=ApplicationComplexity.LOW,
    dependencies=[],
    estimated_effort=5,
    business_criticality=7,
    current_costs=50000,
    cloud_costs_estimate=30000
)

app2 = ApplicationAssessment(
    name="API Backend",
    complexity=ApplicationComplexity.MEDIUM,
    dependencies=["Database"],
    estimated_effort=20,
    business_criticality=9,
    current_costs=80000,
    cloud_costs_estimate=40000
)

app3 = ApplicationAssessment(
    name="Database",
    complexity=ApplicationComplexity.HIGH,
    dependencies=[],
    estimated_effort=30,
    business_criticality=10,
    current_costs=120000,
    cloud_costs_estimate=80000
)

planner.add_application(app1)
planner.add_application(app2)
planner.add_application(app3)

print("Migration Wave Plan:")
print(planner.create_migration_wave_plan())

print("\nROI Analysis:")
print(planner.calculate_roi())
```
