from collections import deque

bees = deque([int(x) for x in input().split()])
total_nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and total_nectar:

    bee = bees.popleft()
    nectar = total_nectar.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    symbol = symbols.popleft()
    result = 0

    if symbol == "+":
        result = abs(bee + nectar)
    elif symbol == "-":
        result = abs(bee - nectar)
    elif symbol == "*":
        result = abs(bee * nectar)
    elif symbol == "/" and nectar > 0:
        result = abs(bee / nectar)

    total_honey += result

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if total_nectar:
    print(f"Nectar left: {', '.join(str(x) for x in total_nectar)}")
