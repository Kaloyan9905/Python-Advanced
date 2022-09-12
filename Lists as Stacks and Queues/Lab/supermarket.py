from collections import deque

name = input()
deque = deque()
paid = False
waiting_people = 0

while name != "End":

    if name == "Paid":
        for _ in range(len(deque)):
            print(deque.popleft())
    else:
        deque.append(name)

    name = input()

print(f"{len(deque)} people remaining.")