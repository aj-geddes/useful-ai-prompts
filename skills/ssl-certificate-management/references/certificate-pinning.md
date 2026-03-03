# Certificate Pinning

## Certificate Pinning

```nginx
# nginx-certificate-pinning.conf
server {
    listen 443 ssl http2;
    server_name api.myapp.com;

    ssl_certificate /etc/nginx/certs/server.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    # Certificate pinning for API clients
    add_header Public-Key-Pins 'pin-sha256="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="; pin-sha256="BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB="; max-age=2592000; includeSubDomains' always;

    location / {
        proxy_pass http://backend;
    }
}
```
