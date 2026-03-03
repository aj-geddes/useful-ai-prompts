# Pluralization Rules

## Pluralization Rules

```typescript
// pluralization.ts
export class PluralRules {
  constructor(private locale: string) {}

  // Get plural category
  select(count: number): Intl.LDMLPluralRule {
    const pr = new Intl.PluralRules(this.locale);
    return pr.select(count);
  }

  // Format with pluralization
  format(count: number, forms: Record<Intl.LDMLPluralRule, string>): string {
    const rule = this.select(count);
    return forms[rule] || forms.other;
  }
}

// Usage
const enRules = new PluralRules("en");

console.log(
  enRules.format(0, {
    zero: "No items",
    one: "One item",
    other: "{{count}} items",
  }),
);

console.log(
  enRules.format(1, {
    one: "One item",
    other: "{{count}} items",
  }),
);

// Different languages have different plural rules
const arRules = new PluralRules("ar"); // Arabic has 6 plural forms
const plRules = new PluralRules("pl"); // Polish has complex plural rules
```

### ICU Message Format

```typescript
// Using intl-messageformat
import IntlMessageFormat from "intl-messageformat";

const message = new IntlMessageFormat(
  "{count, plural, =0 {No items} one {# item} other {# items}}",
  "en",
);

console.log(message.format({ count: 0 })); // No items
console.log(message.format({ count: 1 })); // 1 item
console.log(message.format({ count: 5 })); // 5 items

// With gender
const genderMessage = new IntlMessageFormat(
  "{gender, select, male {He} female {She} other {They}} bought {count, plural, one {# item} other {# items}}",
  "en",
);

console.log(genderMessage.format({ gender: "female", count: 2 }));
// She bought 2 items
```
