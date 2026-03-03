# Python gRPC Server (grpcio)

## Python gRPC Server (grpcio)

```python
import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc
from datetime import datetime

class UserServicer(user_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.users = {}
        self.user_counter = 1

    def GetUser(self, request, context):
        if request.id not in self.users:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.User()
        return self.users[request.id]

    def ListUsers(self, request, context):
        users_list = list(self.users.values())
        page = request.page or 1
        limit = request.limit or 20
        offset = (page - 1) * limit

        return user_pb2.ListUsersResponse(
            users=users_list[offset:offset + limit],
            total=len(users_list),
            page=page
        )

    def CreateUser(self, request, context):
        user_id = str(self.user_counter)
        self.user_counter += 1

        user = user_pb2.User(
            id=user_id,
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            role=request.role,
            created_at=int(datetime.now().timestamp()),
            updated_at=int(datetime.now().timestamp())
        )
        self.users[user_id] = user
        return user

    def StreamUsers(self, request, context):
        for user in self.users.values():
            yield user

    def BulkCreateUsers(self, request_iterator, context):
        created_users = []
        for request in request_iterator:
            user = self.CreateUser(request, context)
            created_users.append(user)

        return user_pb2.ListUsersResponse(
            users=created_users,
            total=len(created_users),
            page=1
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server running on port 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```
