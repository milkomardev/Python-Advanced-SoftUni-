SIZE = 6

p1, p2 = input().split(', ')

matrix = [input().split() for _ in range(SIZE)]
turn = 0
p1_w = False
p2_w = False

while True:
    coordinates = [int(x) for x in input() if x.isdigit()]
    turn += 1
    if turn % 2 != 0:
        current_player, waiting_player = p1, p2
        if p1_w:
            p1_w = False
            continue
    else:
        current_player, waiting_player = p2, p1
        if p2_w:
            p2_w = False
            continue

    if matrix[coordinates[0]][coordinates[1]] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[coordinates[0]][coordinates[1]] == 'T':
        print(f"{current_player} is out of the game! The winner is {waiting_player}.")
        break
    elif matrix[coordinates[0]][coordinates[1]] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        if current_player == p1:
            p1_w = True
        elif current_player == p2:
            p2_w = True
