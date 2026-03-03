# Number and Currency Formatting

## Number and Currency Formatting

```typescript
// number-formatter.ts
export class NumberFormatter {
  constructor(private locale: string) {}

  // Format number
  formatNumber(value: number, options?: Intl.NumberFormatOptions): string {
    return new Intl.NumberFormat(this.locale, options).format(value);
  }

  // Currency
  currency(value: number, currency: string): string {
    return this.formatNumber(value, {
      style: "currency",
      currency,
    });
  }

  // Percentage
  percent(value: number): string {
    return this.formatNumber(value, {
      style: "percent",
      minimumFractionDigits: 0,
      maximumFractionDigits: 2,
    });
  }

  // Decimal
  decimal(value: number, decimals: number = 2): string {
    return this.formatNumber(value, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    });
  }

  // Compact notation (1.2K, 1.5M)
  compact(value: number): string {
    return this.formatNumber(value, {
      notation: "compact",
      compactDisplay: "short",
    });
  }
}

// Usage
const enFormatter = new NumberFormatter("en-US");
const deFormatter = new NumberFormatter("de-DE");
const jaFormatter = new NumberFormatter("ja-JP");

console.log(enFormatter.currency(1234.56, "USD")); // $1,234.56
console.log(deFormatter.currency(1234.56, "EUR")); // 1.234,56 €
console.log(jaFormatter.currency(1234.56, "JPY")); // ¥1,235

console.log(enFormatter.percent(0.1234)); // 12.34%
console.log(enFormatter.compact(1234567)); // 1.2M
```
