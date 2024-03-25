from collections import deque

jobs = deque([int(x) for x in input().split(', ')])
index = int(input())

job_of_interest = jobs[index]

iterations = 0

for order in range(index):
    if jobs[order] == job_of_interest:
        iterations += 1

total = 0

while jobs:
    current_job = min(jobs)
    total += current_job
    jobs.remove(current_job)
    if current_job == job_of_interest and iterations > 0:
        iterations -= 1
    elif current_job==job_of_interest and iterations == 0:
        break


print(total)
