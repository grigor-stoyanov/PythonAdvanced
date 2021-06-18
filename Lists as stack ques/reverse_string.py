text = input()

stack = []
for ch in text:
    stack.append(ch)
result = ''
while stack:
    result += stack.pop()
print(result)