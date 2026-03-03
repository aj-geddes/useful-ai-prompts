# Python Code Metrics (using radon)

## Python Code Metrics (using radon)

```python
from radon.complexity import cc_visit
from radon.metrics import mi_visit, h_visit
from radon.raw import analyze
import os
from typing import Dict, List
import json

class CodeMetricsAnalyzer:
    def analyze_file(self, file_path: str) -> Dict:
        """Analyze a single Python file."""
        with open(file_path, 'r') as f:
            code = f.read()

        # Cyclomatic complexity
        complexity = cc_visit(code)

        # Maintainability index
        mi = mi_visit(code, True)

        # Halstead metrics
        halstead = h_visit(code)

        # Raw metrics
        raw = analyze(code)

        return {
            'file': file_path,
            'complexity': [{
                'name': block.name,
                'complexity': block.complexity,
                'lineno': block.lineno
            } for block in complexity],
            'maintainability_index': mi,
            'halstead': {
                'volume': halstead.total.volume if halstead.total else 0,
                'difficulty': halstead.total.difficulty if halstead.total else 0,
                'effort': halstead.total.effort if halstead.total else 0
            },
            'raw': {
                'loc': raw.loc,
                'lloc': raw.lloc,
                'sloc': raw.sloc,
                'comments': raw.comments,
                'multi': raw.multi,
                'blank': raw.blank
            }
        }

    def analyze_project(self, directory: str) -> List[Dict]:
        """Analyze all Python files in a project."""
        results = []

        for root, dirs, files in os.walk(directory):
            # Skip common directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', 'node_modules']]

            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        result = self.analyze_file(file_path)
                        results.append(result)
                    except Exception as e:
                        print(f"Error analyzing {file_path}: {e}")

        return results

    def generate_report(self, results: List[Dict]) -> str:
        """Generate a markdown report."""
        report = "# Code Metrics Report\n\n"

        # Summary
        total_files = len(results)
        avg_mi = sum(r['maintainability_index'] for r in results) / total_files if total_files > 0 else 0
        total_loc = sum(r['raw']['loc'] for r in results)

        report += "## Summary\n\n"
        report += f"- Total Files: {total_files}\n"
        report += f"- Total LOC: {total_loc}\n"
        report += f"- Average Maintainability Index: {avg_mi:.2f}\n\n"

        # High complexity functions
        report += "## High Complexity Functions\n\n"

        high_complexity = []
        for result in results:
            for func in result['complexity']:
                if func['complexity'] > 10:
                    high_complexity.append({
                        'file': result['file'],
                        **func
                    })

        high_complexity.sort(key=lambda x: x['complexity'], reverse=True)

        if not high_complexity:
            report += "None found.\n\n"
        else:
            for func in high_complexity[:10]:  # Top 10
                report += f"- {func['file']}:{func['lineno']} - {func['name']}\n"
                report += f"  Complexity: {func['complexity']}\n\n"

        # Low maintainability files
        report += "## Low Maintainability Files\n\n"

        low_mi = [r for r in results if r['maintainability_index'] < 65]
        low_mi.sort(key=lambda x: x['maintainability_index'])

        if not low_mi:
            report += "None found.\n\n"
        else:
            for file in low_mi[:10]:
                report += f"- {file['file']}\n"
                report += f"  MI: {file['maintainability_index']:.2f}\n"
                report += f"  LOC: {file['raw']['loc']}\n\n"

        return report

    def export_json(self, results: List[Dict], output_file: str):
        """Export results as JSON."""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)


# Usage
analyzer = CodeMetricsAnalyzer()
results = analyzer.analyze_project('./src')
report = analyzer.generate_report(results)
print(report)

# Export to JSON
analyzer.export_json(results, 'metrics.json')
```
