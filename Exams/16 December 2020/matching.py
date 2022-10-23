from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue

    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        males.pop(0)
        continue

    if female % 25 == 0:
        females.popleft()
        continue

    if not male == female:
        males.append(male - 2)
        continue

    matches += 1

males.reverse()

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")