# Mutation Testing Reports

## Mutation Testing Reports

```bash
# Stryker HTML report shows:
# - Mutation score: 85.5%
# - Mutants killed: 94
# - Mutants survived: 16
# - Mutants timeout: 0
# - Mutants no coverage: 10

# Example mutations:
# ❌ Survived: Changed > to >= in isPositive
#    No test checks boundary condition
#
# ✅ Killed: Changed + to - in add method
#    Test expects specific result
#
# ❌ Survived: Removed if condition check
#    Missing test for that edge case
```
