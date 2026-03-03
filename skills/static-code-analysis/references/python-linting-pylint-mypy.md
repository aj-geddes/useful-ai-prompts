# Python Linting (pylint + mypy)

## Python Linting (pylint + mypy)

```python
# .pylintrc
[MASTER]
ignore=venv,.git,__pycache__
jobs=4

[MESSAGES CONTROL]
disable=
    missing-docstring,
    too-few-public-methods

[FORMAT]
max-line-length=100
max-module-lines=1000

[DESIGN]
max-args=5
max-locals=15
max-returns=6
max-branches=12
max-statements=50
```

```python
# mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_calls = True
warn_redundant_casts = True
warn_unused_ignores = True
strict_equality = True
```
