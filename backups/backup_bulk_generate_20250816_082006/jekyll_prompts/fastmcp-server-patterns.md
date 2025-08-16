---
category: technical-workflows
date: '2025-08-14'
description: ''
layout: prompt
prompt: "async def run_command(command: str, cwd: str = \"/workspace\", timeout: int = 30) -> dict:\n    try:\n        process = await asyncio.create_subprocess_shell(\n            command,\n            cwd=cwd,\n            stdout=asyncio.subprocess.PIPE,\n            stderr=asyncio.subprocess.PIPE,\n            env={\"PATH\": os.environ.get(\"PATH\", \"\")}\n        )\n\n        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)\n\n        return {\n            \"command\": command,\n            \"cwd\": cwd,\n            \"stdout\": stdout.decode(),\n            \"stderr\": stderr.decode(),\n            \"returncode\": process.returncode,\n            \"success\": process.returncode == 0\n        }\n    except asyncio.TimeoutError:\n        raise MCPError(f\"Command timed out after {timeout}s\")\n    except Exception as e:\n        raise MCPError(f\"Subprocess execution error: {str(e)}\")"
slug: fastmcp-server-patterns
tags: []
title: Prompt Blueprint
version: 1.0.0
---
