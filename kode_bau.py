def bad_function_name(a, b, c, d, e, f):
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
                    pass
    else:
        return None


bad_function_name(True, False, None, 1, [2], 3)