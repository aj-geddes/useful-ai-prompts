# Vitest for Vue Testing

## Vitest for Vue Testing

```typescript
// Button.spec.ts
import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import Button from "./Button.vue";

describe("Button.vue", () => {
  it("renders slot content", () => {
    const wrapper = mount(Button, {
      slots: {
        default: "Click me",
      },
    });
    expect(wrapper.text()).toContain("Click me");
  });

  it("emits click event", async () => {
    const wrapper = mount(Button);
    await wrapper.trigger("click");
    expect(wrapper.emitted("click")).toHaveLength(1);
  });

  it("disables button when disabled prop is true", () => {
    const wrapper = mount(Button, {
      props: { disabled: true },
    });
    expect(wrapper.attributes("disabled")).toBeDefined();
  });

  it("applies variant class", () => {
    const wrapper = mount(Button, {
      props: { variant: "primary" },
    });
    expect(wrapper.classes()).toContain("bg-blue-500");
  });
});

// composable.spec.ts
import { describe, it, expect } from "vitest";
import { useCounter } from "./useCounter";

describe("useCounter", () => {
  it("initializes with default value", () => {
    const { count } = useCounter();
    expect(count.value).toBe(0);
  });

  it("increments count", () => {
    const { count, increment } = useCounter();
    increment();
    expect(count.value).toBe(1);
  });
});
```
