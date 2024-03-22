SIZE = 6

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

matrix = [input().split() for _ in range(SIZE)]
position = [int(x) for x in input() if x.isdigit()]

command = input()
while command != 'Stop':
    command_args = command.split(', ')
    action = command_args[0]
    direction = command_args[1]
    position = directions[direction](*position)
    spot = matrix[position[0]][position[1]]

    if action == 'Create':
        value = command_args[2]
        if spot == '.':
            matrix[position[0]][position[1]] = value

    elif action == 'Update':
        value = command_args[2]
        if spot != '.':
            matrix[position[0]][position[1]] = value

    elif action == 'Delete':
        if spot != '.':
            matrix[position[0]][position[1]] = '.'

    elif action == 'Read':
        if spot.isalnum():
            print(spot)

    command = input()

[print(' '.join(row)) for row in matrix]