rows = int(input())

matrix = [[int(j) for j in input().split(',') if int(j) % 2 == 0] for i in range(rows)]
# matrix = []

# for row in range(rows):
#     inner_list = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
#     matrix.append(inner_list)

print(matrix)
