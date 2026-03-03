# Python Memory Profiling

## Python Memory Profiling

```python
import tracemalloc
from typing import List, Tuple

class MemoryProfiler:
    def __init__(self):
        self.snapshots: List = []

    def start(self):
        """Start tracking memory allocations."""
        tracemalloc.start()

    def take_snapshot(self):
        """Take a memory snapshot."""
        snapshot = tracemalloc.take_snapshot()
        self.snapshots.append(snapshot)
        return snapshot

    def compare_snapshots(
        self,
        snapshot1_idx: int,
        snapshot2_idx: int,
        top_n: int = 10
    ):
        """Compare two snapshots."""
        snapshot1 = self.snapshots[snapshot1_idx]
        snapshot2 = self.snapshots[snapshot2_idx]

        stats = snapshot2.compare_to(snapshot1, 'lineno')

        print(f"\nTop {top_n} memory differences:")
        for stat in stats[:top_n]:
            print(f"{stat.size_diff / 1024:.1f} KB: {stat.traceback}")

    def get_top_allocations(self, snapshot_idx: int = -1, top_n: int = 10):
        """Get top memory allocations."""
        snapshot = self.snapshots[snapshot_idx]
        stats = snapshot.statistics('lineno')

        print(f"\nTop {top_n} memory allocations:")
        for stat in stats[:top_n]:
            print(f"{stat.size / 1024:.1f} KB: {stat.traceback}")

    def stop(self):
        """Stop tracking."""
        tracemalloc.stop()


# Usage
profiler = MemoryProfiler()
profiler.start()

# Take initial snapshot
profiler.take_snapshot()

# Run code
data = [i for i in range(1000000)]  # Allocate memory

# Take another snapshot
profiler.take_snapshot()

# Compare
profiler.compare_snapshots(0, 1)

profiler.stop()
```
