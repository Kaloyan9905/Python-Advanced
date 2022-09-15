from collections import deque

bullet_price = int(input())
gun_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())

curr_bullets = gun_size
used_bullets = 0

while bullets and locks:

    lock = locks.popleft()
    bullet = bullets.pop()

    if lock >= bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    curr_bullets -= 1
    used_bullets += 1

    if curr_bullets == 0 and bullets:
        print("Reloading!")
        curr_bullets = gun_size

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence - (used_bullets * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
