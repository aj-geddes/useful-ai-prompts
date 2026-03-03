# Cypress E2E Testing

## Cypress E2E Testing

```typescript
// cypress/e2e/login.cy.ts
describe("Login Flow", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000/login");
  });

  it("logs in with valid credentials", () => {
    cy.get('input[name="email"]').type("user@example.com");
    cy.get('input[name="password"]').type("password123");
    cy.get('button[type="submit"]').click();

    cy.url().should("include", "/dashboard");
    cy.get("h1").should("contain", "Welcome");
  });

  it("displays error for invalid credentials", () => {
    cy.get('input[name="email"]').type("user@example.com");
    cy.get('input[name="password"]').type("wrongpassword");
    cy.get('button[type="submit"]').click();

    cy.get(".error-message").should("contain", "Invalid credentials");
  });

  it("validates email field", () => {
    cy.get('input[name="email"]').type("invalid-email");
    cy.get('input[name="password"]').type("password123");
    cy.get('button[type="submit"]').click();

    cy.get(".error-message").should("contain", "Invalid email");
  });
});

// cypress/e2e/user-management.cy.ts
describe("User Management", () => {
  beforeEach(() => {
    cy.login("admin@example.com", "password123");
    cy.visit("http://localhost:3000/users");
  });

  it("creates a new user", () => {
    cy.get('button:contains("Add User")').click();

    cy.get('input[name="name"]').type("New User");
    cy.get('input[name="email"]').type("newuser@example.com");
    cy.get('button[type="submit"]').click();

    cy.get(".success-message").should("contain", "User created");
    cy.get("table tbody").should("contain", "New User");
  });

  it("edits an existing user", () => {
    cy.get("table tbody tr").first().contains("button", "Edit").click();

    cy.get('input[name="name"]').clear().type("Updated Name");
    cy.get('button[type="submit"]').click();

    cy.get(".success-message").should("contain", "User updated");
  });

  it("deletes a user with confirmation", () => {
    cy.get("table tbody tr").first().contains("button", "Delete").click();
    cy.get('.modal button:contains("Confirm")').click();

    cy.get(".success-message").should("contain", "User deleted");
  });
});

// cypress/support/commands.ts
Cypress.Commands.add("login", (email: string, password: string) => {
  cy.visit("http://localhost:3000/login");
  cy.get('input[name="email"]').type(email);
  cy.get('input[name="password"]').type(password);
  cy.get('button[type="submit"]').click();
  cy.url().should("include", "/dashboard");
});
```
