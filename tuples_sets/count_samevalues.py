nums = tuple([float(ele) for ele in input().split()])
result = {}
for num in nums:
    if num not in result:
        result[num] = 1
    result[0] += 1

# for num in nums:
#     result[num] = nums.count(num)

[print(f'{key} - {value}') for key, value in result.items()]
