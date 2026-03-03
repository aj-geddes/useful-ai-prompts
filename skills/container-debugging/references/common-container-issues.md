# Common Container Issues

## Common Container Issues

```yaml
Issue: Container Won't Start

Diagnosis:
  1. docker logs <container-id>
  2. Check exit code: docker inspect (ExitCode)
  3. Verify image exists: docker images
  4. Check entrypoint: docker inspect --format='{{.Config.Entrypoint}}'

Common Exit Codes:
  0: Normal exit
  1: General application error
  127: Command not found
  128+N: Terminated by signal N
  137: Out of memory (SIGKILL)
  139: Segmentation fault

Solutions:
  - Fix application error
  - Ensure required files exist
  - Check executable permissions
  - Verify working directory

---

Issue: Out of Memory

Symptoms: Exit code 137 (SIGKILL)

Debug:
  docker stats <container-id>
  # Check Memory usage vs limit

Solution:
  docker run -m 512m <image>
  # Increase memory limit
  docker inspect (MemoryLimit)
  # Check current limit

---

Issue: Port Already in Use

Error: "bind: address already in use"

Debug:
  docker ps  # Check running containers
  netstat -tlnp | grep 8080  # Check port usage

Solution:
  docker run -p 8081:8080 <image>
  # Use different host port

---

Issue: Network Issues

Symptom: Cannot reach other containers

Debug:
  docker network ls
  docker inspect <container-id> | grep IPAddress
  docker exec <container-id> ping <other-container>

Solution:
  docker network create app-network
  docker run --network app-network <image>
```
