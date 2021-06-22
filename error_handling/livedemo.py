# different type errors TypeError,NameError(when object is missing/not defined)
# ,ZeroDivisionError,ValueError,SyntaxError,IndexError,KeyError
# exceptions are useful for validations when handling large quantity of information
# you can use the __init__ file in packages to hide functions in an __all__=[''] variable
# so you can select the functions to import from that module and avoid errors this is called capsulating
# sometimes we need custom exceptions
# Exeption holds all the default exeption and is inhereted to create new ones
class MyCustomError(Exception):
    """explanation of custom exception details"""
    pass


raise MyCustomError("Appropriate Message for this exception")
raise ValueError('Some message')


class ValueTooSmall(Exception):
    num = int(input())
    if num < 5:
        raise ValueTooSmall


# handling exceptions allows the code to continue running
# its good except statements not to be left broad to avoid sending wrong error messages
while True:
    try:
        x = int(input('enter number'))
        print(5 / x)
        break
    except (ValueError, ZeroDivisionError):
        print('invalid number')
    except MyCustomError:
        raise MyCustomError
    # finally clause executes before try completes and regardless of exception even if an except raises error
    finally:
        print('finally')
# errors are objects and its arguments can be accessed
