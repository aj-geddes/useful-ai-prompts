---
category: technical-workflows
date: '2025-08-14'
description: ''
layout: prompt
prompt: "{\n  \"mcpServers\": {\n    \"git\": {\n      \"command\": \"docker\",\n      \"args\": [\n        \"run\",\n        \"--rm\",\n        \"-i\",\n        \"--mount\",\n        \"type=bind,src=C:\\\\Users\\\\[USERNAME],dst=/mnt/workspace\",\n        \"mcp/git\"\n      ]\n    },\n    \"filesystem\": {\n      \"command\": \"docker\",\n      \"args\": [\n        \"run\",\n        \"-i\",\n        \"--rm\",\n        \"-v\",\n        \"C:\\\\Users\\\\[USERNAME]:/mnt/workspace:rw\",\n        \"mcp/filesystem\",\n        \"/mnt/workspace\"\n      ]\n    },\n    \"memory\": {\n      \"command\": \"docker\",\n      \"args\": [\n        \"run\",\n        \"-i\",\n        \"-v\",\n        \"claude-memory:/app/dist\",\n        \"--rm\",\n        \"mcp/memory\"\n      ]\n    },\n    \"sequentialthinking\": {\n      \"command\": \"docker\",\n      \"args\": [\"run\", \"--rm\", \"-i\", \"mcp/sequentialthinking\"]\n    },\n    \"llm-context\": {\n      \"command\": \"uv\",\n      \"args\": [\"tool\", \"run\", \"--from\", \"llm-context\", \"lc-mcp\"]\n    },\n    \"github\": {\n      \"command\": \"docker\",\n      \"args\": [\n        \"run\",\n        \"-i\",\n        \"--rm\",\n        \"-e\",\n        \"GITHUB_PERSONAL_ACCESS_TOKEN\",\n        \"ghcr.io/github/github-mcp-server\"\n      ],\n      \"env\": { \"GITHUB_PERSONAL_ACCESS_TOKEN\": \"[YOUR_GITHUB_TOKEN]\" }\n    }\n  }\n}"
slug: claude-mcp-example
tags: []
title: Claude Desktop MCP Configuration Template
version: 1.0.0
---
