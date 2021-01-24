numbers = input()
stack = [int(ele) for ele in numbers.split()]
for _ in range(len(stack)):
    print(stack.pop(),end=' ')