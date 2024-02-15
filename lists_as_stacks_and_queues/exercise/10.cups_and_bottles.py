from collections import deque

cups = deque([int(c) for c in input().split()])
bottles = deque([int(b) for b in input().split()])

waste = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        waste += bottle-cup

    else:
        cup -= bottle
        cups.appendleft(cup)

if not cups:
    print(f"Bottles: {' '.join([str(b) for b in bottles])}")
else:
    print(f"Cups: {' '.join([str(c) for c in cups])}")

print(f"Wasted litters of water: {waste}")