from collections import deque


num_pumps = int(input())
pumps_que = deque()
for i in range(num_pumps):
    pump_stats = [int(ele) for ele in input().split()]
    pumps_que.append({'id': i, 'petrol': pump_stats[0], 'distance': pump_stats[1]})
tank = 0
pump_no = 0
completed_tour = False
tours = 0
while tours < num_pumps:
    tank += pumps_que[0].get('petrol')
    if tank >= pumps_que[0].get('distance'):
        pump_no += 1
        tank -= pumps_que[0].get('distance')
        pumps_que.append(pumps_que.popleft())
        if pump_no == num_pumps:
            completed_tour = True
            break
    else:
        pump_no = 0
        tank = 0
        pumps_que.append(pumps_que.popleft())
        tours += 1

if completed_tour:
    print(pumps_que[0].get('id'))
#
# n = int(input())
# stations = deque()
# for station_id in range(n):
#     stations.append([station_id, input()])
# tank = 0
# completed_tour = True
# for i in range(0, n):
#     for j in range(0, n):
#         pump = stations[i]
#         petrol, distance = list(map(int, pump[1].split()))
#         tank += petrol
#         if tank >= distance:
#             tank -= distance
#             stations.rotate(-1)
#         else:
#             completed_tour = False
#             stations.append(pump)
#             tank = 0
#             break
#         completed_tour = True
#         stations.append(pump)
#     if completed_tour:
#         break
# if completed_tour:
#     print(stations[0][0])