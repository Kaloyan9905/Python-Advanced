from collections import deque

names = deque(input().split())
n = int(input())

while len(names) > 1:
    names.rotate(-n)
    print(f"Removed {names.pop()}")

print(f"Last is {names.popleft()}")