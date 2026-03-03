# Istio-based Canary Deployment

## Istio-based Canary Deployment

```yaml
# canary-deployment-istio.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-v1
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: v1
  template:
    metadata:
      labels:
        app: myapp
        version: v1
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:1.0.0
          ports:
            - containerPort: 8080

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-v2
  namespace: production
spec:
  replicas: 1 # Start with minimal replicas for canary
  selector:
    matchLabels:
      app: myapp
      version: v2
  template:
    metadata:
      labels:
        app: myapp
        version: v2
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:2.0.0
          ports:
            - containerPort: 8080

---
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
  namespace: production
spec:
  hosts:
    - myapp
  http:
    # Canary: 5% to v2, 95% to v1
    - match:
        - headers:
            user-agent:
              regex: ".*Chrome.*" # Test with Chrome
      route:
        - destination:
            host: myapp
            subset: v2
          weight: 100
      timeout: 10s

    # Default route with traffic split
    - route:
        - destination:
            host: myapp
            subset: v1
          weight: 95
        - destination:
            host: myapp
            subset: v2
          weight: 5
      timeout: 10s

---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myapp
  namespace: production
spec:
  host: myapp
  trafficPolicy:
    connectionPool:
      http:
        http1MaxPendingRequests: 100
        maxRequestsPerConnection: 2

  subsets:
    - name: v1
      labels:
        version: v1

    - name: v2
      labels:
        version: v2
      trafficPolicy:
        outlierDetection:
          consecutive5xxErrors: 3
          interval: 30s
          baseEjectionTime: 30s

---
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: myapp
  namespace: production
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  progressDeadlineSeconds: 300
  service:
    port: 80

  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 5
    stepWeightPromotion: 10

  metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m

    - name: request-duration
      thresholdRange:
        max: 500
      interval: 30s

  webhooks:
    - name: acceptance-test
      url: http://flagger-loadtester/
      timeout: 30s
      metadata:
        type: smoke
        cmd: "curl -sd 'test' http://myapp-canary/api/test"

    - name: load-test
      url: http://flagger-loadtester/
      timeout: 5s
      metadata:
        cmd: "hey -z 1m -q 10 -c 2 http://myapp-canary/"
        logCmdOutput: "true"

  # Automatic rollback on failure
  skipAnalysis: false
```
