# FastMCP Server Development Patterns

## Overview
Comprehensive patterns for building production-ready MCP (Model Context Protocol) servers using the FastMCP framework.

## The Prompt

```
You are an expert MCP server developer using the FastMCP framework. Create a production-ready MCP server following these established patterns:

## Core FastMCP Patterns

### 1. Server Initialization
```python
from fastmcp import FastMCP

# Initialize server with proper metadata
mcp = FastMCP(
    name="your-server-name",
    version="1.0.0",
    description="Brief description of server functionality"
)
```

### 2. Tool Implementation Pattern
```python
@mcp.tool()
async def tool_name(
    parameter: str = Field(description="Parameter description")
) -> str:
    """Tool description for LLM understanding.
    
    Args:
        parameter: Detailed parameter explanation
        
    Returns:
        Structured response with status and data
        
    Raises:
        MCPError: When operation fails
    """
    try:
        # Validate inputs
        if not parameter:
            raise MCPError("Parameter cannot be empty")
            
        # Perform operation
        result = await some_async_operation(parameter)
        
        # Return structured response
        return {
            "status": "success",
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise MCPError(f"Tool failed: {str(e)}")
```

### 3. Resource Implementation Pattern
```python
@mcp.resource("scheme://path/{resource_id}")
async def resource_handler(resource_id: str) -> str:
    """Resource description and usage.
    
    Args:
        resource_id: Identifier for the resource
        
    Returns:
        Resource content as string
    """
    # Validate resource exists
    if not await resource_exists(resource_id):
        raise MCPError(f"Resource {resource_id} not found")
        
    # Return resource content
    return await load_resource_content(resource_id)
```

### 4. Prompt Template Pattern
```python
@mcp.prompt()
async def prompt_template(
    context: str = Field(description="Context for prompt generation")
) -> str:
    """Generate structured prompt for specific use case.
    
    Args:
        context: Context information for prompt customization
        
    Returns:
        Formatted prompt template
    """
    return f"""
# Structured Prompt Template

## Context
{context}

## Instructions
1. Analyze the provided context
2. Generate appropriate response
3. Follow best practices

## Output Format
Provide structured output with:
- Analysis summary
- Recommendations
- Next steps
"""
```

## Security Best Practices

### 1. Input Validation
```python
def validate_path(path: str, base_dir: str = "/workspace") -> str:
    """Validate and normalize file paths."""
    # Resolve path and ensure it's within base directory
    resolved = os.path.abspath(os.path.join(base_dir, path))
    if not resolved.startswith(os.path.abspath(base_dir)):
        raise MCPError("Path traversal attempt detected")
    return resolved

def validate_file_size(file_path: str, max_size: int = 10 * 1024 * 1024) -> None:
    """Validate file size limits."""
    if os.path.getsize(file_path) > max_size:
        raise MCPError(f"File too large (max {max_size} bytes)")
```

### 2. Error Handling
```python
class MCPError(Exception):
    """Custom exception for MCP operations."""
    def __init__(self, message: str, code: str = "GENERAL_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)
```

### 3. Async Command Execution
```python
async def run_command(
    command: str,
    cwd: str = "/workspace",
    timeout: int = 30
) -> dict:
    """Execute shell command safely."""
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            cwd=cwd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "")}
        )
        
        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=timeout
        )
        
        return {
            "command": command,
            "cwd": cwd,
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "returncode": process.returncode,
            "success": process.returncode == 0
        }
    except asyncio.TimeoutError:
        raise MCPError(f"Command timed out after {timeout}s")
    except Exception as e:
        raise MCPError(f"Command execution failed: {str(e)}")
```

## Production Deployment

### 1. Docker Configuration
```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Create non-root user
RUN groupadd -r mcpuser && useradd -r -g mcpuser mcpuser

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application code
COPY . .
RUN chown -R mcpuser:mcpuser /app

# Switch to non-root user
USER mcpuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import fastmcp; print('healthy')"

# Run server
CMD ["python", "-u", "server.py"]
```

### 2. Environment Configuration
```python
import os
from typing import Optional

class Config:
    """Server configuration from environment variables."""
    
    def __init__(self):
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.workspace_dir: str = os.getenv("WORKSPACE_DIR", "/workspace")
        self.max_file_size: int = int(os.getenv("MAX_FILE_SIZE", "10485760"))
        self.command_timeout: int = int(os.getenv("COMMAND_TIMEOUT", "30"))

config = Config()
```

Requirements:
- Use FastMCP framework with proper decorators
- Implement comprehensive error handling
- Follow security best practices
- Include structured logging
- Add proper input validation
- Create production-ready Docker configuration
- Write comprehensive tests
- Document all functions and classes
```

## Key Components

### FastMCP Decorators
- `@mcp.tool()` - Define callable tools
- `@mcp.resource()` - Handle resource requests
- `@mcp.prompt()` - Create prompt templates

### Security Features
- Path traversal protection
- File size validation
- Command execution sandboxing
- Input sanitization

### Production Features
- Docker containerization
- Structured logging
- Environment-based configuration
- Health checks
- Non-root execution

## Benefits
- **Rapid Development**: High-level abstractions
- **Security First**: Built-in validation and sandboxing
- **Production Ready**: Docker, logging, monitoring
- **Type Safety**: Full TypeScript-style type hints
- **Testing Support**: Built-in test utilities

## Tags
`fastmcp` `mcp-server` `python` `async` `production` `docker` `security` `testing`