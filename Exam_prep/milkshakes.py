from collections import deque

# recieve integers stack and deque
chocolate = [int(ele) for ele in input().split(', ')]
milk = deque([int(ele) for ele in input().split(', ')])


milkshakes = 0
while chocolate and milk:

    # invalid chocolate case
    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    # invalid milk case
    if milk[0] <= 0 and chocolate[-1] > 0:
        milk.popleft()
        continue
    # invalid both case
    if milk[0] > 0 and chocolate[-1] <= 0:
        chocolate.pop()
        continue

    current_milk = milk.popleft()
    current_chocolate = chocolate.pop()
    # mixing
    if current_milk == current_chocolate:
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        milk.appendleft(current_milk)
        current_chocolate -= 5
        chocolate.append(current_chocolate)

# output
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


if chocolate:
    print(f'Chocolate: {", ".join(map(str,chocolate))}')
else:
    print(f'Chocolate: empty')
if milk:
    print(f'Milk: {", ".join(map(str,milk))}')
else:
    print(f'Milk: empty')

