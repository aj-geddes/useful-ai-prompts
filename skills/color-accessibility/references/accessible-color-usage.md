# Accessible Color Usage

## Accessible Color Usage

```yaml
Color Usage Guidelines:

Status Indicators:

Error:
  Color: #D32F2F (red)
  Contrast: 4.5:1 minimum
  Additional: Error icon, text "Error"
  Don't: Use ONLY red, no other indication

Success:
  Color: #388E3C (green)
  Contrast: 4.5:1 minimum
  Additional: Checkmark icon, text "Success"
  Don't: Use ONLY green

Warning:
  Color: #F57C00 (orange)
  Contrast: 4.5:1 minimum
  Additional: Warning icon, text "Warning"
  Don't: Use ONLY orange

Info:
  Color: #1976D2 (blue)
  Contrast: 4.5:1 minimum
  Additional: Info icon, text "Info"
  Don't: Use ONLY blue

---
Data Visualization:

Charts & Graphs:
  - Use 8+ color combinations for color blindness
  - Include patterns or textures
  - Label elements directly (not legend only)
  - Use colorblind-friendly palettes

Recommended Palettes:
  - ColorBrewer (designed for accessibility)
  - Okabe-Ito palette
  - Paul Tol colors

Heat Maps:
  - Sequential palettes only
  - Avoid red-green combinations
  - Test with simulator

---
UI Component States:

Button States:
  - Default: Primary color
  - Hover: Slightly darker
  - Disabled: Gray with reduced contrast
  - Focus: Outline indicator (not color alone)
  - Active: Darker shade

Form Validation:
  - Invalid: Red + error icon + message
  - Valid: Green + checkmark icon (optional)
  - Required: No special color, use text label

Interactive Elements:
  - Focus: Visible outline or ring
  - Selected: Checkmark or checkmark icon + color
  - Hover: Underline + color change
  - Don't: Use color alone to indicate state
```
