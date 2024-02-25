n = int(input())

matrix = [[x for x in input()] for j in range(n)]

symbol_to_match = input()
position = None

for row_index in range(n):
    if position:
        break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol_to_match:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f"{symbol_to_match} does not occur in the matrix")
