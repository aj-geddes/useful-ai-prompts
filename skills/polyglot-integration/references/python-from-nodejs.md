# Python from Node.js

## Python from Node.js

```typescript
// Using child_process
import { spawn } from "child_process";

function callPython(script: string, args: any[] = []): Promise<any> {
  return new Promise((resolve, reject) => {
    const python = spawn("python3", [script, ...args.map(String)]);

    let stdout = "";
    let stderr = "";

    python.stdout.on("data", (data) => {
      stdout += data.toString();
    });

    python.stderr.on("data", (data) => {
      stderr += data.toString();
    });

    python.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(stderr));
      } else {
        try {
          resolve(JSON.parse(stdout));
        } catch (error) {
          resolve(stdout);
        }
      }
    });
  });
}

// Usage
const result = await callPython("./ml_model.py", [100, 200]);
console.log("Python result:", result);
```

```python
# ml_model.py
import sys
import json

def predict(x, y):
    # ML model logic
    return x * 2 + y

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = predict(x, y)
    print(json.dumps({'prediction': result}))
```
