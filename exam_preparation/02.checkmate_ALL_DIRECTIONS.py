def is_valid_pos(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = 8

board = []
k_pos = []

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

for row in range(SIZE):
    board.append(input().split())
    if 'K' in board[row]:
        k_pos = [row, board[row].index('K')]

queens = []

for direction in directions:
    new_position = [k_pos[0] + direction[0], k_pos[1] + direction[1]]

    while True:
        if is_valid_pos(new_position[0], new_position[1]):
            if board[new_position[0]][new_position[1]] == 'Q':
                queens.append([new_position[0], new_position[1]])
                break
            else:
                new_position = [new_position[0] + direction[0], new_position[1] + direction[1]]
        else:
            break

if queens:
    [print(q) for q in queens]
else:
    print('The king is safe!')
