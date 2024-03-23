def is_valid_index(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE

SIZE = 6

board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]
prize = [['Football', False], ['Teddy Bear', False], ['Lego Construction Set', False]]
points = 0

for throw in range(3):
    spot = [int(x) for x in input().strip('(').strip(')').split(', ')]
    if is_valid_index(spot[0], spot[1]):
        if board[spot[0]][spot[1]] == 'B':
            board[spot[0]][spot[1]] = 0
            index = spot[1]
            for row in board:
                points += row[index]

if 100 <= points <= 199:
    prize[0][1] = True
elif 200 <= points <= 299:
    prize[1][1] = True
elif 300 <= points:
    prize[2][1] = True

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    print(f"Good job! You scored {points} points, and you've won {''.join([p[0] for p in prize if p[1] == True])}.")