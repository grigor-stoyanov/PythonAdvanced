line = list(map(int, input().split()))
negative = filter(lambda x: True if x < 0 else False, line)
positive = filter(lambda x: True if x > 0 else False, line)
negative = abs(sum(negative))
positive = sum(positive)
print(f"{-negative}\n{positive}")
if negative > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")