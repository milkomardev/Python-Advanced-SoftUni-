presents = int(input())
size = int(input())
matrix = []
nice_kids = 0
nice_kids_presents = 0
santa_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if 'S' in matrix[row]:
        santa_position = [row, matrix[row].index('S')]
        matrix[santa_position[0]][santa_position[1]] = '-'
    nice_kids += matrix[row].count('V')

command = input()

while command != 'Christmas morning':
    row, col = [santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]]
    santa_position = [row, col]
    if 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == 'V':
            presents -= 1
            nice_kids_presents += 1
            matrix[row][col] = '-'

        elif matrix[row][col] == 'C':
            for positions in directions.values():
                new_row, new_col = [row + positions[0], col + positions[1]]
                if matrix[new_row][new_col] == 'V':
                    presents -= 1
                    nice_kids_presents += 1
                elif matrix[new_row][new_col] == 'X':
                    presents -= 1

                matrix[new_row][new_col] = '-'

        matrix[row][col] = '-'

        if not presents or nice_kids == nice_kids_presents:
            break

    command = input()

matrix[santa_position[0]][santa_position[1]] = 'S'

if not presents and nice_kids_presents < nice_kids:
    print('Santa ran out of presents!')

[print(*row) for row in matrix]

if nice_kids_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_presents} nice kid/s.")
