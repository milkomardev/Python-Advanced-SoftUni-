import sys

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

max_sum_submatrix = -sys.maxsize
max_submatrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        curr_value = matrix[row][col]
        right_value = matrix[row][col + 1]
        below_value = matrix[row + 1][col]
        diagonal_value = matrix[row + 1][col + 1]
        current_sum = curr_value + right_value + below_value + diagonal_value
        if current_sum > max_sum_submatrix:
            max_sum_submatrix = current_sum
            max_submatrix = [[curr_value, right_value], [below_value, diagonal_value]]


print(*max_submatrix[0])
print(*max_submatrix[1])
print(max_sum_submatrix)