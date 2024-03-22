directions = {
    "up": lambda r, c: [(r - 1) % rows, c],
    "down": lambda r, c: [(r + 1) % rows, c],
    "left": lambda r, c: [r, (c - 1) % cols],
    "right": lambda r, c: [r, (c + 1) % cols],
}

rows, cols = [int(x) for x in input().split(', ')]

matrix = []
my_pos = []
items = {
    "D": ['Christmas decorations', 0, 0],
    "G": ['Gifts', 0, 0],
    "C": ['Cookies', 0, 0],
}
for row in range(rows):
    matrix.append(input().split())
    if 'Y' in matrix[row]:
        my_pos = [row, matrix[row].index('Y')]
    if 'D' in matrix[row]:
        items['D'][1] += matrix[row].count('D')
    if 'G' in matrix[row]:
        items['G'][1] += matrix[row].count('G')
    if 'C' in matrix[row]:
        items['C'][1] += matrix[row].count('C')

matrix[my_pos[0]][my_pos[1]] = 'x'

command = input()
all_collected = False
while command != 'End':
    direction, steps = command.split('-')
    steps = int(steps)

    for step in range(steps):
        new_pos = directions[direction](*my_pos)
        my_pos = new_pos
        if matrix[new_pos[0]][new_pos[1]] in items:
            items[matrix[new_pos[0]][new_pos[1]]][2] += 1
            items[matrix[new_pos[0]][new_pos[1]]][1] -= 1
        matrix[my_pos[0]][my_pos[1]] = 'x'
        if items['D'][1] == 0 and items['C'][1] == 0 and items['G'][1] == 0:
            print("Merry Christmas!")
            all_collected = True
            break
    if all_collected:
        break
    command = input()

matrix[my_pos[0]][my_pos[1]] = 'Y'

print("You've collected:")
for item, *data in items.values():
    print(f"- {data[1]} {item}")

[print(' '.join(row)) for row in matrix]