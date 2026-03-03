# Animation & Transition Design

## Animation & Transition Design

```python
# Define animations and transitions

class InteractionDesign:
    def define_animation(self, interaction):
        """Specify animation properties"""
        return {
            'trigger': interaction.trigger,  # Click, hover, load
            'element': interaction.element,
            'animation': {
                'type': interaction.animation_type,  # Fade, slide, scale
                'duration': interaction.duration,     # 200-400ms typical
                'easing': interaction.easing_fn,      # Ease-in-out
                'delay': interaction.delay_ms
            },
            'purpose': interaction.purpose,  # Feedback, guidance, delight
            'platform': ['Desktop', 'Mobile'],  # Platform-specific
            'accessibility': {
                'respects_prefers_reduced_motion': True,
                'non_distract': 'Critical interactions only'
            }
        }

    def define_transitions(self):
        """Page/screen transitions"""
        return {
            'navigation_forward': {
                'animation': 'Slide right',
                'duration': '300ms',
                'easing': 'ease-out'
            },
            'navigation_back': {
                'animation': 'Slide left',
                'duration': '300ms',
                'easing': 'ease-out'
            },
            'modal_open': {
                'animation': 'Fade + Scale up',
                'duration': '200ms',
                'easing': 'ease-out'
            },
            'modal_close': {
                'animation': 'Fade + Scale down',
                'duration': '150ms',
                'easing': 'ease-in'
            }
        }

    def animation_guidelines(self):
        """Best practices for animation"""
        return {
            'duration': {
                'micro_interactions': '100-200ms',
                'transitions': '200-400ms',
                'entrance_animations': '300-500ms',
                'avoid': '>500ms (feels sluggish)'
            },
            'easing': {
                'entrance': 'Ease out (fast start, slow end)',
                'exit': 'Ease in (slow start, fast end)',
                'focus': 'Ease-in-out for smooth feel'
            },
            'purpose': [
                'Provide feedback',
                'Guide user attention',
                'Communicate state change',
                'Delight users',
                'Avoid: Distraction, slowness'
            ]
        }
```
