from collections import deque

items = {
    30: ["Patch", 0],
    40: ["Bandage", 0],
    100: ["MedKit", 0],
}

textiles = deque([int(x) for x in input().split()])
meds = deque([int(x) for x in input().split()])

while textiles and meds:
    textile = textiles.popleft()
    med = meds.pop()
    total_sum = textile + med

    if total_sum in items:
        items[total_sum][1] += 1

    elif total_sum > 100:
        items[100][1] += 1
        meds[-1] += total_sum - 100

    else:
        med += 10
        meds.append(med)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not meds:
    print("Medicaments are empty.")

[print(f"{item} - {amount}")for item, amount in sorted(items.values(), key=lambda x: (-x[1], x)) if amount]

if meds:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(meds))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
