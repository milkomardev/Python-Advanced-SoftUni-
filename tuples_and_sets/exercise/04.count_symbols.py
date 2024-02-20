char_count = {}

for char in input():
    if char not in char_count:
        char_count[char] = 0

    char_count[char] += 1

for char, count in sorted(char_count.items()):
    print(f"{char}: {count} time/s")