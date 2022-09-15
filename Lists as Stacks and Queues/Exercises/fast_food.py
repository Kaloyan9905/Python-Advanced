from collections import deque

food = int(input())
orders_deque = deque(map(int, input().split()))

biggest_order = max(orders_deque)

while food and orders_deque:
    order = orders_deque.popleft()

    if food >= order:
        food -= order
        continue

    orders_deque.appendleft(order)
    break

print(biggest_order)

if not orders_deque:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders_deque)}")

