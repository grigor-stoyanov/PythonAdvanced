from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))
wasted_water = 0
while cups and bottles:
    current_cup = cups.popleft()
    while current_cup > 0 and bottles:
        current_bottle = bottles.pop()
        current_cup -= current_bottle
    if current_cup < 0:
        wasted_water += -current_cup
if not cups:
    print('Bottles: ', end='')
    print(*[bottles.pop() for i in range(len(bottles))])
else:
    print('Cups: ', end='')
    print(*[cups.popleft() for i in range(len(cups))])
print(f'Wasted litters of water: {wasted_water}')
