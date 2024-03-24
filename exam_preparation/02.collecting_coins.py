size = int(input())

directions = {
    'up': lambda r, c: ((r - 1) % size, c),
    'down': lambda r, c: ((r + 1) % size, c),
    'left': lambda r, c: (r, (c - 1) % size),
    'right': lambda r, c: (r, (c + 1) % size),
}

matrix = []
position = []
coins = 0

for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    if 'P' in matrix[row]:
        position = [row, matrix[row].index('P')]
        matrix[position[0]][position[1]] = 0

path = [[position[0], position[1]]]

while True:
    command = input()
    if command in directions:
        position = directions[command](*position)
        path.append([position[0], position[1]])
    else:
        continue

    if matrix[position[0]][position[1]] == 'X':
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break
    else:
        coins += matrix[position[0]][position[1]]
        matrix[position[0]][position[1]] = 0
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break
print('Your path:')
[print(step) for step in path]
