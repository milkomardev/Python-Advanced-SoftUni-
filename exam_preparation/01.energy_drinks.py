from collections import deque

caffeine_mg = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])

MAXIMUM_CAFFEINE = 300
stamat_caffeine = 0

while caffeine_mg and energy_drinks:
    caffeine = caffeine_mg.pop()
    drink = energy_drinks.popleft()
    current_caf = caffeine * drink

    if current_caf + stamat_caffeine <= MAXIMUM_CAFFEINE:
        stamat_caffeine += current_caf

    else:
        energy_drinks.append(drink)
        stamat_caffeine = max(stamat_caffeine-30, 0)

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")