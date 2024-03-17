from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = deque(int(x) for x in input().split())

total_energy_used = 0
total_toys_created = 0
index = 0

while elves and boxes:
    elf = elves.popleft()

    if elf < 5:
        continue

    index += 1
    material = boxes[-1]
    current_toys_created = 0

    if index % 3 == 0:
        material *= 2
        current_toys_created += 1

    if elf >= material:
        total_energy_used += material
        elf -= material
        if index % 5 == 0:
            current_toys_created = 0
        else:
            current_toys_created += 1
            elf += 1
        total_toys_created += current_toys_created
        boxes.pop()
    else:
        elf *= 2

    elves.append(elf)

print(f'Toys: {total_toys_created}')
print(f'Energy: {total_energy_used}')

if elves:
    print(f'Elves left: {", ".join(str(x) for x in elves)}')
if boxes:
    print(f'Boxes left: {", ".join(str(x) for x in boxes)}')