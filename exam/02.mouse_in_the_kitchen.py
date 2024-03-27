def is_valid_pos(r, c):
    return 0 <= r < rows and 0 <= c < cols


directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

rows, cols = [int(x) for x in input().split(',')]

board = []
mouse_pos = []
cheese = 0

for row in range(rows):
    board.append(list(input()))
    if 'M' in board[row]:
        mouse_pos = [row, board[row].index('M')]
        board[mouse_pos[0]][mouse_pos[1]] = '*'
    if 'C' in board[row]:
        cheese += board[row].count('C')

eaten_cheese = 0

command = input()
while command != 'danger':
    new_pos = directions[command](*mouse_pos)

    if not is_valid_pos(new_pos[0], new_pos[1]):
        print('No more cheese for tonight!')
        break

    if board[new_pos[0]][new_pos[1]] == '@':
        command = input()
        continue

    mouse_pos = [new_pos[0], new_pos[1]]

    if board[new_pos[0]][new_pos[1]] == 'T':
        print('Mouse is trapped!')
        break

    elif board[new_pos[0]][new_pos[1]] == 'C':
        eaten_cheese += 1
        board[new_pos[0]][new_pos[1]] = '*'
        if eaten_cheese == cheese:
            print('Happy mouse! All the cheese is eaten, good night!')
            break

    command = input()
else:
    print('Mouse will come back later!')

board[mouse_pos[0]][mouse_pos[1]] = 'M'

[print(''.join(row)) for row in board]