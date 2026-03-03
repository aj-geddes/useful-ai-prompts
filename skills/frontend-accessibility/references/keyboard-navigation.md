# Keyboard Navigation

## Keyboard Navigation

```typescript
// React Component with keyboard support
import React, { useEffect, useRef, useState } from 'react';

interface MenuItem {
  id: string;
  label: string;
  href: string;
}

const KeyboardNavigationMenu: React.FC<{ items: MenuItem[] }> = ({ items }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      switch (e.key) {
        case 'ArrowLeft':
        case 'ArrowUp':
          e.preventDefault();
          setActiveIndex(prev =>
            prev === 0 ? items.length - 1 : prev - 1
          );
          break;

        case 'ArrowRight':
        case 'ArrowDown':
          e.preventDefault();
          setActiveIndex(prev =>
            prev === items.length - 1 ? 0 : prev + 1
          );
          break;

        case 'Home':
          e.preventDefault();
          setActiveIndex(0);
          break;

        case 'End':
          e.preventDefault();
          setActiveIndex(items.length - 1);
          break;

        case 'Enter':
        case ' ':
          e.preventDefault();
          const link = menuRef.current?.querySelectorAll('a')[activeIndex];
          link?.click();
          break;

        case 'Escape':
          menuRef.current?.querySelector('a')?.blur();
          break;

        default:
          break;
      }
    };

    menuRef.current?.addEventListener('keydown', handleKeyDown);
    return () => menuRef.current?.removeEventListener('keydown', handleKeyDown);
  }, [items.length, activeIndex]);

  return (
    <div role="menubar" ref={menuRef}>
      {items.map((item, index) => (
        <a
          key={item.id}
          href={item.href}
          role="menuitem"
          tabIndex={index === activeIndex ? 0 : -1}
          onFocus={() => setActiveIndex(index)}
          aria-current={index === activeIndex ? 'page' : undefined}
        >
          {item.label}
        </a>
      ))}
    </div>
  );
};
```
