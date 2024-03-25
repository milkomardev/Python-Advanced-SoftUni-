def best_list_pureness(list_of_numbers, number):
    max_sum = float('-inf')
    best_rotation = 0
    for rotation in range(number+1):
        total_sum = 0
        for index in range(len(list_of_numbers)):
            total_sum += index*list_of_numbers[index]

        if total_sum > max_sum:
            max_sum = total_sum
            best_rotation = rotation

        list_of_numbers.insert(0, list_of_numbers.pop(-1))

    return f"Best pureness {max_sum} after {best_rotation} rotations"


test = ([-4, -3, -2, -6], 0)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
