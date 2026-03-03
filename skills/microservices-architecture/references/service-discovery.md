# Service Discovery

## Service Discovery

### Consul Example

```typescript
// service-registry/consul-client.ts
import Consul from "consul";

export class ServiceRegistry {
  private consul: Consul.Consul;

  constructor() {
    this.consul = new Consul({
      host: "consul",
      port: 8500,
    });
  }

  // Register service
  async register(serviceName: string, servicePort: number) {
    await this.consul.agent.service.register({
      id: `${serviceName}-${process.env.HOSTNAME}`,
      name: serviceName,
      address: process.env.SERVICE_IP,
      port: servicePort,
      check: {
        http: `http://${process.env.SERVICE_IP}:${servicePort}/health`,
        interval: "10s",
        timeout: "5s",
      },
    });
  }

  // Discover service
  async discover(serviceName: string): Promise<string> {
    const result = await this.consul.health.service({
      service: serviceName,
      passing: true,
    });

    if (result.length === 0) {
      throw new Error(`Service ${serviceName} not found`);
    }

    // Simple round-robin
    const service = result[Math.floor(Math.random() * result.length)];
    return `http://${service.Service.Address}:${service.Service.Port}`;
  }

  // Deregister on shutdown
  async deregister(serviceId: string) {
    await this.consul.agent.service.deregister(serviceId);
  }
}
```

### Kubernetes Service Discovery

```yaml
# user-service-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
        - name: user-service
          image: user-service:latest
          ports:
            - containerPort: 3000
          env:
            - name: SERVICE_NAME
              value: "user-service"
```

```typescript
// Service call in Kubernetes
const userServiceUrl = process.env.USER_SERVICE_URL || "http://user-service";
const response = await fetch(`${userServiceUrl}/users/${userId}`);
```
