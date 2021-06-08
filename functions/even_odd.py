def even_odd(*args):
    even_odd_list = list(args)
    flag = even_odd_list.pop()
    if flag == 'even':
        even_odd_list = list(filter(lambda x: True if x % 2 == 0 else False, even_odd_list))
    elif flag == 'odd':
        even_odd_list = list(filter(lambda x: True if x % 2 == 1 else False, even_odd_list))
    return even_odd_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
