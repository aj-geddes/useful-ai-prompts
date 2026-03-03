# Acceptance Criteria Examples

## Acceptance Criteria Examples

```yaml
Story: As a customer, I want to save payment methods so I can checkout faster

Acceptance Criteria:

Scenario 1: Add a new payment method
  Given I'm logged in
  And I'm on the payment settings page
  When I click "Add payment method"
  And I enter valid payment details
  And I click "Save"
  Then the payment method is saved
  And I see a success message
  And the new method appears in my saved list

Scenario 2: Edit existing payment method
  Given I have saved payment methods
  When I click "Edit" on a method
  And I change the expiration date
  And I click "Save"
  Then the changes are saved
  And other fields are unchanged

Scenario 3: Delete a payment method
  Given I have multiple saved payment methods
  When I click "Delete" on a method
  And I confirm the deletion
  Then the method is removed
  And my default method is updated if needed

Scenario 4: Error handling
  Given I enter invalid payment information
  When I click "Save"
  Then I see an error message
  And the method is not saved
  And I'm returned to the form to correct

Scenario 5: Security
  Given the payment form is displayed
  When I view the page source
  Then I don't see full payment numbers (PCI compliance)
  And credit card data is encrypted
  And the connection is HTTPS

---
Non-Functional Requirements:
  - Performance: Form save must complete in <2 seconds
  - Usability: Form must be completable in <3 steps
  - Reliability: 99.9% uptime for payment service
  - Accessibility: WCAG 2.1 AA compliance
  - Security: PCI DSS Level 1 compliance
```
