BOARD_SIZE = 8

board = []
w_pos = []
b_pos = []

for row in range(BOARD_SIZE):
    board.append(input().split())

    if 'w' in board[row]:
        w_pos.append(row)
        w_pos.append(board[row].index('w'))
    if 'b' in board[row]:
        b_pos.append(row)
        b_pos.append(board[row].index('b'))

if abs(w_pos[1] - b_pos[1]) != 1 or w_pos[0] < b_pos[0]:
    if BOARD_SIZE - 1 - w_pos[0] >= b_pos[0]:
        print(f"Game over! White pawn is promoted to a queen at {chr(97+w_pos[1])}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97+b_pos[1])}1.")
else:
    if abs(w_pos[0] - b_pos[0] - 1) % 2 == 0:
        print(f"Game over! White win, capture on {chr(97+b_pos[1])}{BOARD_SIZE -((w_pos[0] + b_pos[0])//2)}.")
    elif abs(w_pos[0] - b_pos[0] - 1) % 2 == 1:
        print(f"Game over! Black win, capture on {chr(97+w_pos[1])}{BOARD_SIZE -((w_pos[0] + b_pos[0])//2)}.")
