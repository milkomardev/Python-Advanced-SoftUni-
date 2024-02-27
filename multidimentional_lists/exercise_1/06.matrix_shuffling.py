def is_valid_index(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_command(action, indices):
    if action == 'swap' and is_valid_index(indices) and len(indices) == 4:
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(r) for r in matrix], sep='\n')
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

command = input()

while command != "END":
    action, *data = [int(x) if x.isdigit() else x for x in command.split()]

    swap_command(action, data)
    command = input()


# def is_valid_index(indices):
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)
#
#
# def is_valid_command(action, indices):
#     return action == 'swap' and is_valid_index(indices) and len(indices) == 4
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)
# valid_cols = range(cols)
#
# command = input()
#
# while command != "END":
#     action, *data = [int(x) if x.isdigit() else x for x in command.split()]
#
#     if is_valid_command(action, data):
#         matrix[data[0]][data[1]], matrix[data[2]][data[3]] = matrix[data[2]][data[3]], matrix[data[0]][data[1]]
#         print(*[' '.join(r) for r in matrix], sep='\n')
#     else:
#         print('Invalid input!')
#     command = input()