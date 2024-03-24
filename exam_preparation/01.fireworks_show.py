from collections import deque

fireworks = deque([int(x) for x in input().split(', ')])
explosive = deque([int(x) for x in input().split(', ')])

created_fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0, }
perfect = False

while fireworks and explosive:
    firework = fireworks.popleft()
    if firework <= 0:
        continue

    power = explosive.pop()
    if power <= 0:
        fireworks.appendleft(firework)
        continue

    total = power + firework

    if total % 3 == 0 and total % 5 != 0:
        created_fireworks['Palm Fireworks'] += 1
    elif total % 3 != 0 and total % 5 == 0:
        created_fireworks['Willow Fireworks'] += 1
    elif total % 3 == 0 and total % 5 == 0:
        created_fireworks['Crossette Fireworks'] += 1
    else:
        firework -= 1
        fireworks.append(firework)
        explosive.append(power)
    if created_fireworks['Palm Fireworks'] >= 3 and created_fireworks['Willow Fireworks'] >= 3 \
            and created_fireworks['Crossette Fireworks'] >= 3:
        perfect = True
        break

if perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosive:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive])}")

for name, count in created_fireworks.items():
    print(f"{name}: {count}")
