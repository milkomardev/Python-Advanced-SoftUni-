from collections import deque

clothes_stack = deque([int(x) for x in input().split()])
rack = int(input())

racks_needed = 1
current_rack = rack

while clothes_stack:
    cloth = clothes_stack.pop()
    if cloth <= current_rack:
        current_rack -= cloth
    else:
        racks_needed += 1
        current_rack = rack - cloth

print(racks_needed)