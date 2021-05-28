<<<<<<< HEAD
num_query = int(input())
stack = []
for _ in range(num_query):
    query, *element = [int(ele) for ele in input().split()]
    if query == 1:
        stack.append(element[0])
    elif query == 2:
        if stack:
            stack.pop()
    elif query == 3:
        print(max(stack))
    else:
        print(min(stack))
print(*[stack.pop() for i in range(len(stack))], sep=', ')
=======
num_query = int(input())
stack = []
for _ in range(num_query):
    query, *element = [int(ele) for ele in input().split()]
    if query == 1:
        stack.append(element[0])
    elif query == 2:
        if stack:
            stack.pop()
    elif query == 3:
        print(max(stack))
    else:
        print(min(stack))
print(*[stack.pop() for i in range(len(stack))], sep=', ')
>>>>>>> 7e8381d627bc725b2be27de4d386243fc039cd29
