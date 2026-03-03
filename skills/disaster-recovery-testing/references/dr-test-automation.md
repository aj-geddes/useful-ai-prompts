# DR Test Automation

## DR Test Automation

```yaml
# scheduled-dr-tests.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: quarterly-dr-test
  namespace: operations
spec:
  # Run quarterly on first Monday of each quarter at 2 AM
  schedule: "0 2 2-8 1,4,7,10 MON"
  jobTemplate:
    spec:
      backoffLimit: 0
      template:
        spec:
          serviceAccountName: dr-test-sa
          containers:
            - name: dr-test
              image: myrepo/dr-test:latest
              command:
                - /usr/local/bin/execute-dr-test.sh
              env:
                - name: SLACK_WEBHOOK
                  valueFrom:
                    secretKeyRef:
                      name: dr-notifications
                      key: slack-webhook
                - name: TEST_MODE
                  value: "full"
          restartPolicy: Never
```
