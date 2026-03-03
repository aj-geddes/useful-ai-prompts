# Security Group Management Script

## Security Group Management Script

```bash
#!/bin/bash
# manage-security-groups.sh - Security group management utility

set -euo pipefail

ACTION="${1:-list}"
REGION="${2:-us-east-1}"

# List security groups
list_security_groups() {
    echo "Security Groups in $REGION:"
    aws ec2 describe-security-groups \
        --region "$REGION" \
        --query 'SecurityGroups[*].[GroupId,GroupName,VpcId]' \
        --output table
}

# Show security group details
show_security_group() {
    local sg_id="$1"
    echo "Inbound Rules for $sg_id:"
    aws ec2 describe-security-groups \
        --group-ids "$sg_id" \
        --region "$REGION" \
        --query 'SecurityGroups[0].IpPermissions' \
        --output table

    echo -e "\nOutbound Rules for $sg_id:"
    aws ec2 describe-security-groups \
        --group-ids "$sg_id" \
        --region "$REGION" \
        --query 'SecurityGroups[0].IpPermissionsEgress' \
        --output table
}

# Add inbound rule
add_inbound_rule() {
    local sg_id="$1"
    local protocol="$2"
    local port="$3"
    local cidr="$4"
    local description="${5:-}"

    aws ec2 authorize-security-group-ingress \
        --group-id "$sg_id" \
        --protocol "$protocol" \
        --port "$port" \
        --cidr "$cidr" \
        --region "$REGION" \
        ${description:+--description "$description"}

    echo "Rule added to $sg_id"
}

# Audit security groups for overly permissive rules
audit_security_groups() {
    echo "Auditing security groups for overly permissive rules..."

    aws ec2 describe-security-groups \
        --region "$REGION" \
        --query 'SecurityGroups[*].[GroupId,IpPermissions]' \
        --output text | while read sg_id; do

        # Check for 0.0.0.0/0 on sensitive ports
        if aws ec2 describe-security-groups \
            --group-ids "$sg_id" \
            --region "$REGION" \
            --query "SecurityGroups[0].IpPermissions[?FromPort==\`22\` || FromPort==\`3306\` || FromPort==\`5432\`]" \
            --output json | grep -q "0.0.0.0/0"; then
            echo "WARNING: $sg_id has sensitive ports open to 0.0.0.0/0"
        fi
    done
}

# Main
case "$ACTION" in
    list)
        list_security_groups
        ;;
    show)
        show_security_group "$3"
        ;;
    add-rule)
        add_inbound_rule "$3" "$4" "$5" "$6" "${7:-}"
        ;;
    audit)
        audit_security_groups
        ;;
    *)
        echo "Usage: $0 {list|show|add-rule|audit} [args]"
        exit 1
        ;;
esac
```
