nums = list(map(int, input().split(', ')))
positive = [str(num) for num in nums if num >= 0]
negative = [str(num) for num in nums if num < 0]
even = [str(num) for num in nums if num % 2 == 0]
odd = [str(num) for num in nums if num % 2 == 1]
print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')
