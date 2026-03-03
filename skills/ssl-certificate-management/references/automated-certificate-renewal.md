# Automated Certificate Renewal

## Automated Certificate Renewal

```yaml
# certificate-renewal-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: certificate-renewal
  namespace: operations
spec:
  schedule: "0 2 * * 0" # Weekly at 2 AM Sunday
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: cert-renewal-sa
          containers:
            - name: renewer
              image: alpine:latest
              command:
                - sh
                - -c
                - |
                  apk add --no-cache kubectl curl jq openssl

                  echo "Checking certificate renewal status..."

                  # Get all certificates
                  kubectl get certificates -A -o json | jq -r '.items[] | "\(.metadata.name) \(.metadata.namespace)"' | \
                  while read cert namespace; do
                    status=$(kubectl get certificate "$cert" -n "$namespace" -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}')

                    if [ "$status" != "True" ]; then
                      echo "Renewing certificate: $cert in namespace $namespace"
                      kubectl annotate certificate "$cert" -n "$namespace" \
                        cert-manager.io/issue-temporary-certificate="true" \
                        --overwrite || true
                    fi
                  done

                  echo "Certificate renewal check complete"

          restartPolicy: OnFailure

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cert-renewal-sa
  namespace: operations

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cert-renewal
rules:
  - apiGroups: ["cert-manager.io"]
    resources: ["certificates"]
    verbs: ["get", "list", "patch", "annotate"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cert-renewal
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cert-renewal
subjects:
  - kind: ServiceAccount
    name: cert-renewal-sa
    namespace: operations
```
