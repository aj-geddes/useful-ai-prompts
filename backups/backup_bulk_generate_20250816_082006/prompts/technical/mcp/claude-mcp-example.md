# Claude Desktop MCP Configuration Template

This template provides a comprehensive MCP server setup for Claude Desktop with essential development and productivity tools.

## Prerequisites

- **Docker Desktop** installed and running
- **Claude Desktop** application installed
- **Python/UV** installed (for llm-context server)
- **GitHub Personal Access Token** (for GitHub integration)

## Configuration File

Save this as your `claude_desktop_config.json` file:

### Windows Configuration

```json
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
```

### macOS/Linux Configuration

```json
{
  "mcpServers": {
    "git": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--mount",
        "type=bind,src=/Users/[USERNAME],dst=/mnt/workspace",
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
        "/Users/[USERNAME]:/mnt/workspace:rw",
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
```

## Setup Instructions

### 1. Find Your Configuration File Location

**Windows:**

```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**

```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Linux:**

```
~/.config/Claude/claude_desktop_config.json
```

### 2. Customize the Template

1. **Replace `[USERNAME]`** with your actual system username
2. **Replace `[YOUR_GITHUB_TOKEN]`** with your GitHub Personal Access Token

### 3. Generate GitHub Personal Access Token

1. Go to GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Generate new token with these scopes:
   - `repo` (for private repository access)
   - `public_repo` (for public repository access)
   - `read:org` (for organization access)
   - `user` (for user information)

### 4. Install Required Dependencies

**Install UV (for llm-context server):**

```bash
# Windows/macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Pull Docker Images:**

```bash
docker pull mcp/git
docker pull mcp/filesystem
docker pull mcp/memory
docker pull mcp/sequentialthinking
docker pull ghcr.io/github/github-mcp-server
```

## Server Capabilities

### 🗂️ **Filesystem Server**

- Read, write, create, delete files and directories
- Navigate local file system
- File content analysis and manipulation

### 🔧 **Git Server**

- Git repository operations
- Commit history analysis
- Branch management
- Git status and diff operations

### 🧠 **Memory Server**

- Persistent conversation memory
- Entity and relationship tracking
- Knowledge graph maintenance

### 🤔 **Sequential Thinking Server**

- Multi-step problem solving
- Thought process tracking
- Complex analysis workflows

### 📊 **LLM Context Server**

- Code analysis and understanding
- Project context generation
- Codebase exploration

### 🐙 **GitHub Server**

- Repository management
- Issue and PR operations
- GitHub API integration
- Code review workflows

## Configuration File Location by OS

- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

## Troubleshooting

### Docker Issues

- Ensure Docker Desktop is running
- Check that all required images are pulled
- Verify mount paths exist and are accessible

### Permission Issues

- On Windows, ensure Docker has access to your user directory
- On macOS/Linux, check file permissions for mounted directories

### GitHub Token Issues

- Verify token has correct scopes
- Check token isn't expired
- Ensure token is properly formatted in configuration

### Server Connection Issues

1. Restart Claude Desktop after configuration changes
2. Check Claude Desktop Developer settings for server status
3. Review Docker container logs for error messages

## Advanced Customization

### Custom Workspace Directory

To use a different workspace directory, update both `git` and `filesystem` server mount paths:

**Windows Example:**

```json
"src=D:\\Projects,dst=/mnt/workspace"
```

**macOS/Linux Example:**

```json
"src=/home/user/projects,dst=/mnt/workspace"
```

### Adding Additional Servers

You can add more MCP servers to this configuration. Popular options include:

- Database servers (PostgreSQL, SQLite)
- API integration servers
- Notification servers
- Custom development tools

## Security Notes

- Keep your GitHub token secure and never share it
- Regularly rotate your GitHub Personal Access Token
- Review which directories you're mounting to Docker containers
- Consider using environment variables for sensitive configuration

## Support

If you encounter issues:

1. Check the [MCP Documentation](https://modelcontextprotocol.io/)
2. Review Docker container logs
3. Verify all prerequisites are installed
4. Ensure configuration file syntax is valid JSON

---

**Note:** This template is based on a working Windows configuration and has been adapted for cross-platform use. Adjust paths and commands as needed for your specific environment.
