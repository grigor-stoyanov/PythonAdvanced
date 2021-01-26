n = int(input())
intersection = set()
range1 = set()
range2 = set()
max_len = 0
max_intersection = set()
for _ in range(n):
    nums1, nums2 = input().split('-')
    range1 = set(range(list(map(int, nums1.split(',')))[0], list(map(int, nums1.split(',')))[1]+1))
    range2 = set(range(list(map(int, nums2.split(',')))[0], list(map(int, nums2.split(',')))[1]+1))
    if len(range1&range2) > max_len:
        max_len = len(range1&range2)
        max_intersection = range1&range2
print(f'longest intersection is {list(max_intersection)} with length {max_len}')
