# reduce is a generator like map that allows to do operations to 2 parameters at a time

from functools import reduce

def multiply(*args):
    # result = 1
    # for ele in args:
    #     result *= ele
    # return result
    return(reduce(lambda x,y: x*y, args))

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
