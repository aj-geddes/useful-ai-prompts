# Function Documentation

## Function Documentation

```javascript
/**
 * Calculates the total price including tax and discount.
 *
 * @param {number} basePrice - The base price before tax and discount
 * @param {number} taxRate - Tax rate as a decimal (e.g., 0.08 for 8%)
 * @param {number} [discount=0] - Optional discount amount
 * @returns {number} The final price after tax and discount
 * @throws {Error} If basePrice or taxRate is negative
 *
 * @example
 * const price = calculateTotalPrice(100, 0.08, 10);
 * console.log(price); // 98
 *
 * @example
 * // Without discount
 * const price = calculateTotalPrice(100, 0.08);
 * console.log(price); // 108
 */
function calculateTotalPrice(basePrice, taxRate, discount = 0) {
  if (basePrice < 0 || taxRate < 0) {
    throw new Error("Price and tax rate must be non-negative");
  }
  return basePrice * (1 + taxRate) - discount;
}

/**
 * Fetches user data from the API with retry logic.
 *
 * @async
 * @param {string} userId - The unique identifier for the user
 * @param {Object} [options={}] - Additional options
 * @param {number} [options.maxRetries=3] - Maximum number of retry attempts
 * @param {number} [options.timeout=5000] - Request timeout in milliseconds
 * @returns {Promise<User>} Promise resolving to user object
 * @throws {Error} If user not found after all retries
 *
 * @typedef {Object} User
 * @property {string} id - User ID
 * @property {string} name - User's full name
 * @property {string} email - User's email address
 * @property {string[]} roles - Array of user roles
 *
 * @example
 * try {
 *   const user = await fetchUser('user123', { maxRetries: 5 });
 *   console.log(user.name);
 * } catch (error) {
 *   console.error('Failed to fetch user:', error);
 * }
 */
async function fetchUser(userId, options = {}) {
  const { maxRetries = 3, timeout = 5000 } = options;
  // Implementation...
}
```
