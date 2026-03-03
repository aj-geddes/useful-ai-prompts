# Cypress Accessibility Testing

## Cypress Accessibility Testing

```javascript
// cypress/e2e/accessibility.cy.js
describe("Accessibility Tests", () => {
  beforeEach(() => {
    cy.visit("/");
    cy.injectAxe();
  });

  it("has no detectable a11y violations on load", () => {
    cy.checkA11y();
  });

  it("navigation is accessible", () => {
    cy.checkA11y("nav");
  });

  it("focuses on first error when form submission fails", () => {
    cy.get("form").within(() => {
      cy.get('[type="submit"]').click();
    });

    cy.focused().should("have.attr", "aria-invalid", "true");
  });

  it("modal has correct focus management", () => {
    cy.get('[data-cy="open-modal"]').click();

    // Focus should be in modal
    cy.get('[role="dialog"]').should("exist");
    cy.focused().parents('[role="dialog"]').should("exist");

    // Close modal with Escape
    cy.get("body").type("{esc}");
    cy.get('[role="dialog"]').should("not.exist");

    // Focus returns to trigger
    cy.get('[data-cy="open-modal"]').should("have.focus");
  });
});
```
