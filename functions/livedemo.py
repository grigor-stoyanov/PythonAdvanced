# some functions or methods don't have return
nums = [1, 5, 3, 4]
# they always return none
print(nums.sort())
print(sorted(nums))
# lambda is an anonymous one time function that always returns something and must be used only once
print(lambda a: a + 5)


# argument is the object fed to a function and a parameter is in the function
# built in functions may shadow with variables of the same name
# *args **kwargs packing is useful when u dont know how much arguments u are feeding to ur function
def sum_func(*args):
    sumargs = 0
    for el in args:
        sumargs += int(el)
    return sumargs


sum_func(1, 2, 3, 4, 5, 6, 7, 8, 9)


# its always recommended to use get when using kwargs in a function
def sum_a_b(**kwargs):
    result = (kwargs['a'] + kwargs['b'])
    return result


sum_a_b(a=5, e=6, b=6, c=8)


# when using kwargs and args you need to order the arguments and parameters in right order (mandatory,named='default',*args,**kwargs)
# recursion is a function that calls itsself it needs a base case to stop or it wwill go into error
# local variables of function are saved in the thread and called again with a different value until it reaches base
def say_sth(base):
    if base == 0:
        return
    print('I am saying')
    say_sth(base-1)
# recursion is less optimal than a cycle
# recursion can be used to do different operation on different threads see expressions
say_sth(5)
