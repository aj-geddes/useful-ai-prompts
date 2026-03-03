# gRPC Polyglot Communication

## gRPC Polyglot Communication

```protobuf
// service.proto
syntax = "proto3";

service Calculator {
  rpc Add (NumberPair) returns (Result);
  rpc Multiply (NumberPair) returns (Result);
}

message NumberPair {
  double a = 1;
  double b = 2;
}

message Result {
  double value = 1;
}
```

```python
# Python gRPC Server
import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class Calculator(service_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return service_pb2.Result(value=request.a + request.b)

    def Multiply(self, request, context):
        return service_pb2.Result(value=request.a * request.b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

```typescript
// Node.js gRPC Client
import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";

const packageDefinition = protoLoader.loadSync("service.proto");
const proto = grpc.loadPackageDefinition(packageDefinition);

const client = new proto.Calculator(
  "localhost:50051",
  grpc.credentials.createInsecure(),
);

client.Add({ a: 10, b: 20 }, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("Result:", response.value);
  }
});
```
