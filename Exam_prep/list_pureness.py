from collections import deque


def best_list_pureness(numbers, k):
    data = {}
    numbers = deque(numbers)

    for rotation in range(k + 1):
        if rotation == len(numbers):
            break
        result = sum([index * number for index, number in enumerate(numbers)])
        data.update({rotation: result})
        numbers.appendleft(numbers.pop())

    max_pureness = max(data.values())
    for key, val in data.items():
        if max_pureness == val:
            return f"Best pureness {val} after {key} rotations"


# from collections import deque
#
#
# def best_list_pureness(ll, k, counter=0, ll_sum=[]):
#     if k and not counter==len(ll):
#         ll = deque(ll)
#         ll_sum.append((sum([index * ele for index, ele in enumerate(ll)]), counter))
#         ll.rotate()
#         return best_list_pureness(ll, k - 1, counter + 1)
#     else:
#         ll_sum = sorted(ll_sum, key=lambda x: (-x[0], x[1]))
#         return f'Best pureness {ll_sum[0][0]} after {ll_sum[0][1]} rotations'
#

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
