<<<<<<< HEAD
from collections import deque
water_qty = int(input())
thirsty_que = deque()
thirsty = input()
while not thirsty == 'Start':
    thirsty_que.append(thirsty)
    thirsty = input()
commands = input()
while not commands == 'End':
    command, *liters = commands.split()
    if command == 'refill':
        water_qty += int(liters[0])
        commands = input()
        continue
    req_water = int(command)
    if water_qty >= req_water:
        water_qty -= req_water
        print(f'{thirsty_que.popleft()} got water')
    else:
        print(f'{thirsty_que.popleft()} must wait')
    commands = input()
=======
from collections import deque
water_qty = int(input())
thirsty_que = deque()
thirsty = input()
while not thirsty == 'Start':
    thirsty_que.append(thirsty)
    thirsty = input()
commands = input()
while not commands == 'End':
    command, *liters = commands.split()
    if command == 'refill':
        water_qty += int(liters[0])
        commands = input()
        continue
    req_water = int(command)
    if water_qty >= req_water:
        water_qty -= req_water
        print(f'{thirsty_que.popleft()} got water')
    else:
        print(f'{thirsty_que.popleft()} must wait')
    commands = input()
>>>>>>> 7e8381d627bc725b2be27de4d386243fc039cd29
print(f'{water_qty} liters left.')