from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
calc_symbols = deque(input().split())

honey_made = 0

functions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_bee > curr_nectar:
        bees.appendleft(curr_bee)
        continue
    elif curr_bee < curr_nectar:
        symbol = calc_symbols.popleft()
        honey_made += abs(functions[symbol](curr_bee, curr_nectar))

print(f"Total honey made: {honey_made}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")