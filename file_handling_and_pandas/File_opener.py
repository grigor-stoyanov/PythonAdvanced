# from os import path
#
# if path.exists("file.txt"):
#     print('File found')
# else:
#     print('File not found')

try:
    open("file.txt")
    print('File Found')
except FileNotFoundError:
    print('File not found')