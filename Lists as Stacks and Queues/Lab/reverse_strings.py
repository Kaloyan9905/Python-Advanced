from collections import deque

string = input().split()

deque = deque()

for word in string:
    word = word[::-1]
    deque.appendleft(word)

print(*deque)
