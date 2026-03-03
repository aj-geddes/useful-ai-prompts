# Stryker for JavaScript/TypeScript

## Stryker for JavaScript/TypeScript

```bash
# Install Stryker
npm install --save-dev @stryker-mutator/core @stryker-mutator/jest-runner

# Initialize configuration
npx stryker init

# Run mutation testing
npx stryker run
```

```javascript
// stryker.conf.json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "packageManager": "npm",
  "reporters": ["html", "clear-text", "progress", "dashboard"],
  "testRunner": "jest",
  "jest": {
    "projectType": "custom",
    "configFile": "jest.config.js",
    "enableFindRelatedTests": true
  },
  "coverageAnalysis": "perTest",
  "mutate": [
    "src/**/*.ts",
    "!src/**/*.spec.ts",
    "!src/**/*.test.ts"
  ],
  "thresholds": {
    "high": 80,
    "low": 60,
    "break": 50
  }
}

// Example source code
// src/calculator.ts
export class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }

  subtract(a: number, b: number): number {
    return a - b;
  }

  multiply(a: number, b: number): number {
    return a * b;
  }

  divide(a: number, b: number): number {
    if (b === 0) {
      throw new Error('Division by zero');
    }
    return a / b;
  }

  isPositive(n: number): boolean {
    return n > 0;
  }
}

// ❌ Weak tests - mutations will survive
describe('Calculator - Weak Tests', () => {
  const calc = new Calculator();

  test('add returns a number', () => {
    const result = calc.add(2, 3);
    expect(typeof result).toBe('number');
    // This test won't catch mutations like: return a - b; or return a * b;
  });

  test('divide with non-zero divisor', () => {
    expect(() => calc.divide(10, 2)).not.toThrow();
    // Doesn't verify the actual result!
  });
});

// ✅ Strong tests - will kill mutations
describe('Calculator - Strong Tests', () => {
  const calc = new Calculator();

  describe('add', () => {
    test('adds two positive numbers', () => {
      expect(calc.add(2, 3)).toBe(5);
    });

    test('adds negative numbers', () => {
      expect(calc.add(-2, -3)).toBe(-5);
    });

    test('adds zero', () => {
      expect(calc.add(5, 0)).toBe(5);
      expect(calc.add(0, 5)).toBe(5);
    });
  });

  describe('subtract', () => {
    test('subtracts numbers correctly', () => {
      expect(calc.subtract(5, 3)).toBe(2);
      expect(calc.subtract(3, 5)).toBe(-2);
    });
  });

  describe('multiply', () => {
    test('multiplies numbers', () => {
      expect(calc.multiply(3, 4)).toBe(12);
      expect(calc.multiply(-2, 3)).toBe(-6);
    });

    test('multiply by zero', () => {
      expect(calc.multiply(5, 0)).toBe(0);
    });
  });

  describe('divide', () => {
    test('divides numbers correctly', () => {
      expect(calc.divide(10, 2)).toBe(5);
      expect(calc.divide(7, 2)).toBe(3.5);
    });

    test('throws error on division by zero', () => {
      expect(() => calc.divide(10, 0)).toThrow('Division by zero');
    });
  });

  describe('isPositive', () => {
    test('returns true for positive numbers', () => {
      expect(calc.isPositive(1)).toBe(true);
      expect(calc.isPositive(100)).toBe(true);
    });

    test('returns false for zero and negative', () => {
      expect(calc.isPositive(0)).toBe(false);
      expect(calc.isPositive(-1)).toBe(false);
    });
  });
});
```
