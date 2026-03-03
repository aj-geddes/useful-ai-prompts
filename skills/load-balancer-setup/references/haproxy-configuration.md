# HAProxy Configuration

## HAProxy Configuration

```conf
# /etc/haproxy/haproxy.cfg
global
    log stdout local0
    log stdout local1 notice
    maxconn 4096
    daemon

    # Security
    tune.ssl.default-dh-param 2048
    ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256
    ssl-default-bind-options ssl-min-ver TLSv1.2

defaults
    log global
    mode http
    option httplog
    option denylogin
    option forwardfor
    option http-server-close

    # Timeouts
    timeout connect 5000
    timeout client 50000
    timeout server 50000

    # Stats
    stats enable
    stats uri /stats
    stats refresh 30s
    stats admin if TRUE

# Frontend - Public facing
frontend web_frontend
    bind *:80
    bind *:443 ssl crt /etc/ssl/certs/myapp.pem
    mode http
    option httplog

    # Redirect HTTP to HTTPS
    http-request redirect scheme https if !{ ssl_fc }

    # Logging
    log /dev/log local0 debug

    # Rate limiting
    stick-table type ip size 100k expire 30s store http_req_rate(10s)
    http-request track-sc0 src
    http-request deny if { sc_http_req_rate(0) gt 100 }

    # ACLs
    acl is_websocket hdr(Upgrade) -i websocket
    acl is_api path_beg /api/
    acl is_health path /health
    acl is_static path_beg /static/

    # Route to appropriate backend
    use_backend health_backend if is_health
    use_backend api_backend if is_api
    use_backend static_backend if is_static
    use_backend web_backend if is_websocket
    default_backend web_backend

# Frontend for internal API
frontend internal_api_frontend
    bind 127.0.0.1:8080
    mode http
    default_backend stats_backend

# Health check backend
backend health_backend
    mode http
    balance roundrobin
    server local 127.0.0.1:8080 check

# Main web backend
backend web_backend
    mode http
    balance roundrobin

    # Session persistence
    cookie SERVERID insert indirect nocache

    # Compression
    compression algo gzip
    compression type text/html text/plain text/css application/json

    # Servers with health checks
    server web1 10.0.1.10:8080 check cookie web1 weight 5
    server web2 10.0.1.11:8080 check cookie web2 weight 5
    server web3 10.0.1.12:8080 check cookie web3 weight 3

    # Health check configuration
    option httpchk GET /health HTTP/1.1\r\nHost:\ localhost
    timeout check 5s

# API backend with connection limits
backend api_backend
    mode http
    balance least_conn
    maxconn 1000

    option httpchk GET /api/health
    timeout check 5s

    server api1 10.0.2.10:3000 check weight 5
    server api2 10.0.2.11:3000 check weight 5
    server api3 10.0.2.12:3000 check weight 3

# Static file backend
backend static_backend
    mode http
    balance roundrobin

    # Cache control for static files
    http-response set-header Cache-Control "public, max-age=31536000, immutable"

    server static1 10.0.3.10:80 check
    server static2 10.0.3.11:80 check

# Stats backend
backend stats_backend
    stats enable
    stats uri /stats
    stats refresh 30s
```
