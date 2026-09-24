```python
x = 10


def bad_function_name(a, b, c, d, e, f):
    """Process the given values."""
    local_value = 1
    zero = 0

    if a:
        if not b:
            if c is None:
                try:
                    result = a + b
                    result = e[0] + f + local_value + zero
                    print(result)
                except (IndexError, TypeError):
                    return None
    else:
        return None


bad_function_name(True, False, None, 1, [2], 3)
```
