def is_valid_pos(row,col):
    return 0 <= row < SIZE and 0 <= col < SIZE


SIZE = 7

p1, p2 = input().split(', ')
players = {p1: [501, 0], p2: [501, 0]}

board = [input().split() for _ in range(SIZE)]
turn = 0

while players[p1][0] > 0 and players[p2][0] > 0:
    turn += 1
    if turn % 2 == 1:
        current_player = p1
        players[p1][1] += 1
    else:
        current_player = p2
        players[p2][1] += 1

    position = [int(x) for x in input().strip('(').strip(')').split(', ')]
    row = position[0]
    col = position[1]

    if not is_valid_pos(row,col):
        continue

    if board[row][col] == 'B':
        players[current_player][0] = 0
        break
    elif board[row][col].isdigit():
        players[current_player][0] -= int(board[row][col])
    elif board[row][col] == 'D':
        score = (int(board[row][0]) + int(board[row][-1]) + int(board[0][col]) + int(board[-1][col])) * 2
        players[current_player][0] -= score
    elif board[row][col] == 'T':
        score = (int(board[row][0]) + int(board[row][-1]) + int(board[0][col]) + int(board[-1][col])) * 3
        players[current_player][0] -= score

for player, points in players.items():
    if points[0] <= 0:
        print(f"{player} won the game with {points[1]} throws!")