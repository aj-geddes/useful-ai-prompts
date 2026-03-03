# Component Diagram

## Component Diagram

```plantuml
@startuml
package "Frontend" {
  [Web App]
  [Mobile App]
}

package "API Gateway" {
  [Load Balancer]
  [API Gateway]
}

package "Microservices" {
  [User Service]
  [Product Service]
  [Order Service]
  [Payment Service]
}

package "Data Stores" {
  database "PostgreSQL" {
    [User DB]
    [Product DB]
    [Order DB]
  }
  database "Redis" {
    [Cache]
    [Session Store]
  }
}

[Web App] --> [Load Balancer]
[Mobile App] --> [Load Balancer]
[Load Balancer] --> [API Gateway]
[API Gateway] --> [User Service]
[API Gateway] --> [Product Service]
[API Gateway] --> [Order Service]
[API Gateway] --> [Payment Service]

[User Service] --> [User DB]
[Product Service] --> [Product DB]
[Order Service] --> [Order DB]
[User Service] --> [Cache]
[Product Service] --> [Cache]
[API Gateway] --> [Session Store]
@enduml
```
