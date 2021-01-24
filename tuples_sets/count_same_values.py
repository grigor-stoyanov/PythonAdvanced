import timeit

# def get_index(my_tuple, element, index):
#     indices = []
#     while True:
#         try:
#             new_index = my_tuple.index(element, index)
#             indices.append(new_index)
#             index = new_index + 1
#         except ValueError:
#             break
#     return indices
#
#
nums_tuple = tuple(map(float, input().split()))
start = timeit.default_timer()
# This code iterates trough every unique number until it finds all copies
# But it extracts each number's indexes every time by going trough them all
# i = 0
# indices_list = []
# while i < len(nums_tuple):
#     if i not in indices_list:
#         indices_list.extend(get_index(nums_tuple, nums_tuple[i], min()))
#         print(f'{nums_tuple[i]} - {nums_tuple.count(nums_tuple[i])} times')
#     elif len(indices_list) == len(nums_tuple):
#         break
#     i += 1
# This code counts every number in the tuple until it reaches the last one
# But it also counts the numbers multiple times
# nums_count = {}
# for num in nums_tuple:
#     nums_count[num] = nums_tuple.count(num)
# for num, count in nums_count.items():
#     print(f'{num} - {count} times')
# This code goes trough each number in the tuple
# but only increments the their values in a dictionary and is the fastest solution
nums_count = {}
for num in nums_tuple:
    nums_count[num] = nums_count.get(num, 0) + 1
for num, count in nums_count.items():
    print(f'{num} - {count} times')
print(f'time elapsed {timeit.default_timer() - start:.10f}')