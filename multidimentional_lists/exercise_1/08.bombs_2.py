from collections import deque


def is_valid_position(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs_positions = deque([[int(x) for x in i.split(',')] for i in input().split()])

directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


while bombs_positions:

    curr_bomb_position = bombs_positions.popleft()
    bomb_value = matrix[curr_bomb_position[0]][curr_bomb_position[1]]

    for direction in directions:
        curr_cell_row, curr_cell_col = curr_bomb_position[0] + direction[0], curr_bomb_position[1] + direction[1]
        if is_valid_position(curr_cell_row, curr_cell_col):
            if matrix[curr_cell_row][curr_cell_col] > 0:
                matrix[curr_cell_row][curr_cell_col] -= bomb_value
    matrix[curr_bomb_position[0]][curr_bomb_position[1]] = 0

alive_cells = [el for x in matrix for el in x if el > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*r) for r in matrix]


