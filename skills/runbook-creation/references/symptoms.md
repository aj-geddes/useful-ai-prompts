# Symptoms

## Symptoms

- Health check endpoint returning 500 errors
- Users unable to access application
- Load balancer showing all instances unhealthy
- Alerts: `service_down`, `health_check_failed`


## Severity: P0 (Critical)


## Initial Response (5 minutes)

1. **Acknowledge the incident**
   ```bash
   # Acknowledge in PagerDuty
   # Post in #incidents Slack channel
   ```
````

2. **Create incident channel**

   ```
   Create Slack channel: #incident-YYYY-MM-DD-service-down
   Post incident details and status updates
   ```

3. **Assess impact**

   ```bash
   # Check service status
   kubectl get pods -n production

   # Check recent deployments
   kubectl rollout history deployment/api -n production

   # Check logs
   kubectl logs -f deployment/api -n production --tail=100
   ```
