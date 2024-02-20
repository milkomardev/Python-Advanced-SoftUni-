odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name_sum = (sum([ord(l) for l in input()])) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    print(*odd_set | even_set, sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set - even_set, sep=', ')
else:
    print(*odd_set ^ even_set, sep=', ')
