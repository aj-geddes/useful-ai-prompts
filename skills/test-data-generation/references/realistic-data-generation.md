# Realistic Data Generation

## Realistic Data Generation

```javascript
// tests/helpers/dataGenerator.js
const { faker } = require("@faker-js/faker");

class DataGenerator {
  static generateCreditCard() {
    return {
      number: faker.finance.creditCardNumber("#### #### #### ####"),
      cvv: faker.finance.creditCardCVV(),
      expiry: faker.date.future().toISOString().slice(0, 7), // YYYY-MM
      type: faker.helpers.arrayElement(["visa", "mastercard", "amex"]),
    };
  }

  static generateAddress() {
    return {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state(),
      zip: faker.location.zipCode(),
      country: faker.location.country(),
      coordinates: {
        lat: parseFloat(faker.location.latitude()),
        lng: parseFloat(faker.location.longitude()),
      },
    };
  }

  static generateDateRange(days = 30) {
    const endDate = new Date();
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days);
    return { startDate, endDate };
  }

  static generateTimeSeries(count, interval = "day") {
    const data = [];
    const now = new Date();

    for (let i = count - 1; i >= 0; i--) {
      const date = new Date(now);
      if (interval === "day") date.setDate(date.getDate() - i);
      if (interval === "hour") date.setHours(date.getHours() - i);

      data.push({
        timestamp: date,
        value: faker.number.float({ min: 0, max: 100, precision: 0.01 }),
      });
    }

    return data;
  }

  static generateRealisticEmail(firstName, lastName, domain = "example.com") {
    const patterns = [
      `${firstName}.${lastName}`,
      `${firstName}${lastName}`,
      `${firstName.charAt(0)}${lastName}`,
      `${firstName}_${lastName}`,
    ];

    const pattern = faker.helpers.arrayElement(patterns);
    return `${pattern.toLowerCase()}@${domain}`;
  }
}

module.exports = { DataGenerator };
```
