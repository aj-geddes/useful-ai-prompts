# Java from Python (Py4J)

## Java from Python (Py4J)

```java
// JavaApp.java
public class JavaApp {
    public int add(int a, int b) {
        return a + b;
    }

    public String processData(String data) {
        return data.toUpperCase();
    }

    public static void main(String[] args) {
        JavaApp app = new JavaApp();
        GatewayServer server = new GatewayServer(app);
        server.start();
    }
}
```

```python
# Python client
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
app = gateway.entry_point

result = app.add(10, 20)
print(f"Result: {result}")

processed = app.processData("hello world")
print(f"Processed: {processed}")
```
