from collections import deque


def perfect_show(dict):
    for key, value in dict.items():
        if value < 3:
            return False
    return True


fireworks = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
perfect_firework_show = False

while fireworks and explosive_power:

    if perfect_show(fireworks_dict):
        perfect_firework_show = True
        break

    firework = fireworks.popleft()
    explosive = explosive_power.pop()

    result = firework + explosive

    if firework <= 0 and explosive <= 0:
        continue

    if firework <= 0:
        explosive_power.append(explosive)
        continue

    if explosive <= 0:
        fireworks.appendleft(firework)
        continue

    if result % 3 == 0 and not result % 5 == 0:
        fireworks_dict["Palm Fireworks"] += 1
        continue

    if result % 5 == 0 and not result % 3 == 0:
        fireworks_dict["Willow Fireworks"] += 1
        continue

    if result % 3 == 0 and result % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1
        continue

    fireworks.append(firework - 1)
    explosive_power.append(explosive)

if perfect_show(fireworks_dict):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power if explosive_power)}")

print(f"Palm Fireworks: {fireworks_dict['Palm Fireworks']}")
print(f"Willow Fireworks: {fireworks_dict['Willow Fireworks']}")
print(f"Crossette Fireworks: {fireworks_dict['Crossette Fireworks']}")
