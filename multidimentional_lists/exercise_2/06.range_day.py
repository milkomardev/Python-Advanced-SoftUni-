SIZE = 5
matrix = []
player_pos = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

targets = 0
targets_hit = 0
targets_hit_pos = []

for row in range(SIZE):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        player_pos = [row, matrix[row].index('A')]

    targets += matrix[row].count('x')

all_shot = False

for _ in range(int(input())):
    command = input().split()
    direction = command[1]

    if command[0] == 'move':
        steps = int(command[2])
        row = player_pos[0] + (directions[direction][0] * steps)
        col = player_pos[1] + (directions[direction][1] * steps)
        if 0 <= row < SIZE and 0 <= col < SIZE:
            if not matrix[row][col] == 'x':
                player_pos = [row, col]

    elif command[0] == 'shoot':
        row = player_pos[0] + directions[direction][0]
        col = player_pos[1] + directions[direction][1]
        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets_hit += 1
                targets_hit_pos.append([row, col])
                if targets == targets_hit:
                    print(f"Training completed! All {targets_hit} targets hit.")
                    all_shot = True
                break
            row += directions[direction][0]
            col += directions[direction][1]

    if all_shot:
        break

if targets > targets_hit:
    print(f"Training not completed! {targets - targets_hit} targets left.")

[print(x) for x in targets_hit_pos]