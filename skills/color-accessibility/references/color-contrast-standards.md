# Color Contrast Standards

## Color Contrast Standards

```yaml
WCAG Contrast Ratios:

WCAG AA (Minimum):
  - Normal text: 4.5:1
  - Large text (18pt+): 3:1
  - UI components & graphical elements: 3:1
  - Focus indicators: 3:1

WCAG AAA (Enhanced):
  - Normal text: 7:1
  - Large text: 4.5:1
  - Better for accessibility

---
Testing Contrast:

Tools:
  - WebAIM Contrast Checker
  - Color Contrast Analyzer
  - Figma plugins
  - Browser DevTools

Formula (WCAG): Contrast = (L1 + 0.05) / (L2 + 0.05)
  Where L = relative luminance

Example Pairs:

Good (Pass AA):
  - Black (#000000) on White (#FFFFFF) = 21:1 ✓
  - White on Dark Blue (#003366) = 12.6:1 ✓
  - Dark Gray (#333333) on Light Gray (#EEEEEE) = 10:1 ✓

Poor (Fail):
  - Light Gray (#CCCCCC) on White (#FFFFFF) = 1.3:1 ✗
  - Yellow (#FFFF00) on White (#FFFFFF) = 1.07:1 ✗
```
