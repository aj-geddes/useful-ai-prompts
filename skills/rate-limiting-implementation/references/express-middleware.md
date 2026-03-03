# Express Middleware

## Express Middleware

```typescript
import express from "express";
import { RedisRateLimiter } from "./rate-limiter";

interface RateLimitMiddlewareOptions {
  points: number;
  duration: number;
  blockDuration?: number;
  keyGenerator?: (req: express.Request) => string;
  handler?: (req: express.Request, res: express.Response) => void;
  skipSuccessfulRequests?: boolean;
  skipFailedRequests?: boolean;
}

function createRateLimitMiddleware(
  limiter: RedisRateLimiter,
  options: RateLimitMiddlewareOptions,
) {
  const keyGenerator = options.keyGenerator || ((req) => req.ip || "unknown");

  return async (
    req: express.Request,
    res: express.Response,
    next: express.NextFunction,
  ) => {
    const key = keyGenerator(req);

    try {
      const result = await limiter.consume(key, {
        points: options.points,
        duration: options.duration,
        blockDuration: options.blockDuration,
      });

      // Set rate limit headers
      res.setHeader("X-RateLimit-Limit", options.points);
      res.setHeader("X-RateLimit-Remaining", result.remaining);
      res.setHeader(
        "X-RateLimit-Reset",
        new Date(result.resetTime).toISOString(),
      );

      if (!result.allowed) {
        res.setHeader("Retry-After", result.retryAfter!);

        if (options.handler) {
          return options.handler(req, res);
        }

        return res.status(429).json({
          error: "Too Many Requests",
          message: `Rate limit exceeded. Retry after ${result.retryAfter} seconds.`,
          retryAfter: result.retryAfter,
        });
      }

      // Handle conditional consumption
      if (options.skipSuccessfulRequests || options.skipFailedRequests) {
        const originalSend = res.send;
        res.send = function (data: any) {
          const statusCode = res.statusCode;

          if (
            (options.skipSuccessfulRequests && statusCode < 400) ||
            (options.skipFailedRequests && statusCode >= 400)
          ) {
            // Refund the consumed point
            limiter.consume(
              key,
              {
                points: options.points,
                duration: options.duration,
              },
              -1,
            );
          }

          return originalSend.call(this, data);
        };
      }

      next();
    } catch (error) {
      console.error("Rate limiting error:", error);
      // Fail open - allow request if rate limiter fails
      next();
    }
  };
}

// Usage
const app = express();
const redis = new Redis();
const limiter = new RedisRateLimiter(redis);

// Global rate limit
app.use(
  createRateLimitMiddleware(limiter, {
    points: 100,
    duration: 60,
    blockDuration: 300,
  }),
);

// API-specific rate limit
app.use(
  "/api/search",
  createRateLimitMiddleware(limiter, {
    points: 10,
    duration: 60,
    keyGenerator: (req) => `search:${req.ip}`,
    skipSuccessfulRequests: true,
  }),
);

// User-specific rate limit
app.use(
  "/api/user",
  createRateLimitMiddleware(limiter, {
    points: 1000,
    duration: 3600,
    keyGenerator: (req) => `user:${req.user?.id || req.ip}`,
  }),
);
```
