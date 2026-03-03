# Docker Debugging Basics

## Docker Debugging Basics

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

# Copy files from container
docker cp <container-id>:/path/to/file /local/path

# View image layers
docker history <image-name>
docker inspect <image-name>
```
