import os

try:
    os.remove('asd.txt')
except FileNotFoundError:
    print('file does not exist!')

# if os.path.exists('asd.txt'):
#   os.remove('asd.txt')
# else:
#   print('file does not exist!')
