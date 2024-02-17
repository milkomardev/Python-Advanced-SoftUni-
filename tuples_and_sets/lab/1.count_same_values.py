numbers = tuple([float(x) for x in (input().split())])

nums_and_occurrences = {}

for n in numbers:
    if n not in nums_and_occurrences:
        nums_and_occurrences[n] = 1
    else:
        nums_and_occurrences[n] += 1

for number, times in nums_and_occurrences.items():
    print(f"{number} - {times} times")