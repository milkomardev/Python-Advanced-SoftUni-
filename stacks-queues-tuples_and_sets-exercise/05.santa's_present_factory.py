from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

value_of_toys = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted_toys = []

while materials and magic:
    material = materials.pop() if magic[0] or not materials[0] else 0
    curr_magic = magic.popleft() if material or not magic[0] else 0

    if not curr_magic:
        continue

    current_value = material * curr_magic

    if current_value in value_of_toys:
        crafted_toys.append(value_of_toys[current_value])
    elif current_value < 0:
        materials.append(material + curr_magic)
    elif current_value > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {'Teddy bear', 'Bicycle'}.issubset(crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for toy in sorted(set(crafted_toys)):
    print(f"{toy}: {crafted_toys.count(toy)}")
