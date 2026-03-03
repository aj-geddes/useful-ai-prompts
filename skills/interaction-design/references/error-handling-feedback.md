# Error Handling & Feedback

## Error Handling & Feedback

```yaml
Error State Design:

Primary Error Message:
  "Payment declined"  (clear, non-technical)

Secondary Explanation:
  "Your card was declined by the bank. This might be due to
  insufficient funds, security concerns, or an expired card."

Recovery Action:
  [ Retry Payment ] [ Use Different Card ] [ Contact Support ]

Form Field Errors:
  - Highlight field with error color (red)
  - Show error icon
  - Place error message near field
  - Show error on blur, not on keystroke

Form Validation:
  - Real-time validation for good UX
  - Server-side validation for security
  - Show success state after valid input
  - Clear error when corrected

---

Success States:

Confirmation Message:
  "Payment successful!"
  Duration: 2-3 seconds
  Action: Auto-dismiss or click to close

Next Step:
  - Order confirmation email sent
  - What happens next?
  - Related actions

Visual Feedback:
  - Check mark animation
  - Subtle celebration animation
  - Sound (optional, if enabled)
```
