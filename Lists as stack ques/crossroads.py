from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
crash_happened = False
count_crossed = 0
while True:
    cmd = input()
    if cmd == 'END':
        print(f'Everyone is safe.\n{count_crossed} total cars passed the crossroads.')
        break
    if not cmd == 'green':
        cars.append(cmd)
    else:
        total_time = green_light + free_window
        while total_time - free_window > 0 and cars:
            crossing = cars.popleft()
            for part in crossing:
                total_time -= 1
                if total_time < 0:
                    print('A crash happened!')
                    print(f'{crossing} was hit at {part}.')
                    crash_happened = True
                    break
            count_crossed += 1
    if crash_happened:
        break
