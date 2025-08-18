---
"category": |-
  technical-workflows
"date": |-
  2025-08-18
"description": ""
"layout": |-
  prompt
"prompt": |-
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
"slug": |-
  fastmcp-server-patterns
"tags": []
"title": |-
  Prompt Blueprint
"version": |-
  1.0.0
---
