from collections import deque

food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

for o in range(len(orders)):
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print('Orders complete')
