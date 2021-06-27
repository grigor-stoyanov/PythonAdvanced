from collections import deque


def math_operations(*args, **kwargs):
    mapper = {
        'a': lambda x, y: x + y,
        's': lambda x, y: x - y,
        'd': lambda x, y: x / y,
        'm': lambda x, y: x * y
    }
    args = deque(args)
    while args:
        for key, value in kwargs.items():
            if not args:
                break
            try:
                kwargs[key] = mapper[key](value, args.popleft())
            except ZeroDivisionError:
                continue
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
