rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
flattened_matrix = [num for row in matrix for num in row]

print(flattened_matrix)