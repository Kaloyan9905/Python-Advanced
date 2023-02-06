from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()

    result = caffeine * drink

    if result <= 300 - total_caffeine:
        total_caffeine += result
        continue

    energy_drinks.append(drink)
    total_caffeine -= 30

    if total_caffeine < 0:
        total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")

