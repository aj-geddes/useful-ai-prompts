---
category: technical-workflows
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-18'
description: Design and implement production-ready FastMCP servers with best practices for async operations, error handling, subprocess execution, and tool integration.
layout: prompt
slug: fastmcp-server-patterns
tags:
- FastMCP
- MCP servers
- Python async
- tool development
- subprocess execution
title: FastMCP Server Development Patterns
version: 2.0.0
prompt: |
  I'll help you build robust FastMCP (Model Context Protocol) servers with production-ready patterns. Let me understand your needs:

  ## YOUR MCP SERVER

  - What functionality does your MCP server provide? (file operations, git commands, database access, API integration)
  - What tools will your server expose to Claude?
  - Will it need subprocess execution? (shell commands, git, etc.)
  - Any state management or persistent storage needs?

  ## EXECUTION ENVIRONMENT

  - What's the deployment target? (Docker, local dev, cloud)
  - What working directory or workspace structure?
  - Any environment variables or configuration needed?
  - Security constraints? (allowed commands, path restrictions)

  ## INTEGRATION REQUIREMENTS

  - What external systems will you interact with? (filesystems, APIs, databases)
  - Any authentication or API keys to manage?
  - Timeout and resource limit requirements?
  - Error handling and logging needs?

  ---

  Based on your answers, I'll provide:

  ## 1. FASTMCP SERVER STRUCTURE

  Complete server implementation with:
  - **Server initialization** with proper configuration
  - **Tool definitions** with clear schemas and descriptions
  - **Async handlers** for all operations
  - **Error handling** with MCP error types
  - **Resource management** for cleanup

  ## 2. SUBPROCESS EXECUTION PATTERNS

  For commands and external processes:
  - **Async subprocess execution** with timeout handling
  - **Stream capture** for stdout/stderr
  - **Exit code handling** and success detection
  - **Environment variable management**
  - **Working directory control**
  - **Timeout and cancellation** support

  Example pattern:
  ```python
  async def run_command(command: str, cwd: str, timeout: int):
      # Safe async subprocess with timeout
      # Error handling and result formatting
      # Clean resource cleanup
  ```

  ## 3. TOOL IMPLEMENTATION

  FastMCP tool patterns for:
  - **Input validation** with Pydantic models
  - **Authorization checks** before execution
  - **Rate limiting** and resource quotas
  - **Progress reporting** for long operations
  - **Structured responses** with consistent format

  ## 4. ERROR HANDLING

  Comprehensive error management:
  - **MCPError types** for different failure modes
  - **Timeout handling** with graceful degradation
  - **Subprocess errors** with detailed context
  - **Validation errors** with helpful messages
  - **Resource exhaustion** handling

  ## 5. SECURITY PATTERNS

  Safe execution practices:
  - **Command sanitization** to prevent injection
  - **Path validation** to prevent traversal
  - **Allowed command whitelist** patterns
  - **Environment isolation**
  - **Resource limits** (memory, CPU, disk)

  ## 6. DOCKER INTEGRATION

  Container deployment:
  - Dockerfile with proper base image
  - Volume mounting for workspace access
  - Environment variable injection
  - Health checks and monitoring
  - Log aggregation setup

  ## 7. TESTING & DEBUGGING

  - Unit test patterns for async tools
  - Integration tests with mock MCP client
  - Error scenario testing
  - Performance benchmarking
  - Logging and debugging strategies

  **Example Deliverables**:
  - Complete FastMCP server with async subprocess tool
  - Error handling for timeouts and failures
  - Docker configuration for deployment
  - Test suite with async test patterns
  - Documentation and usage examples

  Tell me what your MCP server needs to do!
---
