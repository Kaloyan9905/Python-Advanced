from collections import deque

water = int(input())
name = input()

people = deque()

while name != "Start":
    people.append(name)

    name = input()

while True:
    command = input()

    if command == "End":
        break

    if "refill" in command:
        water += int(command.split()[1])
        continue

    if water >= int(command):
        print(f"{people.popleft()} got water")
        water -= int(command)
        continue

    print(f"{people.popleft()} must wait")

print(f"{water} liters left")
