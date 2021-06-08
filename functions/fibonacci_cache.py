# because function is recursive it must return istsself n^n times
# we need to memorise past calls so future calls not to repeat previous ones
# there is a decorator that simplifies this cache mechanic
# from functools import lru_cache
# @lru_cache(maxsize=1000)
fibonacci_cache = {}


# if we have cached value return it

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    #   return 1
    if n == 2:
        value = 1
    #   return 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    #   return fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci_cache[n] = value
    return value


for n in range(1, 100):
    print(n, ':', fibonacci(n))
