# Inventory and Variables

## Inventory and Variables

```yaml
# inventory/hosts.ini
[webservers]
web1 ansible_host=10.0.1.10
web2 ansible_host=10.0.1.11
web3 ansible_host=10.0.1.12

[databases]
db1 ansible_host=10.0.2.10 db_role=primary
db2 ansible_host=10.0.2.11 db_role=replica

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3

# inventory/group_vars/webservers.yml
---
app_version: "1.2.3"
app_repo_url: "https://github.com/myorg/myapp.git"
environment: production
log_level: INFO

# inventory/host_vars/web1.yml
---
server_role: primary
max_connections: 500
```
