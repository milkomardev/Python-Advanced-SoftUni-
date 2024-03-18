directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

field = []
submarine_pos = []

for row in range(int(input())):
    field.append(list(input()))
    if 'S' in field[row]:
        submarine_pos = [row, field[row].index('S')]

ships_hit = 0
mines_hit = 0
field[submarine_pos[0]][submarine_pos[1]] = '-'

while True:
    command = input()
    new_pos = directions[command](*submarine_pos)
    submarine_pos = new_pos

    if field[new_pos[0]][new_pos[1]] == 'C':
        ships_hit += 1
        field[new_pos[0]][new_pos[1]] = '-'
        if ships_hit == 3:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            field[new_pos[0]][new_pos[1]] = 'S'
            break
    elif field[new_pos[0]][new_pos[1]] == '*':
        mines_hit += 1
        field[new_pos[0]][new_pos[1]] = '-'
        if mines_hit == 3:
            field[new_pos[0]][new_pos[1]] = 'S'
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{new_pos[0]}, {new_pos[1]}]!')
            break

[print(''.join(row)) for row in field]