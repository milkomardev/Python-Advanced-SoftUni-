def is_valid_pos(r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())
bombs = int(input())

bombs_positions = [[int(x) for x in input().strip('(').strip(')').split(', ')] for _ in range(bombs)]
matrix = []

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

for row in range(size):
    inner = []
    for col in range(size):
        if [row, col] in bombs_positions:
            inner.append('*')
        else:
            inner.append(0)
    matrix.append(inner)

for row in range(size):
    for col in range(size):
        bombs_around = 0
        if matrix[row][col] == 0:
            el_pos = [row, col]
            for direction in directions:
                next_pos = [el_pos[0] + direction[0], el_pos[1] + direction[1]]
                if is_valid_pos(next_pos[0], next_pos[1]):
                    if matrix[next_pos[0]][next_pos[1]] == '*':
                        bombs_around += 1
            matrix[row][col] = bombs_around

[print(*row) for row in matrix]