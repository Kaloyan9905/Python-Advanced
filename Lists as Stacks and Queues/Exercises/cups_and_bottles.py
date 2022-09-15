from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0

while cups and bottles:

    if bottles[-1] >= cups[0]:
        wasted_water += bottles.pop() - cups.popleft()
    else:
        cups[0] -= bottles.pop()

if not cups and bottles:
    print(f"Bottles: {''.join([str(bottle) for bottle in bottles])}")
else:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")

print(f"Wasted litters of water: {wasted_water}")
