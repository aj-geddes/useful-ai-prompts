# API Gateway Security Configuration

## API Gateway Security Configuration

```yaml
# nginx-api-gateway.conf
# Nginx API Gateway with security hardening

http {
    # Security headers
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header Content-Security-Policy "default-src 'self'" always;

    # Rate limiting zones
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=auth_limit:10m rate=1r/s;
    limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

    # Request body size limit
    client_max_body_size 10M;
    client_body_buffer_size 128k;

    # Timeout settings
    client_body_timeout 12;
    client_header_timeout 12;
    send_timeout 10;

    server {
        listen 443 ssl http2;
        server_name api.example.com;

        # SSL configuration
        ssl_certificate /etc/ssl/certs/api.example.com.crt;
        ssl_certificate_key /etc/ssl/private/api.example.com.key;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;

        # API endpoints
        location /api/ {
            # Rate limiting
            limit_req zone=api_limit burst=20 nodelay;
            limit_conn conn_limit 10;

            # CORS headers
            add_header Access-Control-Allow-Origin "https://app.example.com" always;
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE" always;
            add_header Access-Control-Allow-Headers "Authorization, Content-Type" always;

            # Block common exploits
            if ($request_method !~ ^(GET|POST|PUT|DELETE|HEAD)$ ) {
                return 444;
            }

            # Proxy to backend
            proxy_pass http://backend:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            # Timeouts
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }

        # Auth endpoints with stricter limits
        location /api/auth/ {
            limit_req zone=auth_limit burst=5 nodelay;

            proxy_pass http://backend:3000;
        }

        # Block access to sensitive files
        location ~ /\. {
            deny all;
            return 404;
        }
    }
}
```
