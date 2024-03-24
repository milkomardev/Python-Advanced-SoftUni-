def is_valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


string = input()
size = int(input())

matrix = []
position = []

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

for row in range(size):
    matrix.append(list(input()))
    if 'P' in matrix[row]:
        position = [row, matrix[row].index('P')]
        matrix[position[0]][position[1]] = '-'

for _ in range(int(input())):
    command = input()
    new_position = directions[command](*position)

    if is_valid_index(new_position[0], new_position[1]):
        if str(matrix[new_position[0]][new_position[1]]).isalpha():
            string += str(matrix[new_position[0]][new_position[1]])
            matrix[new_position[0]][new_position[1]] = '-'
    else:
        if string:
            string = string[:-1]
            continue
    position = new_position

matrix[position[0]][position[1]] = 'P'

print(string)
[print(''.join(row)) for row in matrix]