# Chromatic for Storybook

## Chromatic for Storybook

```typescript
// .storybook/main.ts
export default {
  addons: ['@storybook/addon-essentials'],
  framework: '@storybook/react',
};

// Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    chromatic: {
      viewports: [320, 768, 1200],  // Test responsive
      delay: 300,                    // Wait for animations
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Button',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Button',
  },
};

export const Disabled: Story = {
  args: {
    variant: 'primary',
    disabled: true,
    children: 'Disabled Button',
  },
};

export const WithIcon: Story = {
  args: {
    children: (
      <>
        <Icon name="arrow-right" /> Continue
      </>
    ),
  },
};

// Test hover states
export const HoverState: Story = {
  args: {
    variant: 'primary',
    children: 'Hover Me',
  },
  parameters: {
    pseudo: { hover: true },
  },
};

// Test focus states
export const FocusState: Story = {
  args: {
    variant: 'primary',
    children: 'Focus Me',
  },
  parameters: {
    pseudo: { focus: true },
  },
};
```

```bash
# Install Chromatic
npm install --save-dev chromatic

# Run visual tests
npx chromatic --project-token=<TOKEN>

# In CI
npx chromatic --exit-zero-on-changes
```
