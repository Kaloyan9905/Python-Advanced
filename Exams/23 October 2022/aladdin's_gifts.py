from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

my_dict = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:

    material = materials.pop()
    magic = magic_level.popleft()

    result = magic + material

    if result < 100:
        if result % 2 == 0:
            material *= 2
            magic *= 3
        else:
            material *= 2
            magic *= 2

        result = magic + material

    elif result > 499:
        result /= 2

    if not 100 <= result <= 499:
        continue

    if 100 <= result <= 199:
        my_dict["Gemstone"] += 1
    elif 200 <= result <= 299:
        my_dict["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        my_dict["Gold"] += 1
    elif 400 <= result <= 499:
        my_dict["Diamond Jewellery"] += 1

if my_dict["Gemstone"] and my_dict["Porcelain Sculpture"] or \
        my_dict["Gold"] and my_dict["Diamond Jewellery"]:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

reworked_dict = sorted(my_dict.items(), key=lambda x: x[0])

for key, value in reworked_dict:
    if value:
        print(f"{key}: {value}")
