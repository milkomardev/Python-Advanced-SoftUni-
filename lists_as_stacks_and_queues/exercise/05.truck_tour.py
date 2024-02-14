from collections import deque

petrol = 0
pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
index = 0
copy_pumps = pumps.copy()


while copy_pumps:
    pump_data = copy_pumps.popleft()

    petrol += pump_data[0]
    distance = pump_data[1]

    if distance > petrol:
        pumps.rotate(-1)
        copy_pumps = pumps.copy()
        petrol = 0
        index += 1
    else:
        petrol -= distance

print(index)