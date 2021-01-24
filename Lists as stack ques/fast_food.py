from collections import deque

qty_food = int(input())
orders_que = deque(int(ele) for ele in input().split())
print(max(orders_que))
while qty_food - orders_que[0] >= 0 and orders_que:
    qty_food -= orders_que.popleft()
if orders_que:
    print('Orders left: ', end='')
    print(*list(orders_que), sep=', ')
else:
    print("Orders complete")
