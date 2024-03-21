SIZE = 5

directions = {
    'up': lambda r, c: [(r - 1) % SIZE, c],
    'down': lambda r, c: [(r + 1) % SIZE, c],
    'left': lambda r, c: [r, (c - 1) % SIZE],
    'right': lambda r, c: [r, (c + 1) % SIZE],
}

deposits = {'M': ['Metal', 0], 'W': ['Water', 0], 'C': ['Concrete', 0]}

field = []
rover_pos = []


for row in range(SIZE):
    field.append(input().split())
    if 'E' in field[row]:
        rover_pos = (row, field[row].index('E'))


for direction in input().split(', '):
    rover_pos = directions[direction](*rover_pos)
    place = field[rover_pos[0]][rover_pos[1]]

    if place in deposits:
        deposits[place][1] += 1
        print(f"{deposits[place][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    elif place == 'R':
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if all([deposits['W'][1], deposits['M'][1], deposits['C'][1]]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")