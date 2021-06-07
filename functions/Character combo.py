# from itertools import permutations
#
# line = input()
# result = list(permutations(list(line)))
# for ele in result:
#     print(''.join(ele))

def permutation(chars, current_chars=[]):
    if not chars:
        return
    permutation(chars[1:],)


line = list('abc')
permutation(line)