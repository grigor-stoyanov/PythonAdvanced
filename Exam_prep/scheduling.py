job_times = [(int(index), int(value)) for index, value in enumerate(input().split(', '))]
job_index = int(input())
job_times = list(sorted(job_times, key=lambda x: (x[1])))
time = 0
for idx, ele in job_times:
    time += ele
    if idx == job_index:
        break
print(time)