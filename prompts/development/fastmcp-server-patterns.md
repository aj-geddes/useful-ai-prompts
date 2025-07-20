## Solicit User Input for \[precise FastMCP server use case and context]

To initiate scaffolding of a high-integrity FastMCP server instance, provide the following inputs:

- **Application Context**: Clearly articulate the intended use case, including domain-specific workflows or automation tasks the server is expected to support.
- **Toolset Definition**: Enumerate the categories of tools to be provisioned (e.g., semantic enrichment, system integration interfaces, orchestration triggers). Indicate whether each tool is stateless, stateful, or event-driven.
- **Target API Corpus**: Supply the location(s) of technical specifications (e.g., OpenAPI, GraphQL schemas, or human-authored interface contracts) for any upstream or downstream APIs that the server will bind to.

These directives will guide the precise formulation of tool declarations, input validation schemas, execution contexts, and prompt scaffolds in alignment with the system's operational semantics.

---

## Foundational Requirements

- **Contractual Conformity**: The server must strictly comply with the FastMCP platform’s declarative constructs for registering tools, resources, and prompt interfaces.
- **Security Formalism**: All externally-facing surfaces must incorporate path normalization, input sanitization, and bounded execution zones to mitigate attack surfaces.
- **Concurrency Semantics**: All tool operations must be natively asynchronous, facilitating scalable event loop concurrency for I/O-bound routines.
- **Container Integrity**: Deployment targets must use minimal, reproducible, and non-root Docker images instrumented with liveness and readiness probes.
- **Error Taxonomy**: Use canonical fault classes (e.g., `MCPError`) with metadata to facilitate structured telemetry, debugging, and user-facing diagnostics.
- **Environmental Configuration Discipline**: Externalize configuration parameters through environment variables, applying defensive defaults to ensure fault tolerance and testability.

---

## Engineering Patterns for Server Composition

### **1. Server Initialization Contract**

```python
from fastmcp import FastMCP

mcp = FastMCP(
    name="your-server-name",
    version="1.0.0",
    description="Concise statement of system purpose and functional boundary"
)
```

### **2. Tool Registration Paradigm**

```python
@mcp.tool()
async def tool_name(parameter: str = Field(description="Input specification")) -> str:
    try:
        if not parameter:
            raise MCPError("Missing required parameter")

        result = await some_async_operation(parameter)

        return {
            "status": "success",
            "result": result,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise MCPError(f"Execution failure: {str(e)}")
```

### **3. Resource Endpoint Schema**

```python
@mcp.resource("scheme://path/{resource_id}")
async def resource_handler(resource_id: str) -> str:
    if not await resource_exists(resource_id):
        raise MCPError(f"Resource {resource_id} not found")

    return await load_resource_content(resource_id)
```

### **4. Prompt Construction Scaffold**

```python
@mcp.prompt()
async def prompt_template(context: str = Field(description="Dynamic payload for contextualization")) -> str:
    return f"""
# Prompt Blueprint

## Context
{context}

## Directives
1. Interpret the contextual input
2. Derive operational intent
3. Respond using canonical structure

## Output Schema
- Summary of key insights
- Suggested course of action
- Follow-up queries if applicable
"""
```

---

## Feature Extensions (New)

- **Type Enforcement Layer**: All tool inputs must implement Pydantic-backed schema definitions to facilitate runtime introspection and linting.
- **Async Fault Isolation**: All asynchronous boundaries must be surrounded by timeout constraints and structured cancellation logic.
- **Prompt Dynamism**: Prompt generation should accommodate runtime context fusion, memory references, or user-injected modifiers.

---

## Secure Execution Architecture

### **Path and Size Validation**

```python
def validate_path(path: str, base_dir: str = "/workspace") -> str:
    resolved = os.path.abspath(os.path.join(base_dir, path))
    if not resolved.startswith(os.path.abspath(base_dir)):
        raise MCPError("Path traversal violation")
    return resolved

def validate_file_size(file_path: str, max_size: int = 10 * 1024 * 1024) -> None:
    if os.path.getsize(file_path) > max_size:
        raise MCPError(f"File size exceeds permitted limit of {max_size} bytes")
```

### **Error Formalization**

```python
class MCPError(Exception):
    def __init__(self, message: str, code: str = "GENERAL_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)
```

### **Command Execution Sandbox**

```python
async def run_command(command: str, cwd: str = "/workspace", timeout: int = 30) -> dict:
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            cwd=cwd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "")}
        )

        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)

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
        raise MCPError(f"Subprocess execution error: {str(e)}")
```

---

## Production Deployment Pipeline

### **Container Blueprint**

```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN groupadd -r mcpuser && useradd -r -g mcpuser mcpuser
WORKDIR /app

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .
RUN chown -R mcpuser:mcpuser /app
USER mcpuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import fastmcp; print('healthy')"

CMD ["python", "-u", "server.py"]
```

### **Runtime Configuration Schema**

```python
class Config:
    def __init__(self):
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.workspace_dir = os.getenv("WORKSPACE_DIR", "/workspace")
        self.max_file_size = int(os.getenv("MAX_FILE_SIZE", "10485760"))
        self.command_timeout = int(os.getenv("COMMAND_TIMEOUT", "30"))

config = Config()
```

---

## Reference Documentation

The following authoritative sources should guide development and runtime behavior:

- [FastMCP Python SDK Reference](https://github.com/fastmcp/fastmcp-sdk-python)
- [FastMCP Developer Guide](https://docs.fastmcp.dev/guide/server-development)
- [FastMCP Prompt Specification](https://docs.fastmcp.dev/specs/prompts)
- [FastMCP Tool and Resource Patterns](https://docs.fastmcp.dev/specs/tools-resources)
- [FastMCP Containerization Best Practices](https://docs.fastmcp.dev/deployment/docker)

These resources should be ingested into the operational context by LLMs supporting autonomous configuration and validation.

---

## Project Deliverables

### **Artifacts**

- `fastmcp-server.md`: Architecture and deployment instructions

### **Configuration Interfaces**

- `server.py`: Entrypoint logic for FastMCP service lifecycle
- `mcp-config.yaml`: Runtime schema for operational parameters

### **Containerization Manifests**

- `Dockerfile`: Hardened container declaration
- `requirements.txt`: Version-locked dependency list

---

## Evaluation Criteria

- ✅ FastMCP initialization completes with all metadata validated
- ✅ Tool definitions are typed, documented, and schema-enforced
- ✅ All inputs are constrained and validated in local execution contexts
- ✅ Timeout and error boundaries are consistently implemented
- ✅ Docker image operates in non-root, health-verified context
- ✅ Runtime environment is fully configurable via typed schema

---

## Quality Standards

- **Layered Security Enforcement**: Defense-in-depth model applied to all ingress points
- **Telemetry Rigor**: All exceptions and anomalies must be logged using structured semantics
- **Deterministic Build Workflow**: CI/CD processes must produce reproducible binaries and state artifacts
- **Fault Resilience**: Tool failures should degrade predictably with full traceability
- **Documentation Fidelity**: All exposed classes and functions must carry doctrinal docstrings for introspection and linting
