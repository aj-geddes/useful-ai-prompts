# Class Documentation

## Class Documentation

```javascript
/**
 * Represents a shopping cart in an e-commerce application.
 * Manages items, calculates totals, and handles checkout operations.
 *
 * @class
 * @example
 * const cart = new ShoppingCart('user123');
 * cart.addItem({ id: 'prod1', name: 'Laptop', price: 999.99 }, 1);
 * console.log(cart.getTotal()); // 999.99
 */
class ShoppingCart {
  /**
   * Creates a new shopping cart instance.
   *
   * @constructor
   * @param {string} userId - The ID of the user who owns this cart
   * @param {Object} [options={}] - Configuration options
   * @param {string} [options.currency='USD'] - Currency code
   * @param {number} [options.taxRate=0] - Tax rate as decimal
   */
  constructor(userId, options = {}) {
    this.userId = userId;
    this.items = [];
    this.currency = options.currency || "USD";
    this.taxRate = options.taxRate || 0;
  }

  /**
   * Adds an item to the cart or increases quantity if already present.
   *
   * @param {Product} product - The product to add
   * @param {number} quantity - Quantity to add (must be positive integer)
   * @returns {CartItem} The added or updated cart item
   * @throws {Error} If quantity is not a positive integer
   *
   * @typedef {Object} Product
   * @property {string} id - Product ID
   * @property {string} name - Product name
   * @property {number} price - Product price
   *
   * @typedef {Object} CartItem
   * @property {Product} product - Product details
   * @property {number} quantity - Item quantity
   * @property {number} subtotal - Item subtotal (price * quantity)
   */
  addItem(product, quantity) {
    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error("Quantity must be a positive integer");
    }

    const existingItem = this.items.find(
      (item) => item.product.id === product.id,
    );

    if (existingItem) {
      existingItem.quantity += quantity;
      existingItem.subtotal =
        existingItem.product.price * existingItem.quantity;
      return existingItem;
    }

    const newItem = {
      product,
      quantity,
      subtotal: product.price * quantity,
    };
    this.items.push(newItem);
    return newItem;
  }

  /**
   * Calculates the total price including tax.
   *
   * @returns {number} Total price with tax
   */
  getTotal() {
    const subtotal = this.items.reduce((sum, item) => sum + item.subtotal, 0);
    return subtotal * (1 + this.taxRate);
  }

  /**
   * Removes all items from the cart.
   *
   * @returns {void}
   */
  clear() {
    this.items = [];
  }
}
```
