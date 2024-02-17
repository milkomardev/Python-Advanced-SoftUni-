cars = set()

for _ in range(int(input())):
    direction, car = input().split(", ")
    if direction == "IN":
        cars.add(car)
    elif direction == "OUT":
        cars.remove(car)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")