from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

task_done = False

while materials and magic_level:

    material = materials.pop()
    magic = magic_level.popleft()

    result = magic * material

    if result == 150:
        toys["Doll"] += 1
    elif result == 250:
        toys["Wooden train"] += 1
    elif result == 300:
        toys["Teddy bear"] += 1
    elif result == 400:
        toys["Bicycle"] += 1
    else:
        if result < 0:
            materials.append(magic + material)
        elif result > 0:
            materials.append(material + 15)
        else:
            if material == 0 and magic == 0:
                continue
            elif material == 0:
                magic_level.appendleft(magic)
            else:
                materials.append(material)

if materials:
    materials.reverse()

if toys["Doll"] and toys["Wooden train"] or toys["Teddy bear"] and toys["Bicycle"]:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

reworked_dict = sorted(toys.items(), key=lambda x: x[0])

for key, value in reworked_dict:
    if value:
        print(f"{key}: {value}")
