# Cypress Visual Testing

## Cypress Visual Testing

```javascript
// cypress/e2e/visual.cy.js
describe("Visual Regression Tests", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("homepage visual snapshot", () => {
    cy.viewport(1280, 720);
    cy.matchImageSnapshot("homepage-desktop");
  });

  it("mobile navigation menu", () => {
    cy.viewport("iphone-x");
    cy.get('[data-cy="menu-toggle"]').click();
    cy.get(".mobile-menu").should("be.visible");
    cy.matchImageSnapshot("mobile-menu-open");
  });

  it("form validation errors", () => {
    cy.get("form").within(() => {
      cy.get('[type="email"]').type("invalid-email");
      cy.get('[type="submit"]').click();
    });

    cy.get(".error-message").should("be.visible");
    cy.matchImageSnapshot("form-validation-errors");
  });

  it("loading state", () => {
    cy.intercept("GET", "/api/products", (req) => {
      req.reply((res) => {
        res.delay(1000); // Simulate slow response
        res.send();
      });
    });

    cy.visit("/products");
    cy.matchImageSnapshot("loading-skeleton");
  });

  it("empty state", () => {
    cy.intercept("GET", "/api/cart", { items: [] });
    cy.visit("/cart");
    cy.matchImageSnapshot("cart-empty-state");
  });
});

// cypress.config.js
const { defineConfig } = require("cypress");
const {
  addMatchImageSnapshotPlugin,
} = require("cypress-image-snapshot/plugin");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      addMatchImageSnapshotPlugin(on, config);
    },
  },
});

// cypress/support/commands.js
import { addMatchImageSnapshotCommand } from "cypress-image-snapshot/command";

addMatchImageSnapshotCommand({
  failureThreshold: 0.03, // Allow 3% difference
  failureThresholdType: "percent",
  customDiffConfig: { threshold: 0.1 },
  capture: "viewport",
});
```
