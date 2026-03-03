# Dependency Mapping

## Dependency Mapping

```python
# Dependency mapping and tracking

class DependencyTracker:
    DEPENDENCY_TYPES = {
        'Finish-to-Start': 'Task B cannot start until Task A is complete',
        'Start-to-Start': 'Task B cannot start until Task A starts',
        'Finish-to-Finish': 'Task B cannot finish until Task A is complete',
        'Start-to-Finish': 'Task B cannot finish until Task A starts'
    }

    def __init__(self):
        self.tasks = []
        self.dependencies = []
        self.critical_path = []

    def create_dependency_map(self, tasks):
        """Create visual dependency network"""
        dependency_graph = {
            'nodes': [],
            'edges': [],
            'critical_items': []
        }

        for task in tasks:
            dependency_graph['nodes'].append({
                'id': task.id,
                'name': task.name,
                'duration': task.duration,
                'owner': task.owner,
                'status': task.status
            })

            for blocker in task.blocked_by:
                dependency_graph['edges'].append({
                    'from': blocker,
                    'to': task.id,
                    'type': 'Finish-to-Start',
                    'lag': 0  # days between tasks
                })

        return dependency_graph

    def analyze_critical_path(self, tasks):
        """Identify longest chain of dependent tasks"""
        paths = self.find_all_paths(tasks)
        critical_path = max(paths, key=len)

        return {
            'critical_items': critical_path,
            'total_duration': sum(t.duration for t in critical_path),
            'slack_available': 0,
            'any_delay_impacts_schedule': True,
            'monitoring_frequency': 'Daily'
        }

    def identify_blocking_dependencies(self, tasks):
        """Find tasks that block other work"""
        blocking_tasks = {}

        for task in tasks:
            blocked_count = sum(1 for t in tasks if task.id in t.blocked_by)
            if blocked_count > 0:
                blocking_tasks[task.id] = {
                    'task': task.name,
                    'blocking_count': blocked_count,
                    'blocked_tasks': [t.id for t in tasks if task.id in t.blocked_by],
                    'status': task.status,
                    'due_date': task.due_date,
                    'risk_level': 'High' if blocked_count > 3 else 'Medium'
                }

        return blocking_tasks

    def find_circular_dependencies(self, tasks):
        """Detect circular dependency chains"""
        cycles = []

        for task in tasks:
            visited = set()
            if self.has_cycle(task, visited, tasks):
                cycles.append({
                    'cycle': visited,
                    'severity': 'Critical',
                    'action': 'Resolve immediately'
                })

        return cycles

    def has_cycle(self, task, visited, tasks):
        visited.add(task.id)

        for blocker_id in task.blocked_by:
            blocker = next(t for t in tasks if t.id == blocker_id)

            if blocker.id in visited:
                return True
            if self.has_cycle(blocker, visited, tasks):
                return True

        visited.remove(task.id)
        return False
```
