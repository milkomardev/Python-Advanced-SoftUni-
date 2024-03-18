def is_valid_position(row, col):
    return 0 <= row < rows and 0 <= col < cols and playground[row][col] != 'O'


rows, cols = [int(x) for x in input().split()]

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

playground = []
moves = 0
players_touched = 0
blind_pos = []

for row in range(rows):
    playground.append(input().split())
    if 'B' in playground[row]:
        blind_pos = [row, playground[row].index('B')]

command = input()
while command != 'Finish':
    new_pos = directions[command](*blind_pos)

    if is_valid_position(new_pos[0], new_pos[1]):
        moves += 1
        if playground[new_pos[0]][new_pos[1]] == 'P':
            players_touched += 1
            playground[new_pos[0]][new_pos[1]] = '-'
            if players_touched == 3:
                break
        blind_pos = new_pos
    command = input()

print('Game over!')
print(f"Touched opponents: {players_touched} Moves made: {moves}")