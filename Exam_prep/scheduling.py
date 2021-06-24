from collections import deque

job_times = [(int(index), int(value)) for index, value in enumerate(input().split(', '))]
job_index = int(input())
job_times = deque(sorted(job_times, key=lambda x: (x[1])))
time = 0
while job_times:
    index, value = job_times.popleft()
    time += value
    if index == job_index:
        break
print(time)
