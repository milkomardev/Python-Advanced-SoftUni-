from collections import deque

rows, cols = [int(x) for x in input().split()]
line = list(input())

line_copy = deque(line)

for r in range(rows):
    while len(line_copy) < cols:
        line_copy.extend(line)

    if r % 2 == 0:
        print(*[line_copy.popleft() for c in range(cols)], sep='')
    else:
        print(*[line_copy.popleft() for c in range(cols)][::-1], sep='')