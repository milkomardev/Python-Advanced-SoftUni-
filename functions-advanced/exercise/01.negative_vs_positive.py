def print_numbers(positive, negative):
    print(sum(negative))
    print(sum(positive))

    if abs(sum(positive)) > abs(sum(negative)):
        print("The positives are stronger than the negatives")
    else:
        print('The negatives are stronger than the positives')


numbers = [int(x) for x in input().split()]
positive = [x for x in numbers if x > 0]
negative = [x for x in numbers if x < 0]

print_numbers(positive, negative)