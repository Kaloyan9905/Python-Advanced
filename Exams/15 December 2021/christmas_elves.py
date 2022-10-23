from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

counter = 0
toys = 0
energy = 0

while elfs_energy and materials:
    elf = elfs_energy.popleft()
    material = materials.pop()

    if elf < 5:
        materials.append(material)
        continue

    counter += 1

    needs_break = False
    created_two_toys = False

    if counter % 3 == 0:
        if elf >= material * 2:
            toys += 2
            energy += material * 2
            elf -= material * 2
            elfs_energy.append(elf + 1)
            created_two_toys = True
        else:
            needs_break = True

    elif counter % 5 == 0:
        if elf >= material:
            elf -= material
            energy += material
        else:
            needs_break = True

    else:
        if elf >= material:
            toys += 1
            energy += material
            elf -= material
            elfs_energy.append(elf + 1)
        else:
            needs_break = True

    if counter % 5 == 0 and created_two_toys:
        toys -= 2

    if needs_break:
        elfs_energy.append(elf * 2)
        materials.append(material)


print(f"Toys: {toys}")
print(f"Energy: {energy}")

if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")

if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
