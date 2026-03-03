# Playbook Structure and Best Practices

## Playbook Structure and Best Practices

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
      tags: [verify]

# roles/common/tasks/main.yml
---
- name: Update system packages
  apt:
    update_cache: yes
    cache_valid_time: 3600
  when: ansible_os_family == 'Debian'

- name: Install required packages
  package:
    name: "{{ packages }}"
    state: present
  vars:
    packages:
      - curl
      - git
      - htop
      - python3-pip

- name: Configure sysctl settings
  sysctl:
    name: "{{ item.name }}"
    value: "{{ item.value }}"
    sysctl_set: yes
    state: present
  loop:
    - name: net.core.somaxconn
      value: 65535
    - name: net.ipv4.tcp_max_syn_backlog
      value: 65535
    - name: fs.file-max
      value: 2097152

- name: Create application user
  user:
    name: appuser
    shell: /bin/bash
    home: /home/appuser
    createhome: yes
    state: present

# roles/docker/tasks/main.yml
---
- name: Install Docker prerequisites
  package:
    name: "{{ docker_packages }}"
    state: present
  vars:
    docker_packages:
      - apt-transport-https
      - ca-certificates
      - curl
      - gnupg
      - lsb-release

- name: Add Docker GPG key
  apt_key:
    url: https://download.docker.com/linux/ubuntu/gpg
    state: present

- name: Add Docker repository
  apt_repository:
    repo: "deb https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
    state: present

- name: Install Docker
  package:
    name:
      - docker-ce
      - docker-ce-cli
      - containerd.io
    state: present

- name: Start Docker service
  systemd:
    name: docker
    enabled: yes
    state: started

- name: Add user to docker group
  user:
    name: appuser
    groups: docker
    append: yes

# roles/application/tasks/main.yml
---
- name: Clone application repository
  git:
    repo: "{{ app_repo_url }}"
    dest: "/home/appuser/app"
    version: "{{ app_version }}"
    force: yes
  become: yes
  become_user: appuser

- name: Copy environment configuration
  template:
    src: .env.j2
    dest: "/home/appuser/app/.env"
    owner: appuser
    group: appuser
    mode: '0600'
  notify: restart application

- name: Build Docker image
  docker_image:
    name: "myapp:{{ app_version }}"
    build:
      path: "/home/appuser/app"
      pull: yes
    source: build
    state: present
  become: yes

- name: Start application container
  docker_container:
    name: myapp
    image: "myapp:{{ app_version }}"
    state: started
    restart_policy: always
    ports:
      - "8080:8080"
    volumes:
      - /home/appuser/app:/app:ro
    env:
      NODE_ENV: "{{ environment }}"
      LOG_LEVEL: "{{ log_level }}"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

handlers:
  - name: restart application
    docker_container:
      name: myapp
      state: restarted
```
