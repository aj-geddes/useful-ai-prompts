# Error Codes & Response Format

## ERROR_CODES Map

```javascript
const ERROR_CODES = {
  VALIDATION_ERROR:    { status: 422, message: "Validation failed" },
  NOT_FOUND:           { status: 404, message: "Resource not found" },
  UNAUTHORIZED:        { status: 401, message: "Authentication required" },
  FORBIDDEN:           { status: 403, message: "Access denied" },
  CONFLICT:            { status: 409, message: "Resource conflict" },
  RATE_LIMITED:        { status: 429, message: "Too many requests" },
  INTERNAL_ERROR:      { status: 500, message: "Internal server error" },
  SERVICE_UNAVAILABLE: { status: 503, message: "Service unavailable" },
};
```

## Global Error Middleware — Node.js (Express)

```javascript
// Error response formatter
function formatErrorResponse(error, requestId, traceId) {
  return {
    error: {
      code: error.code,
      message: error.message,
      statusCode: error.statusCode,
      requestId,
      timestamp: error.timestamp,
      ...(error.details && { details: error.details }),
      traceId,
    },
  };
}

// Error logger (severity by status code)
function logError(error, context) {
  const logData = {
    timestamp: new Date().toISOString(),
    errorCode: error.code,
    errorMessage: error.message,
    statusCode: error.statusCode,
    stack: error.stack,
    context,
  };

  if (error.statusCode >= 500) {
    console.error("[ERROR]", JSON.stringify(logData));
    trackError(logData); // send to Sentry, etc.
  } else if (error.statusCode >= 400) {
    console.warn("[WARN]", JSON.stringify(logData));
  }
}

// Global error handler middleware
app.use((err, req, res, next) => {
  const requestId = req.id || `req_${Date.now()}`;
  const traceId = req.traceId;

  logError(err, {
    requestId, traceId,
    method: req.method, path: req.path,
    query: req.query, userId: req.user?.id,
  });

  if (err instanceof ApiError) {
    return res.status(err.statusCode).json(formatErrorResponse(err, requestId, traceId));
  }

  if (err instanceof SyntaxError && "body" in err) {
    const e = new ApiError("VALIDATION_ERROR", "Invalid JSON", 400);
    return res.status(400).json(formatErrorResponse(e, requestId, traceId));
  }

  if (err.name === "ValidationError") {
    const details = Object.keys(err.errors).map((field) => ({
      field, message: err.errors[field].message, code: "VALIDATION_FAILED",
    }));
    const e = new ApiError("VALIDATION_ERROR", "Validation failed", 422, details);
    return res.status(422).json(formatErrorResponse(e, requestId, traceId));
  }

  if (err.name === "CastError") {
    const e = new ApiError("NOT_FOUND", "Invalid resource ID", 404);
    return res.status(404).json(formatErrorResponse(e, requestId, traceId));
  }

  const e = new ApiError("INTERNAL_ERROR", "An unexpected error occurred", 500);
  res.status(500).json(formatErrorResponse(e, requestId, traceId));
});

// Async route wrapper — eliminates try/catch boilerplate
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

// Catch unhandled promise rejections
process.on("unhandledRejection", (reason) => {
  console.error("Unhandled Rejection:", reason);
  trackError({ type: "unhandledRejection", reason });
});
```

## Global Error Handlers — Python (Flask)

```python
from flask import Flask, jsonify, request
from datetime import datetime
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

class APIError(Exception):
    def __init__(self, code, message, status_code=500, details=None):
        super().__init__()
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or []
        self.timestamp = datetime.utcnow().isoformat()

ERROR_CODES = {
    'VALIDATION_ERROR': 422,
    'NOT_FOUND': 404,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'CONFLICT': 409,
    'INTERNAL_ERROR': 500,
}

def format_error(error, request_id, trace_id):
    return {
        'error': {
            'code': error.code,
            'message': error.message,
            'statusCode': error.status_code,
            'requestId': request_id,
            'timestamp': error.timestamp,
            'traceId': trace_id,
            'details': error.details or None,
        }
    }

def log_error(error, context):
    entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'code': error.code,
        'message': error.message,
        'status': error.status_code,
        'context': context,
    }
    if error.status_code >= 500:
        logger.error(entry)
    elif error.status_code >= 400:
        logger.warning(entry)

@app.errorhandler(APIError)
def handle_api_error(error):
    request_id = request.headers.get('X-Request-ID', f'req_{int(datetime.utcnow().timestamp())}')
    trace_id = request.headers.get('X-Trace-ID')
    log_error(error, {'request_id': request_id, 'method': request.method, 'path': request.path})
    return jsonify(format_error(error, request_id, trace_id)), error.status_code

@app.errorhandler(400)
def handle_bad_request(error):
    e = APIError('VALIDATION_ERROR', 'Invalid request', 400)
    return jsonify(format_error(e, f'req_{int(datetime.utcnow().timestamp())}', None)), 400

@app.errorhandler(404)
def handle_not_found(error):
    e = APIError('NOT_FOUND', 'Resource not found', 404)
    return jsonify(format_error(e, f'req_{int(datetime.utcnow().timestamp())}', None)), 404

@app.errorhandler(500)
def handle_internal_error(error):
    logger.error(f'Internal error: {error}', exc_info=True)
    e = APIError('INTERNAL_ERROR', 'Internal server error', 500)
    return jsonify(format_error(e, f'req_{int(datetime.utcnow().timestamp())}', None)), 500
```
