# gRPC Versioning

## gRPC Versioning

```protobuf
// v1/user.proto
syntax = "proto3";
package user.v1;

message User {
  string id = 1;
  string name = 2;
}

// v2/user.proto
syntax = "proto3";
package user.v2;

message User {
  string id = 1;
  string name = 2;
  string email = 3;
  Profile profile = 4;
}

message Profile {
  string avatar = 1;
  string bio = 2;
}

// Both versions can coexist
service UserServiceV1 {
  rpc GetUser (GetUserRequest) returns (user.v1.User);
}

service UserServiceV2 {
  rpc GetUser (GetUserRequest) returns (user.v2.User);
}
```
