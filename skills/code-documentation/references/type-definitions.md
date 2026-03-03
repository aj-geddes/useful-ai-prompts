# Type Definitions

## Type Definitions

```typescript
/**
 * API response wrapper for all endpoints
 *
 * @template T - The type of data in the response
 * @typedef {Object} ApiResponse
 * @property {boolean} success - Whether the request succeeded
 * @property {T} [data] - Response data (present on success)
 * @property {string} [error] - Error message (present on failure)
 * @property {Object} [metadata] - Additional response metadata
 * @property {number} metadata.timestamp - Response timestamp
 * @property {string} metadata.requestId - Unique request ID
 */

/**
 * User authentication credentials
 *
 * @typedef {Object} Credentials
 * @property {string} email - User email address
 * @property {string} password - User password (min 8 characters)
 */

/**
 * Pagination parameters for list endpoints
 *
 * @typedef {Object} PaginationParams
 * @property {number} [page=1] - Page number (1-indexed)
 * @property {number} [limit=20] - Items per page (max 100)
 * @property {string} [sortBy='createdAt'] - Field to sort by
 * @property {'asc'|'desc'} [order='desc'] - Sort order
 */
```
