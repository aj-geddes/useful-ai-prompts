# GCP Firewall Rules

## GCP Firewall Rules

```yaml
# gcp-firewall-rules.yaml
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: allow-http-https
spec:
  network:
    name: default
  direction: INGRESS
  priority: 1000
  sourceRanges:
    - 0.0.0.0/0
  allowed:
    - IPProtocol: tcp
      ports:
        - "80"
        - "443"
  targetTags:
    - http-server
    - https-server

---
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: allow-ssh-internal
spec:
  network:
    name: default
  direction: INGRESS
  priority: 1000
  sourceRanges:
    - 10.0.0.0/8
  allowed:
    - IPProtocol: tcp
      ports:
        - "22"
  targetTags:
    - allow-ssh

---
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: deny-all-ingress
spec:
  network:
    name: default
  direction: INGRESS
  priority: 65534
  denied:
    - IPProtocol: all
```
