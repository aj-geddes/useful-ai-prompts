---
category: technical-workflows
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-18'
description: 'Generate custom MCP (Model Context Protocol) server configurations for Claude Desktop with Docker or native execution, including workspace mounting, environment variables, and security settings.'
layout: prompt
slug: claude-mcp-example
tags:
- MCP
- Claude Desktop
- Docker
- Configuration
- Model Context Protocol
title: Claude Desktop MCP Configuration Generator
version: 2.0.0
prompt: |
  I'll help you create a custom MCP server configuration for Claude Desktop. Let me understand your setup:

  ## YOUR ENVIRONMENT

  - What operating system are you using? (Windows, macOS, Linux)
  - What's your username/home directory path?
  - Do you prefer Docker-based or native MCP servers?
  - Any existing MCP servers you want to integrate?

  ## MCP SERVERS YOU NEED

  Which MCP servers do you want to configure?
  - **Git**: Repository operations and version control
  - **Filesystem**: File system access and manipulation
  - **Memory**: Persistent knowledge storage
  - **Sequential Thinking**: Enhanced reasoning workflows
  - **LLM Context**: Context management tools
  - **GitHub**: GitHub API integration
  - **Other**: Specify custom servers

  ## WORKSPACE & SECURITY

  - What workspace directory should be accessible?
  - Do you need read-only or read-write access?
  - Any API tokens or credentials to configure? (GitHub, etc.)
  - Docker volume preferences for persistent data?

  ---

  Based on your answers, I'll provide:

  ## 1. COMPLETE CONFIGURATION FILE

  A ready-to-use JSON configuration for `claude_desktop_config.json`:

  ```json
  {
    "mcpServers": {
      "server-name": {
        "command": "docker|uv|npx",
        "args": ["appropriate", "arguments"],
        "env": {
          "ENV_VAR": "value"
        }
      }
    }
  }
  ```

  ## 2. DOCKER SETUP INSTRUCTIONS

  For Docker-based servers:
  - Volume mount configurations for your workspace
  - Environment variable setup
  - Security considerations (read-only mounts, network isolation)
  - Persistent storage for memory/data

  ## 3. NATIVE SETUP INSTRUCTIONS

  For native servers:
  - Installation commands (uv, npx, pip)
  - Path configurations
  - Dependency requirements
  - Environment setup

  ## 4. SERVER-SPECIFIC DETAILS

  ### Git Server
  - Workspace access configuration
  - Git credentials handling
  - Repository path mounting

  ### Filesystem Server
  - Directory access permissions
  - Read/write configurations
  - Security boundaries

  ### GitHub Server
  - Personal access token setup
  - Scope and permissions
  - API rate limiting

  ### Memory Server
  - Persistent volume configuration
  - Data retention policies
  - Backup strategies

  ## 5. TESTING & VALIDATION

  - How to test each server connection
  - Common troubleshooting steps
  - Verification commands
  - Log locations

  ## 6. SECURITY BEST PRACTICES

  - Token management and rotation
  - Workspace access restrictions
  - Docker security configurations
  - Credential storage recommendations

  **Ready to get started?** Tell me about your environment and which MCP servers you need!
---
