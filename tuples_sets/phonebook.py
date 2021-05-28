phone_book = {}
line = input()
while not line.isdigit():
    name, number = line.split('-')
    phone_book[name] = number
    line = input()
for i in range(int(line)):
    name = input()
    if name in phone_book.keys():
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')