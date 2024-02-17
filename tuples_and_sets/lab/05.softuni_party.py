reservations = set()

for _ in range(int(input())):
    reservation = input()
    reservations.add(reservation)

guest = input()

while guest != "END":
    reservations.remove(guest)
    guest = input()

filtered_list = sorted(reservations)

print(len(filtered_list))
print("\n".join(filtered_list))
