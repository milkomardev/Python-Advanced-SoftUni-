rows, cols = [int(x) for x in input().split(', ')]

# matrix = []
matrix2 = [[int(x) for x in input().split(', ')] for r in range(rows)]
number_sum = 0

# for row in range(rows):
#     inner_list = [int(x) for x in input().split(', ')]
#     matrix.append(inner_list)
#     number_sum += sum(inner_list)

print(number_sum)
print(matrix2)

