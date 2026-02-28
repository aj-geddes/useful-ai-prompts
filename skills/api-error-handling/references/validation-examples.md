# Validation Patterns

## Input Validation (Node.js with Zod)

Validate at the boundary — before any business logic runs.

```javascript
import { z } from "zod";

// Define schema with clear error messages
const CreateUserSchema = z.object({
  email:    z.string().email("Invalid email format"),
  name:     z.string().min(1, "Name is required").max(100),
  age:      z.number().int().min(0).max(150).optional(),
  role:     z.enum(["admin", "user", "viewer"]).default("user"),
});

// Validate and throw structured ApiError on failure
function validateInput(schema, data) {
  const result = schema.safeParse(data);
  if (!result.success) {
    const details = result.error.issues.map((issue) => ({
      field:   issue.path.join("."),
      message: issue.message,
      code:    issue.code.toUpperCase(),
    }));
    throw new ApiError("VALIDATION_ERROR", "Validation failed", 422, details);
  }
  return result.data;
}

// Route usage
app.post("/api/users", asyncHandler(async (req, res) => {
  const data = validateInput(CreateUserSchema, req.body);
  const user = await UserService.create(data);
  res.status(201).json({ data: user });
}));
```

Error response clients receive:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "statusCode": 422,
    "details": [
      { "field": "email",  "message": "Invalid email format", "code": "INVALID_STRING" },
      { "field": "name",   "message": "Name is required",     "code": "TOO_SMALL" }
    ]
  }
}
```

## Schema Guards — Detecting Bad API Responses

Validate *incoming* responses from upstream services before trusting them:

```javascript
const ExternalUserSchema = z.object({
  id:    z.string().uuid(),
  email: z.string().email(),
  name:  z.string(),
});

async function fetchExternalUser(userId) {
  const response = await fetch(`https://api.example.com/users/${userId}`);

  if (!response.ok) {
    throw new ApiError("SERVICE_UNAVAILABLE", "Upstream user service failed", 503);
  }

  const raw = await response.json();
  const result = ExternalUserSchema.safeParse(raw);

  if (!result.success) {
    // Log the schema violation for debugging — don't expose to client
    console.error("Upstream schema violation:", result.error.issues, { raw });
    throw new ApiError("INTERNAL_ERROR", "Unexpected response from user service", 500);
  }

  return result.data;
}
```

## Validate Before Expensive Operations

Catch bad inputs before DB queries, file I/O, or API calls:

```javascript
// ✅ Validate ID format before querying
app.get("/api/users/:id", asyncHandler(async (req, res) => {
  const id = req.params.id;

  // Guard: reject obviously invalid IDs before hitting the DB
  if (!/^[0-9a-f]{24}$/.test(id)) {
    throw new ApiError("NOT_FOUND", "User not found", 404);
    // Note: return 404, not 400 — don't reveal ID format details to clients
  }

  const user = await User.findById(id);
  if (!user) throw new ApiError("NOT_FOUND", "User not found", 404);

  res.json({ data: user });
}));
```

## Python Input Validation (Pydantic)

```python
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, Literal

class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str
    age: Optional[int] = None
    role: Literal["admin", "user", "viewer"] = "user"

    @validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        return v.strip()

    @validator("age")
    def age_must_be_valid(cls, v):
        if v is not None and not (0 <= v <= 150):
            raise ValueError("Age must be between 0 and 150")
        return v

# In Flask route:
from flask import request, jsonify
from pydantic import ValidationError

@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = CreateUserRequest(**request.json)
    except ValidationError as e:
        details = [
            {"field": ".".join(str(loc) for loc in err["loc"]),
             "message": err["msg"],
             "code": err["type"].upper()}
            for err in e.errors()
        ]
        raise APIError("VALIDATION_ERROR", "Validation failed", 422, details)

    user = UserService.create(data.dict())
    return jsonify({"data": user}), 201
```

## Common Validation Anti-patterns

```javascript
// ❌ DON'T — validate after the expensive operation
const user = await expensiveDbQuery(req.body.id);
if (!req.body.id) throw new Error("ID required");  // too late

// ❌ DON'T — return 200 with error in body
res.json({ success: false, error: "Invalid email" });  // breaks HTTP semantics

// ❌ DON'T — stop on first error (force client to fix one at a time)
if (!body.email) throw new ApiError(...);
if (!body.name)  throw new ApiError(...);

// ✅ DO — collect all field errors and return them together (see Zod example above)
```
