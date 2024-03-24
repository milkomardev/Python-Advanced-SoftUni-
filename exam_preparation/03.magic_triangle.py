def is_valid_index(c, col_size):
    return 0 <= c < col_size


def get_magic_triangle(n):
    triangle = []
    for row in range(1, n + 1):
        triangle.append([1] * row)

    for row in range(2, n):
        for col in range(len(triangle[row])):
            if is_valid_index(col-1, len(triangle[row-1])) and is_valid_index(col, len(triangle[row-1])):
                upper_left = triangle[row-1][col-1]
                upper_right = triangle[row-1][col]
                triangle[row][col] = upper_left + upper_right

    return triangle


get_magic_triangle(5)
