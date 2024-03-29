def numbers_searching(*args):
    start_number = min(args)
    end_number = max(args)
    missing_numbers = []
    dup_numbers = []

    for n in range(start_number, end_number + 1):
        if n not in args:
            missing_numbers.append(n)
        elif args.count(n) > 1:
            dup_numbers.append(n)

    return [missing_numbers[-1], dup_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
