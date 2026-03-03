# Color Contrast Validator

## Color Contrast Validator

```python
from typing import Tuple
import math

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance."""
    def adjust(color: int) -> float:
        c = color / 255.0
        if c <= 0.03928:
            return c / 12.92
        return math.pow((c + 0.055) / 1.055, 2.4)

    r, g, b = rgb
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """Calculate WCAG contrast ratio between two colors."""
    lum1 = calculate_luminance(hex_to_rgb(color1))
    lum2 = calculate_luminance(hex_to_rgb(color2))

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)

def check_wcag_compliance(
    foreground: str,
    background: str,
    level: str = 'AA',
    large_text: bool = False
) -> dict:
    """Check if color combination meets WCAG standards."""
    ratio = calculate_contrast_ratio(foreground, background)

    # WCAG 2.1 requirements
    requirements = {
        'AA': {'normal': 4.5, 'large': 3.0},
        'AAA': {'normal': 7.0, 'large': 4.5}
    }

    required_ratio = requirements[level]['large' if large_text else 'normal']
    passes = ratio >= required_ratio

    return {
        'ratio': round(ratio, 2),
        'required': required_ratio,
        'passes': passes,
        'level': level,
        'grade': 'Pass' if passes else 'Fail'
    }

# Usage
result = check_wcag_compliance('#000000', '#FFFFFF', 'AA', False)
print(f"Contrast ratio: {result['ratio']}:1")  # 21:1
print(f"WCAG {result['level']}: {result['grade']}")  # Pass
```
