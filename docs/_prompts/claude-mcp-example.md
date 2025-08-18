---
"category": |-
  technical-workflows
"date": |-
  2025-08-18
"description": ""
"layout": |-
  prompt
"prompt": |-
  {
    "mcpServers": {
      "git": {
        "command": "docker",
        "args": [
          "run",
          "--rm",
          "-i",
          "--mount",
          "type=bind,src=C:\\Users\\[USERNAME],dst=/mnt/workspace",
          "mcp/git"
        ]
      },
      "filesystem": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-v",
          "C:\\Users\\[USERNAME]:/mnt/workspace:rw",
          "mcp/filesystem",
          "/mnt/workspace"
        ]
      },
      "memory": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "-v",
          "claude-memory:/app/dist",
          "--rm",
          "mcp/memory"
        ]
      },
      "sequentialthinking": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "mcp/sequentialthinking"]
      },
      "llm-context": {
        "command": "uv",
        "args": ["tool", "run", "--from", "llm-context", "lc-mcp"]
      },
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "[YOUR_GITHUB_TOKEN]" }
      }
    }
  }
"slug": |-
  claude-mcp-example
"tags": []
"title": |-
  Claude Desktop MCP Configuration Template
"version": |-
  1.0.0
---
