# def is_divisible(number):
#     divisible = [num for num in range(2, 11) if number % num == 0]
#     return True if divisible else False
#
#
end = int(input())
start = int(input())
# result = [num for num in range(start, end + 1) if is_divisible(num)]
print([num for num in range(start, end + 1) if [d for d in range(1, 11) if num % d == 0]])
# print(result)
