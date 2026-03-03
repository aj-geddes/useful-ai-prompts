# Nginx Configuration

## Nginx Configuration

```nginx
# nginx.conf - API Gateway configuration
upstream user_service {
    server user-service:3000;
    keepalive 32;
}

upstream product_service {
    server product-service:3001;
    keepalive 32;
}

upstream order_service {
    server order-service:3002;
    keepalive 32;
}

# Rate limiting
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_req_zone $http_x_api_key zone=user_limit:10m rate=100r/s;

server {
    listen 80;
    server_name api.example.com;

    # Enable gzip compression
    gzip on;
    gzip_types application/json;
    gzip_min_length 1000;

    # User Service Routes
    location /api/users {
        limit_req zone=api_limit burst=20 nodelay;

        # Authentication check
        access_by_lua_block {
            local token = ngx.var.http_authorization
            if not token then
                return ngx.HTTP_UNAUTHORIZED
            end
        }

        proxy_pass http://user_service;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Request timeout
        proxy_connect_timeout 10s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    # Product Service Routes
    location /api/products {
        limit_req zone=api_limit burst=50 nodelay;

        proxy_pass http://product_service;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # Caching
        proxy_cache api_cache;
        proxy_cache_valid 200 1m;
        proxy_cache_key "$scheme$request_method$host$request_uri";
    }

    # Order Service Routes (requires auth)
    location /api/orders {
        limit_req zone=user_limit burst=10 nodelay;

        auth_request /auth;
        auth_request_set $auth_user $upstream_http_x_user_id;

        proxy_pass http://order_service;
        proxy_http_version 1.1;
        proxy_set_header X-User-ID $auth_user;
    }

    # Health check endpoint
    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }

    # Metrics endpoint
    location /metrics {
        stub_status on;
        access_log off;
    }
}

# Cache definition
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=api_cache:10m max_size=1g inactive=60m;
```
