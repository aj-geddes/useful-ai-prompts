# Cypress E2E Tests

## Cypress E2E Tests

```javascript
// cypress/e2e/authentication.cy.js
describe("User Authentication Flow", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("should register a new user account", () => {
    cy.get('[data-cy="signup-button"]').click();
    cy.url().should("include", "/signup");

    // Fill registration form
    const timestamp = Date.now();
    cy.get('[name="email"]').type(`user${timestamp}@example.com`);
    cy.get('[name="password"]').type("SecurePass123!");
    cy.get('[name="confirmPassword"]').type("SecurePass123!");
    cy.get('[name="firstName"]').type("Test");
    cy.get('[name="lastName"]').type("User");

    // Accept terms
    cy.get('[name="acceptTerms"]').check();

    // Submit form
    cy.get('button[type="submit"]').click();

    // Verify success
    cy.url().should("include", "/dashboard");
    cy.get(".welcome-message").should("contain", "Welcome, Test!");

    // Verify email sent (check via API)
    cy.request(`/api/test/emails/${timestamp}@example.com`)
      .its("body")
      .should("have.property", "subject", "Welcome to Our App");
  });

  it("should handle validation errors", () => {
    cy.get('[data-cy="signup-button"]').click();

    // Submit empty form
    cy.get('button[type="submit"]').click();

    // Check for validation errors
    cy.get(".error-message").should("have.length.greaterThan", 0);
    cy.get('[name="email"]').parent().should("contain", "Email is required");

    // Fill invalid email
    cy.get('[name="email"]').type("invalid-email");
    cy.get('[name="password"]').type("weak");
    cy.get('button[type="submit"]').click();

    cy.get('[name="email"]').parent().should("contain", "Invalid email format");
    cy.get('[name="password"]')
      .parent()
      .should("contain", "Password must be at least 8 characters");
  });

  it("should login with valid credentials", () => {
    // Create test user first
    cy.request("POST", "/api/test/users", {
      email: "test@example.com",
      password: "Password123!",
      name: "Test User",
    });

    // Login
    cy.get('[data-cy="login-button"]').click();
    cy.get('[name="email"]').type("test@example.com");
    cy.get('[name="password"]').type("Password123!");
    cy.get('button[type="submit"]').click();

    // Verify login successful
    cy.url().should("include", "/dashboard");
    cy.getCookie("auth_token").should("exist");

    // Verify user menu
    cy.get('[data-cy="user-menu"]').click();
    cy.get(".user-email").should("contain", "test@example.com");
  });

  it("should maintain session across page reloads", () => {
    // Login
    cy.loginViaAPI("test@example.com", "Password123!");
    cy.visit("/dashboard");

    // Verify logged in
    cy.get(".user-menu").should("exist");

    // Reload page
    cy.reload();

    // Still logged in
    cy.get(".user-menu").should("exist");
    cy.getCookie("auth_token").should("exist");
  });

  it("should logout successfully", () => {
    cy.loginViaAPI("test@example.com", "Password123!");
    cy.visit("/dashboard");

    cy.get('[data-cy="user-menu"]').click();
    cy.get('[data-cy="logout-button"]').click();

    cy.url().should("equal", Cypress.config().baseUrl + "/");
    cy.getCookie("auth_token").should("not.exist");
  });
});

// Custom command for login
Cypress.Commands.add("loginViaAPI", (email, password) => {
  cy.request("POST", "/api/auth/login", { email, password }).then(
    (response) => {
      window.localStorage.setItem("auth_token", response.body.token);
    },
  );
});
```
