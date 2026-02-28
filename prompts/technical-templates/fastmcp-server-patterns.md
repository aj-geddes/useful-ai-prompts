# FastMCP Server Development Patterns

## Metadata

- **ID**: `fastmcp-server-patterns`
- **Version**: 1.1.0
- **Category**: Technical / MCP
- **Tags**: fastmcp, mcp-server, server-development, api-integration, automation, model-context-protocol
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+ (MCP-enabled)
- **Created**: 2024-01-15
- **Updated**: 2025-01-01

## Overview

Provides comprehensive patterns and production-ready templates for developing FastMCP servers with proper security controls, async concurrency, and integration capabilities. Covers tool registration, resource handling, prompt templates, and containerized deployment configurations. Enables rapid development of secure, scalable MCP server implementations.

## When to Use

**Ideal Scenarios:**

- Developing new FastMCP server implementations for Claude or other MCP clients
- Creating tool, resource, and prompt integrations for the Model Context Protocol
- Building containerized MCP deployments with security controls and health monitoring
- Implementing async patterns for scalable, concurrent MCP operations
- Integrating external APIs and services through MCP tool interfaces

**Anti-patterns (when not to use):**

- Client-side MCP integration (connecting to existing servers)
- Non-MCP API development using standard REST/GraphQL patterns
- Simple scripting without server persistence requirements
- Prototyping without production security requirements

---

## Prompt

```xml
<role>
You are an MCP Platform Engineer with deep expertise in FastMCP server development, Python async patterns, and secure containerized deployments. You build production-grade MCP servers with comprehensive error handling, input validation, structured logging, and operational observability. Your implementations follow security best practices and handle edge cases gracefully.
</role>

<context>
The Model Context Protocol (MCP) enables AI assistants to interact with external tools, resources, and data sources through standardized interfaces. FastMCP provides a Python framework for rapid server development with decorator-based tool registration. Production deployments require security hardening, input validation, timeout management, and containerized execution.
</context>

<input_handling>
Required inputs:
- Application context and intended use case for the MCP server
- Toolset definition (categories and specific operations to provision)
- Target API specifications (OpenAPI schemas, GraphQL endpoints, or interface contracts)

Infer if not provided:
- Tool operation type (default: stateless async operations)
- Security requirements (default: standard input validation, path restrictions)
- Deployment target (default: Docker container with stdio transport)
</input_handling>

<task>
Scaffold a production-ready FastMCP server implementation.

1. Initialize server with proper metadata, versioning, and configuration management
2. Design tool registration with typed inputs (Pydantic), validation rules, and structured response formats
3. Create resource endpoints with existence checking, access control, and error handling
4. Build prompt templates with dynamic context injection and variable substitution
5. Implement security controls including path validation, size limits, timeout constraints, and command sandboxing
6. Configure containerized deployment with health checks, non-root execution, and resource limits
7. Document API interfaces, configuration options, and operational parameters
</task>

<output_specification>
Format: Python implementation with Dockerfile and configuration files
Length: 1000-2000 words with complete code examples
Structure:
- Server initialization and configuration
- Tool registration patterns with validation
- Resource endpoint implementation
- Security control implementation
- Dockerfile with production hardening
- Usage documentation and examples
</output_specification>

<quality_criteria>
Excellent outputs will:
- Use native async operations throughout for scalable concurrency
- Implement strict input validation with Pydantic schemas and custom validators
- Include timeout constraints and structured cancellation for all external calls
- Configure non-root Docker execution with health probes and resource limits
- Provide comprehensive error handling with structured error responses

Avoid:
- Synchronous blocking operations in tool implementations
- Missing input validation or path normalization allowing traversal attacks
- Embedding secrets, credentials, or configuration in code
- Over-permissive container configurations or running as root
</quality_criteria>

<constraints>
- Follow FastMCP best practices and conventions
- Use type hints throughout for documentation and validation
- Implement graceful degradation for external service failures
- Consider MCP protocol version compatibility
</constraints>
```

---

## Example Usage

### Input

We need a FastMCP server for secure file system operations on a mounted workspace directory. Tools needed: read_file, write_file, list_directory, search_files. The server will be deployed as a Docker container with /workspace mounted as a volume. Requirements: path traversal prevention, file size limits (10MB), non-root execution, and structured JSON responses.

### Output

**Server Initialization**

