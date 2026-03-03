# Protocol Buffer Service Definition

## Protocol Buffer Service Definition

```protobuf
syntax = "proto3";

package user.service;

message User {
  string id = 1;
  string email = 2;
  string first_name = 3;
  string last_name = 4;
  string role = 5;
  int64 created_at = 6;
  int64 updated_at = 7;
}

message CreateUserRequest {
  string email = 1;
  string first_name = 2;
  string last_name = 3;
  string role = 4;
}

message UpdateUserRequest {
  string id = 1;
  string email = 2;
  string first_name = 3;
  string last_name = 4;
}

message GetUserRequest {
  string id = 1;
}

message ListUsersRequest {
  int32 page = 1;
  int32 limit = 2;
}

message ListUsersResponse {
  repeated User users = 1;
  int32 total = 2;
  int32 page = 3;
}

message DeleteUserRequest {
  string id = 1;
}

message Empty {}

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);
  rpc CreateUser(CreateUserRequest) returns (User);
  rpc UpdateUser(UpdateUserRequest) returns (User);
  rpc DeleteUser(DeleteUserRequest) returns (Empty);
  rpc StreamUsers(Empty) returns (stream User);
  rpc BulkCreateUsers(stream CreateUserRequest) returns (ListUsersResponse);
}

message Event {
  string type = 1;
  string user_id = 2;
  string data = 3;
  int64 timestamp = 4;
}

service EventService {
  rpc Subscribe(Empty) returns (stream Event);
  rpc PublishEvent(Event) returns (Empty);
}
```
