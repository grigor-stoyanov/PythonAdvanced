<<<<<<< HEAD
from collections import deque
from datetime import datetime, timedelta

line = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')
robot_que = deque([{'name': ele.split('-')[0], 'time': int(ele.split('-')[1]), 'available': time} for ele in line])
products = deque()
isRobotFree = True
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
while products:
    time += timedelta(seconds=1)
    current_product = products.popleft()
    for i in range(0, len(robot_que)):
        current_robot = robot_que.popleft()
        if current_robot.get('available') <= time:
            print(current_robot.get('name') + ' - ' + current_product + time.strftime(' [%H:%M:%S]'))
            current_robot['available'] = time + timedelta(seconds=current_robot.get('time'))
            robot_que.append(current_robot)
            isRobotFree = True
            break
        else:
            isRobotFree = False
            robot_que.append(current_robot)
    if not isRobotFree:
=======
from collections import deque
from datetime import datetime, timedelta

line = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')
robot_que = deque([{'name': ele.split('-')[0], 'time': int(ele.split('-')[1]), 'available': time} for ele in line])
products = deque()
isRobotFree = True
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
while products:
    time += timedelta(seconds=1)
    current_product = products.popleft()
    for i in range(0, len(robot_que)):
        current_robot = robot_que.popleft()
        if current_robot.get('available') <= time:
            print(current_robot.get('name') + ' - ' + current_product + time.strftime(' [%H:%M:%S]'))
            current_robot['available'] = time + timedelta(seconds=current_robot.get('time'))
            robot_que.append(current_robot)
            isRobotFree = True
            break
        else:
            isRobotFree = False
            robot_que.append(current_robot)
    if not isRobotFree:
>>>>>>> 7e8381d627bc725b2be27de4d386243fc039cd29
        products.append(current_product)