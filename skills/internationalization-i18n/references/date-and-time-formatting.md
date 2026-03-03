# Date and Time Formatting

## Date and Time Formatting

### JavaScript (Intl API)

```typescript
// date-formatter.ts
export class DateFormatter {
  constructor(private locale: string) {}

  // Format date
  formatDate(date: Date, options?: Intl.DateTimeFormatOptions): string {
    return new Intl.DateTimeFormat(this.locale, options).format(date);
  }

  // Predefined formats
  short(date: Date): string {
    return this.formatDate(date, {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  }

  long(date: Date): string {
    return this.formatDate(date, {
      year: "numeric",
      month: "long",
      day: "numeric",
      weekday: "long",
    });
  }

  time(date: Date): string {
    return this.formatDate(date, {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  }

  relative(date: Date): string {
    const rtf = new Intl.RelativeTimeFormat(this.locale, { numeric: "auto" });
    const diff = date.getTime() - Date.now();
    const days = Math.round(diff / (1000 * 60 * 60 * 24));

    if (Math.abs(days) < 1) {
      const hours = Math.round(diff / (1000 * 60 * 60));
      return rtf.format(hours, "hour");
    }

    return rtf.format(days, "day");
  }
}

// Usage
const enFormatter = new DateFormatter("en-US");
const esFormatter = new DateFormatter("es-ES");
const jaFormatter = new DateFormatter("ja-JP");

const date = new Date("2024-01-15");

console.log(enFormatter.short(date)); // Jan 15, 2024
console.log(esFormatter.short(date)); // 15 ene 2024
console.log(jaFormatter.short(date)); // 2024年1月15日

console.log(enFormatter.relative(new Date(Date.now() - 86400000))); // yesterday
```

### React-Intl Date Formatting

```typescript
import { FormattedDate, FormattedTime, FormattedRelativeTime } from 'react-intl';

export function DateDisplay() {
  const date = new Date();

  return (
    <div>
      {/* Date */}
      <FormattedDate
        value={date}
        year="numeric"
        month="long"
        day="numeric"
      />

      {/* Time */}
      <FormattedTime value={date} />

      {/* Relative time */}
      <FormattedRelativeTime
        value={-1}
        unit="day"
        updateIntervalInSeconds={60}
      />
    </div>
  );
}
```
