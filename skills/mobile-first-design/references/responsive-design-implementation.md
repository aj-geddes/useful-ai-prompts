# Responsive Design Implementation

## Responsive Design Implementation

```python
# Implement responsive CSS and layouts

class ResponsiveDesign:
    def create_responsive_grid(self, mobile_cols=1):
        """CSS Grid responsive structure"""
        return {
            'mobile': {
                'columns': 1,
                'gap': '16px',
                'breakpoint': 'max-width: 480px'
            },
            'tablet': {
                'columns': 2,
                'gap': '24px',
                'breakpoint': '481px - 768px'
            },
            'desktop': {
                'columns': 3,
                'gap': '32px',
                'breakpoint': 'min-width: 769px'
            }
        }

    def responsive_typography(self):
        """Fluid font sizes"""
        return {
            'h1': {
                'mobile': '24px',
                'tablet': '32px',
                'desktop': '48px',
                'line_height': {
                    'mobile': '1.2',
                    'desktop': '1.3'
                }
            },
            'body': {
                'mobile': '14px',
                'tablet': '16px',
                'desktop': '16px',
                'line_height': '1.6'
            }
        }

    def responsive_spacing(self):
        """Adaptive padding and margins"""
        return {
            'container_padding': {
                'mobile': '16px',
                'tablet': '24px',
                'desktop': '32px'
            },
            'section_margin': {
                'mobile': '24px',
                'desktop': '48px'
            },
            'touch_target_size': '44px minimum (Apple)'
        }

    def touch_friendly_design(self):
        """Mobile interaction optimization"""
        return {
            'button_size': '44px x 44px minimum',
            'touch_target_spacing': '8px minimum between',
            'form_input_height': '44px + 16px padding',
            'scrolling_area': 'Full width swipe friendly',
            'modal_height': 'Max 85vh, scrollable',
            'keyboard_awareness': 'Account for software keyboard'
        }
```
