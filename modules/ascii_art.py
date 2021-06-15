import pyfiglet

from termcolor import colored

message = input()
print(pyfiglet.figlet_format(message))
print(colored('Hello', 'red', attrs=['bold']))
