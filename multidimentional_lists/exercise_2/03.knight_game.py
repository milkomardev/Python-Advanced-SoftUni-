def hit_horses(row, col):
    damage = 0
    for direction in directions:
        current_row, current_col = row + direction[0], col + direction[1]
        if 0 <= current_row < size and 0 <= current_col < size:
            if matrix[current_row][current_col] == 'K':
                damage += 1
    return damage


size = int(input())

matrix = [[x for x in input()] for _ in range(size)]

removed_knights = 0

directions = {
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1),
}

while True:
    max_dmg_knight = 0
    max_dmg_knight_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                current_dmg = hit_horses(row, col)
                if current_dmg > max_dmg_knight:
                    max_dmg_knight = current_dmg
                    max_dmg_knight_position = row, col

    if max_dmg_knight_position:
        matrix[max_dmg_knight_position[0]][max_dmg_knight_position[1]] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)