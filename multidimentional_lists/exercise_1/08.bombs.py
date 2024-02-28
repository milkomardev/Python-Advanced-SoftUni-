from collections import deque


def is_valid_position(row, col):
    return 0 <= row < size and 0 <= col < size


def explode(bomb_row, bomb_col, bomb_value):
    for direction in directions:
        curr_cell_row, curr_cell_col = bomb_row + direction[0], bomb_col + direction[1]
        if is_valid_position(curr_cell_row, curr_cell_col):
            if matrix[curr_cell_row][curr_cell_col] > 0:
                matrix[curr_cell_row][curr_cell_col] -= bomb_value


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs_positions = deque([[int(x) for x in position.split(',')] for position in input().split()])

directions = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1),
)

while bombs_positions:
    curr_bomb_position = bombs_positions.popleft()
    bomb_value = matrix[curr_bomb_position[0]][curr_bomb_position[1]]
    explode(curr_bomb_position[0], curr_bomb_position[1], bomb_value)

alive_cells = [el for x in matrix for el in x if el > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*r) for r in matrix]
