# Color Vision Deficiency Simulation

## Color Vision Deficiency Simulation

```python
# Design for color vision deficiency

class ColorAccessibility:
    COLOR_DEFICIENCY_TYPES = {
        'Protanopia': 'Red-blind (1% male)',
        'Deuteranopia': 'Green-blind (1% male)',
        'Tritanopia': 'Blue-yellow blind (very rare)',
        'Monochromacy': 'Complete color blindness (very rare)'
    }

    def simulate_vision_deficiency(self, color, deficiency_type):
        """Simulate how color appears to different eyes"""
        # Color blind simulation
        simulated_colors = {
            'normal': color,
            'protanopia': self.apply_protanopia_filter(color),
            'deuteranopia': self.apply_deuteranopia_filter(color),
            'tritanopia': self.apply_tritanopia_filter(color)
        }
        return simulated_colors

    def check_palette_accessibility(self, color_palette):
        """Validate entire palette for accessibility"""
        issues = []

        # Check contrast ratios
        for color_pair in self.generate_pairs(color_palette):
            contrast = self.calculate_contrast(color_pair[0], color_pair[1])
            if contrast < 4.5:
                issues.append({
                    'type': 'Low contrast',
                    'colors': color_pair,
                    'ratio': contrast,
                    'severity': 'Critical'
                })

        # Check color blind differentiation
        for deficiency in self.COLOR_DEFICIENCY_TYPES:
            simulated = self.simulate_for_deficiency(color_palette, deficiency)
            if not self.are_colors_distinguishable(simulated):
                issues.append({
                    'type': 'Color blindness',
                    'deficiency': deficiency,
                    'severity': 'High'
                })

        return {
            'palette': color_palette,
            'issues': issues,
            'is_accessible': len(issues) == 0,
            'recommendations': self.generate_recommendations(issues)
        }

    def generate_recommendations(self, issues):
        """Suggest palette improvements"""
        return [
            'Use patterns or icons to differentiate (not just color)',
            'Increase contrast ratios',
            'Use tested accessible color combinations',
            'Test with color blindness simulator before launch'
        ]
```
