from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxi_times = deque([int(x) for x in input().split(', ')])

total_time = 0

while customers and taxi_times:

    cmr = customers.popleft()
    time = taxi_times.pop()

    if time >= cmr:
        total_time += cmr
    else:
        customers.appendleft(cmr)

if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
elif not taxi_times:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(str(x) for x in customers)}")