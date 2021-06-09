# python file objects are just the same as any object
# built in io methods
# open expects the file to be in the same directory if no path has been set
# it returns a file object  whose type depends on the mode
a = open("example.txt", "r")
# "r" -read mode "w" write mode cd .. means 1 level backwards + read & write, x create new file for write, text mode t , b binary mode
try:
    a = open("../file_handling_and_pandas/example.txt")
except FileNotFoundError:
    print('File not found or path is incorrect')
# read will read parts of the file (first 2 bytes and subsequent when called again)
print(a.read(2))
print(a.read(2))
print(type(a.read()))
# returns an entire row
print(a.readline())
# write creates a file with given name and if it exists its overwritten!
file = open('python.txt', 'w')
file.write('hello\n')
file.write('there\n')
file.close()
# its good for files to be closed after use to avoid errors
file = open('python.txt', 'a')
file.write('content\n')
# append wont delete previous content
content = ['1\n', '2\n', '3\n']
file.writelines(content)
file.close()
# only temporary information with a same standard is usually kept in files
# for important files a database is involved
# files are case insensitive by default on windows depending on setting
# with statements automatically closes the file and assigns it to a variable
with open('file.txt', 'w') as f:
    f.write('test')
import os

try:
    os.remove('asd.txt')
except FileNotFoundError:
    print('file does not exist!')
# if os.path.exists('asd.txt'):
# os.remove('asd.txt')
# still returns file not found error if it is already deleted
# there is a method to reach the absolute file path without hardcoding it
current_dir = os.path.dirname(os.path.abspath(__file__))
# saving it in a variable makes it change with each time it changes directory
print(current_dir)
path = os.path.join(current_dir, '..', 'file_handling_and_pandas', 'example.txt')
# we can create new paths with existing ones using join method which adapts to os pathing style
with open(path) as file:
    file.close()
# default pathing style is linux
print(__file__)
# gives list of strings of names of all current directory ./ and ../ with a step backwards
print(os.listdir('./'))
print('type_hinting.py' in os.listdir('../'))
print(os.path.abspath(__file__))
