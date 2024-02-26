size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
primary_diagonal_sum = sum([matrix[i][i] for i in range(size)])
secondary_diagonal_sum = sum([matrix[i][size - i - 1] for i in range(size)])
print(abs(primary_diagonal_sum - secondary_diagonal_sum))