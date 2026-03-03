---
name: container-debugging
description: >
  Debug Docker containers and containerized applications. Diagnose deployment
  issues, container lifecycle problems, and resource constraints.
---

# Container Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Container debugging focuses on issues within Docker/Kubernetes environments including resource constraints, networking, and application runtime problems.

## When to Use

- Container won't start
- Application crashes in container
- Resource limits exceeded
- Network connectivity issues
- Performance problems in containers

## Quick Start

Minimal working example:

```bash
# Check container status
docker ps -a
docker inspect <container-id>
docker stats <container-id>

# View container logs
docker logs <container-id>
docker logs --follow <container-id>  # Real-time
docker logs --tail 100 <container-id>  # Last 100 lines

# Connect to running container
docker exec -it <container-id> /bin/bash
docker exec -it <container-id> sh

# Inspect container details
docker inspect <container-id> | grep -A 5 "State"
docker inspect <container-id> | grep -E "Memory|Cpu"

# Check container processes
docker top <container-id>

# View resource usage
docker stats <container-id>
# Shows: CPU%, Memory usage, Network I/O

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Docker Debugging Basics](references/docker-debugging-basics.md) | Docker Debugging Basics |
| [Common Container Issues](references/common-container-issues.md) | Common Container Issues |
| [Container Optimization](references/container-optimization.md) | Container Optimization |
| [Debugging Checklist](references/debugging-checklist.md) | Debugging Checklist |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
