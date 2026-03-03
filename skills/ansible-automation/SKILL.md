---
name: ansible-automation
description: >
  Infrastructure automation and configuration management using Ansible
  playbooks, roles, and inventory. Use for deploying applications, patching, and
  managing servers.
---

# Ansible Automation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Automate infrastructure provisioning, configuration management, and application deployment across multiple servers using Ansible playbooks, roles, and dynamic inventory management.

## When to Use

- Configuration management
- Application deployment
- Infrastructure patching and updates
- Multi-server orchestration
- Cloud instance provisioning
- Container management
- Database administration
- Security compliance automation

## Quick Start

Minimal working example:

```yaml
# site.yml - Main playbook
---
- name: Deploy application stack
  hosts: all
  gather_facts: yes
  serial: 1  # Rolling deployment

  pre_tasks:
    - name: Display host information
      debug:
        var: inventory_hostname
      tags: [always]

  roles:
    - common
    - docker
    - application

  post_tasks:
    - name: Verify deployment
      uri:
        url: "http://{{ inventory_hostname }}:8080/health"
        status_code: 200
      retries: 3
      delay: 10
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Playbook Structure and Best Practices](references/playbook-structure-and-best-practices.md) | Playbook Structure and Best Practices |
| [Inventory and Variables](references/inventory-and-variables.md) | Inventory and Variables |
| [Ansible Deployment Script](references/ansible-deployment-script.md) | Ansible Deployment Script |
| [Configuration Template](references/configuration-template.md) | Configuration Template |

## Best Practices

### ✅ DO

- Use roles for modularity
- Implement proper error handling
- Use templates for configuration
- Leverage handlers for idempotency
- Use serial deployment for rolling updates
- Implement health checks
- Store inventory in version control
- Use vault for sensitive data

### ❌ DON'T

- Use command/shell without conditionals
- Copy files without templates
- Run without check mode first
- Mix environments in inventory
- Hardcode values
- Ignore error handling
- Use shell for simple tasks
