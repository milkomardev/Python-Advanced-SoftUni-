directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

size = int(input())
car = int(input())

matrix = [input().split() for _ in range(size)]

car_pos = [0, 0]
kilometers = 0

command = input()
while command != "End":
    car_pos = directions[command](*car_pos)
    kilometers += 10

    if matrix[car_pos[0]][car_pos[1]] == 'F':
        print(f"Racing car {car} finished the stage!")
        break

    elif matrix[car_pos[0]][car_pos[1]] == 'T':
        kilometers += 20
        matrix[car_pos[0]][car_pos[1]] = '.'
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 'T':
                    car_pos = [row, col]
                    matrix[car_pos[0]][car_pos[1]] = '.'
                    continue
    command = input()
else:
    print(f"Racing car {car} DNF.")

matrix[car_pos[0]][car_pos[1]] = 'C'

print(f"Distance covered {kilometers} km.")
[print(''.join(el)) for el in matrix]
