# User Data Script

## User Data Script

```bash
#!/bin/bash
# user-data.sh

set -e
set -x

# Update system
apt-get update
apt-get upgrade -y

# Install dependencies
apt-get install -y \
  curl \
  wget \
  git \
  nodejs \
  npm \
  postgresql-client

# Install Node.js application
mkdir -p /opt/app
cd /opt/app
git clone https://github.com/myorg/myapp.git .
npm install --production

# Create systemd service
cat > /etc/systemd/system/myapp.service << EOF
[Unit]
Description=My Node App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/opt/app
ExecStart=/usr/bin/node index.js
Restart=on-failure
RestartSec=5

Environment="NODE_ENV=production"
Environment="PORT=3000"

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable myapp
systemctl start myapp

# Install and configure CloudWatch agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
dpkg -i -E ./amazon-cloudwatch-agent.deb

# Configure log streaming
cat > /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json << EOF
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/syslog",
            "log_group_name": "/aws/ec2/web-server",
            "log_stream_name": "{instance_id}"
          },
          {
            "file_path": "/opt/app/logs/*.log",
            "log_group_name": "/aws/ec2/app",
            "log_stream_name": "{instance_id}"
          }
        ]
      }
    }
  },
  "metrics": {
    "metrics_collected": {
      "cpu": {"measurement": [{"name": "cpu_usage_idle"}]},
      "mem": {"measurement": [{"name": "mem_used_percent"}]},
      "disk": {"measurement": [{"name": "used_percent"}]}
    }
  }
}
EOF

/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -s \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```
