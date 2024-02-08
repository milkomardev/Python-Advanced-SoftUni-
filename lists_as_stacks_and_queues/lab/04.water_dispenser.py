from collections import deque

water = int(input())
queue = deque()
name = input()

while name != 'Start':
    queue.append(name)
    name = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        if int(data[0]) <= water:
            print(f"{queue.popleft()} got water")
            water -= int(data[0])
        else:
            print(f"{queue.popleft()} must wait")
    else:
        water += int(data[1])
    command = input()

print(f"{water} liters left")