def is_valid_position(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())
alice_pos = []
matrix = []

for row in range(size):
    matrix.append([x for x in input().split()])
    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = '*'


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

tea_bags = 0

while True:
    command = input()
    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]
    alice_pos = [row, col]

    if not is_valid_position(row, col):
        print("Alice didn't make it to the tea party.")
        break

    elif matrix[row][col] == 'R':
        print("Alice didn't make it to the tea party.")
        matrix[row][col] = '*'
        break

    elif matrix[row][col].isdigit():
        tea_bags += int(matrix[row][col])
        matrix[row][col] = '*'
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break

    matrix[row][col] = '*'


[print(*row) for row in matrix]