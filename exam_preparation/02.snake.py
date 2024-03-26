def is_valid_pos(r, c):
    return 0 <= r < size and 0 <= c < size

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

size = int(input())
matrix = []
snake_pos = []
food = 0

for row in range(size):
    matrix.append(list(input()))
    if 'S' in matrix[row]:
        snake_pos = [row, matrix[row].index('S')]
        matrix[snake_pos[0]][snake_pos[1]] = '.'


while food < 10:
    command = input()
    next_pos = directions[command](*snake_pos)
    snake_pos = [next_pos[0], next_pos[1]]

    if not is_valid_pos(next_pos[0], next_pos[1]):
        break

    if matrix[next_pos[0]][next_pos[1]] == '*':
        food += 1

    elif matrix[next_pos[0]][next_pos[1]] == 'B':
        matrix[next_pos[0]][next_pos[1]] = '.'
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 'B':
                    snake_pos = [row, col]

    matrix[snake_pos[0]][snake_pos[1]] = '.'


if food == 10:
    matrix[snake_pos[0]][snake_pos[1]] = 'S'
    print('You won! You fed the snake.')
else:
    print('Game over!')
print(f"Food eaten: {food}")
[print(''.join(row)) for row in matrix]



