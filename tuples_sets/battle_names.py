n = int(input())
sum_names = 0
set_odd = set()
set_even = set()
for i in range(1, n + 1):
    name = input()
    for ch in name:
        sum_names += ord(ch)
    sum_names = sum_names // i
    if sum_names % 2 == 0:
        set_even.add(sum_names)
    else:
        set_odd.add(sum_names)
    sum_names = 0
if sum(set_odd) == sum(set_even):
    print(*(set_odd | set_even), sep=', ')
elif sum(set_odd) > sum(set_even):
    print(*(set_odd - set_even), sep=', ')
elif sum(set_even) > sum(set_odd):
    print(*(set_even ^ set_odd), sep=', ')
