from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male = males.pop()

    if male <= 0:
        continue
    elif male % 25 == 0:
        males.pop()
        continue

    female = females.popleft()

    if female <= 0:
        males.append(male)
        continue
    elif female % 25 == 0:
        females.pop()
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
