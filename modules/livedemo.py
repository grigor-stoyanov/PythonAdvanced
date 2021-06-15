# a module is a file with python code
# stored in packages they contain different functionality that can be imported in other code
# builtin modules math,os,sys,itertools,random,functools
import math as m

# needs to be called every time with the function
print(m.trunc(4.5))

# python reads code from top to bottom so to avoid collisions with simular names its better to avoid import from
from math import sqrt
from math import *


def sqrt():
    print('hello')


print(sqrt())

# the correct way to order imports is from top in alphabetic order separated by a row
# installing custom modules can be done using terminal install pip command
# its good to install them in a virtual evnironment venv so they will not be affected by future updates
# virtualenv venv cd ..venv/script activate
# u can see all installed modules in a requirements file using a pip command pip freeze > requirements.txt
# and u can install certain modules from a file as such pip install -r requirements.txt

# any .py file can be imported allowing us to create our own custom modules
# by creating a python package we get a __init__.py file allowing us to import python files
# by starting a py file with an import it goes trough the init and other files until it reaches the function to be imported
# if there is an import in the module file that is being imported it goes trough them as well running everything in the code
# a way to avoid that is using if __name__ == '__main__': in the module code file
# importing your own custom files start from the root project folder
