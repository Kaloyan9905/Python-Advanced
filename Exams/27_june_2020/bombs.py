from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

filled_bombs_pouch = False
counter = 0


total_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    result = effect + casing

    if result not in (40, 60, 120):
        bomb_casings.append(casing - 5)
        bomb_effects.appendleft(effect)
        continue

    if result == 40:
        total_bombs["Datura Bombs"] += 1
    elif result == 60:
        total_bombs["Cherry Bombs"] += 1
    elif result == 120:
        total_bombs["Smoke Decoy Bombs"] += 1

    for name, amount in total_bombs.items():
        if amount >= 3:
            counter += 1

    if counter == 3:
        filled_bombs_pouch = True
        break
    else:
        counter = 0

if filled_bombs_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

reworked_dict = sorted(total_bombs.items(), key=lambda x: x[0])

for key, value in reworked_dict:
    print(f"{key}: {value}")
