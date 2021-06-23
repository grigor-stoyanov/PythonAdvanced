def input_number():
    num = 0
    while not num:
        try:
            num = int(input())
        except ValueError:
            print('The value must be an integer')
            continue
    return num


numbers_dictionary = {}

while (line := input()) != "Search":
    number_as_string = line
    number = input_number()
    numbers_dictionary[number_as_string] = number

while (line := input()) != "Remove":
    searched = line
    print(numbers_dictionary.get(searched, 'Number does not exist.'))

while (line := input()) != "End":
    removed = line
    try:
        del numbers_dictionary[removed]
    except KeyError:
        print('Number does not exist in dictionary')
        continue

print(numbers_dictionary)
