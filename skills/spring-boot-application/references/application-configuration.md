# Application Configuration

## Application Configuration

```yaml
# application.yml
spring:
  application:
    name: api-service
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASSWORD}
    driver-class-name: org.postgresql.Driver
  jpa:
    hibernate:
      ddl-auto: validate
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
  security:
    jwt:
      secret: ${JWT_SECRET}
      expiration: 86400000

server:
  port: 8080
  servlet:
    context-path: /
```