```python
"""
Secure Filesystem MCP Server
Provides controlled file operations within mounted workspace
"""
from fastmcp import FastMCP
from pydantic import Field, field_validator
import os
import aiofiles
import asyncio
from pathlib import Path

# Server configuration
WORKSPACE_BASE = os.environ.get("WORKSPACE_PATH", "/workspace")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

mcp = FastMCP(
    name="filesystem-mcp",
    version="1.0.0",
    description="Secure file system operations for mounted workspace"
)
```

**Security Utilities**

```python
class MCPSecurityError(Exception):
    """Security violation in MCP operation"""
    pass

def validate_path(path: str, base_dir: str = WORKSPACE_BASE) -> Path:
    """
    Validate and normalize path, preventing traversal attacks.
    Returns resolved absolute path within base directory.
    """
    # Normalize and resolve the path
    base = Path(base_dir).resolve()
    requested = (base / path).resolve()

    # Verify path is within base directory
    if not str(requested).startswith(str(base)):
        raise MCPSecurityError(
            f"Path traversal violation: {path} escapes workspace"
        )

    return requested

def validate_file_size(path: Path, max_size: int = MAX_FILE_SIZE) -> None:
    """Validate file size is within limits."""
    if path.exists() and path.stat().st_size > max_size:
        raise MCPSecurityError(
            f"File exceeds size limit: {path.stat().st_size} > {max_size}"
        )
```

**Tool Registration with Validation**

```python
@mcp.tool()
async def read_file(
    path: str = Field(
        description="File path relative to workspace root",
        examples=["src/main.py", "config/settings.json"]
    )
) -> dict:
    """
    Read file contents from workspace.
    Returns file content with metadata.
    """
    try:
        validated_path = validate_path(path)

        if not validated_path.exists():
            return {
                "status": "error",
                "error": f"File not found: {path}"
            }

        if not validated_path.is_file():
            return {
                "status": "error",
                "error": f"Not a file: {path}"
            }

        validate_file_size(validated_path)

        async with aiofiles.open(validated_path, 'r') as f:
            content = await asyncio.wait_for(f.read(), timeout=30.0)

        return {
            "status": "success",
            "path": str(validated_path.relative_to(WORKSPACE_BASE)),
            "content": content,
            "size": len(content)
        }

    except MCPSecurityError as e:
        return {"status": "error", "error": str(e), "security_violation": True}
    except asyncio.TimeoutError:
        return {"status": "error", "error": "Read operation timed out"}
    except Exception as e:
        return {"status": "error", "error": f"Read failed: {str(e)}"}


@mcp.tool()
async def write_file(
    path: str = Field(description="File path relative to workspace root"),
    content: str = Field(description="Content to write to file")
) -> dict:
    """
    Write content to file in workspace.
    Creates parent directories if needed.
    """
    try:
        if len(content.encode('utf-8')) > MAX_FILE_SIZE:
            return {
                "status": "error",
                "error": f"Content exceeds size limit: {MAX_FILE_SIZE} bytes"
            }

        validated_path = validate_path(path)

        # Create parent directories
        validated_path.parent.mkdir(parents=True, exist_ok=True)

        async with aiofiles.open(validated_path, 'w') as f:
            await asyncio.wait_for(f.write(content), timeout=30.0)

        return {
            "status": "success",
            "path": str(validated_path.relative_to(WORKSPACE_BASE)),
            "bytes_written": len(content.encode('utf-8'))
        }

    except MCPSecurityError as e:
        return {"status": "error", "error": str(e), "security_violation": True}
    except Exception as e:
        return {"status": "error", "error": f"Write failed: {str(e)}"}
```

**Production Dockerfile**

```dockerfile
# syntax=docker/dockerfile:1.4
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Security: Create non-root user
RUN groupadd -r -g 1000 mcpuser && \
    useradd -r -u 1000 -g mcpuser mcpuser

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application
COPY --chown=mcpuser:mcpuser . .

# Security: Switch to non-root user
USER mcpuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import fastmcp; print('healthy')" || exit 1

# Run with unbuffered output for logging
CMD ["python", "-u", "server.py"]
```

**Container Execution**

```bash
# Run with workspace mount
docker run -d \
  --name filesystem-mcp \
  --user 1000:1000 \
  --read-only \
  --tmpfs /tmp:size=100M \
  -v /path/to/workspace:/workspace:rw \
  --memory=512m \
  --cpus=0.5 \
  filesystem-mcp:latest
```

---

## Related Prompts

- [MCP Integration Framework](./mcp-enabler-comprehensive.md) - Comprehensive MCP enablement
- [API Design Expert](../technical-workflows/api-design-expert.md) - API design patterns
- [Docker Production Patterns](./docker-production-patterns.md) - Container security
