rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_submatrix_sum = float('-inf')
max_submatrix_els = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_list = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]]
        second_list = [matrix[row+1][col], matrix[row+1][col + 1], matrix[row+1][col + 2]]
        third_list = [matrix[row+2][col], matrix[row+2][col + 1], matrix[row+2][col + 2]]
        submatrix_sum = sum(first_list) + sum(second_list) + sum(third_list)

        if submatrix_sum > max_submatrix_sum:
            max_submatrix_sum = submatrix_sum
            max_submatrix_els = [first_list, second_list, third_list]

print(f"Sum = {max_submatrix_sum}")
[print(*row) for row in max_submatrix_els]