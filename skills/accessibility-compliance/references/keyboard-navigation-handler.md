# Keyboard Navigation Handler

## Keyboard Navigation Handler

```typescript
// Keyboard navigation utilities
export const KeyboardNavigation = {
  // Handle arrow key navigation in lists
  handleListNavigation: (event: KeyboardEvent, items: HTMLElement[]) => {
    const currentIndex = items.findIndex(
      (item) => item === document.activeElement,
    );

    let nextIndex: number;

    switch (event.key) {
      case "ArrowDown":
        event.preventDefault();
        nextIndex = Math.min(currentIndex + 1, items.length - 1);
        items[nextIndex]?.focus();
        break;

      case "ArrowUp":
        event.preventDefault();
        nextIndex = Math.max(currentIndex - 1, 0);
        items[nextIndex]?.focus();
        break;

      case "Home":
        event.preventDefault();
        items[0]?.focus();
        break;

      case "End":
        event.preventDefault();
        items[items.length - 1]?.focus();
        break;
    }
  },

  // Make element keyboard accessible
  makeAccessible: (element: HTMLElement, onClick: () => void): void => {
    element.setAttribute("tabindex", "0");
    element.setAttribute("role", "button");

    element.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        onClick();
      }
    });
  },
};
```
