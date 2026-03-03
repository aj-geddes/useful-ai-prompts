# Rust from Python (PyO3)

## Rust from Python (PyO3)

```rust
// lib.rs
use pyo3::prelude::*;

#[pyfunction]
fn fibonacci(n: u64) -> PyResult<u64> {
    let mut a = 0;
    let mut b = 1;

    for _ in 0..n {
        let temp = a;
        a = b;
        b = temp + b;
    }

    Ok(a)
}

#[pyfunction]
fn process_large_array(arr: Vec<f64>) -> PyResult<f64> {
    Ok(arr.iter().sum())
}

#[pymodule]
fn rust_extension(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(process_large_array, m)?)?;
    Ok(())
}
```

```python
# Usage in Python
import rust_extension

result = rust_extension.fibonacci(100)
print(f"Fibonacci: {result}")

arr = list(range(1000000))
total = rust_extension.process_large_array(arr)
print(f"Sum: {total}")
```
