from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = deque([int(x) for x in input().split(', ')])


bombs_dict = {
    40: ['Datura Bombs', 0],
    60: ['Cherry Bombs', 0],
    120: ['Smoke Decoy Bombs', 0],
}

successful = False

while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    total = effect + casing

    if total in bombs_dict:
        bombs_dict[total][1] += 1
        if bombs_dict[40][1] >= 3 and bombs_dict[60][1] >= 3 and bombs_dict[120][1] >= 3:
            successful = True
            break

    else:
        casing -= 5
        effects.appendleft(effect)
        casings.append(casing)

if successful:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(str(e) for e in effects)}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(str(c) for c in casings)}")
else:
    print("Bomb Casings: empty")

for bomb, count in sorted(bombs_dict.values()):
    print(f"{bomb}: {count}")