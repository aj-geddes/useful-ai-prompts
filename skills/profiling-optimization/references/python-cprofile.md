# Python cProfile

## Python cProfile

```python
import cProfile
import pstats
from pstats import SortKey
import io

class Profiler:
    def __init__(self):
        self.profiler = cProfile.Profile()

    def __enter__(self):
        self.profiler.enable()
        return self

    def __exit__(self, *args):
        self.profiler.disable()

    def print_stats(self, sort_by: str = 'cumulative'):
        """Print profiling statistics."""
        s = io.StringIO()
        ps = pstats.Stats(self.profiler, stream=s)

        if sort_by == 'time':
            ps.sort_stats(SortKey.TIME)
        elif sort_by == 'cumulative':
            ps.sort_stats(SortKey.CUMULATIVE)
        elif sort_by == 'calls':
            ps.sort_stats(SortKey.CALLS)

        ps.print_stats(20)  # Top 20
        print(s.getvalue())

    def save_stats(self, filename: str):
        """Save profiling data."""
        self.profiler.dump_stats(filename)

# Usage
with Profiler() as prof:
    # Code to profile
    result = expensive_function()

prof.print_stats('cumulative')
prof.save_stats('profile.prof')
```
