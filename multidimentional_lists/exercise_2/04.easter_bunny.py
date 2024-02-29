def is_valid_position(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())

board = []
bunny_position = []
best_direction = None

max_sum = 0
eggs_positions = []


for row in range(size):
    inner_list = [x for x in input().split()]
    board.append(inner_list)

    if 'B' in inner_list:
        bunny_position = (row, inner_list.index("B"))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for direction, positions in directions.items():
    eggs_sum = 0
    new_row, new_col = [bunny_position[0] + directions[direction][0], bunny_position[1] + directions[direction][1]]
    current_eggs_positions = []

    while is_valid_position(new_row, new_col):

        if board[new_row][new_col] == 'X':
            break

        eggs_sum += int(board[new_row][new_col])
        current_eggs_positions.append([new_row, new_col])

        new_row += positions[0]
        new_col += positions[1]

    if eggs_sum >= max_sum:
        max_sum = eggs_sum
        best_direction = direction
        eggs_positions = current_eggs_positions


print(best_direction)
print(*eggs_positions, sep='\n')
print(max_sum)