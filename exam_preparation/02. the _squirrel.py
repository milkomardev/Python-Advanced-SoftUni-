def is_valid_index(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = input().split(', ')

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

field = []
squirrel_pos = []
collected_nuts = 0

for row in range(size):
    field.append(list(input()))
    if 's' in field[row]:
        squirrel_pos = [row, field[row].index('s')]

for command in commands:
    next_pos = directions[command](*squirrel_pos)
    squirrel_pos = next_pos
    if not is_valid_index(next_pos[0], next_pos[1]):
        print("The squirrel is out of the field.")
        break

    if field[next_pos[0]][next_pos[1]] == 'h':
        collected_nuts += 1
        field[next_pos[0]][next_pos[1]] = '*'
        if collected_nuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break

    elif field[next_pos[0]][next_pos[1]] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break

else:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {collected_nuts}')