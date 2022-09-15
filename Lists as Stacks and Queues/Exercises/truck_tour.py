from collections import deque

n = int(input())

queue = deque()

for _ in range(n):
    info = [int(x) for x in input().split()]
    queue.append(info)

for attempt in range(n):
    failed = False
    tank = 0

    for fuel, distance in queue:
        tank += fuel

        if distance > tank:
            failed = True
            break

        tank -= distance

    if failed:
        queue.append(queue.popleft())
    else:
        print(attempt)
        break

