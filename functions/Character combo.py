# from itertools import permutations
#
# line = input()
# result = list(permutations(list(line)))
# for ele in result:
#     print(''.join(ele))
from collections import deque


def permutation(chars, count=0):
    if count == len(chars):
        print(''.join(chars), end=' ')
        return
    for i in range(count, len(chars)):
        chars[i], chars[count] = chars[count], chars[i]
        permutation(chars, count + 1)

line = list('abc')
permutation(line)
