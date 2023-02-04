from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper_size = [int(x) for x in input().split(", ")]

box_count = 0

while eggs and paper_size:

    egg = eggs.popleft()
    paper = paper_size.pop()

    if egg == 13:
        paper_size.append(paper)
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    if egg <= 0:
        paper_size.append(paper)
        continue

    if egg + paper <= 50:
        box_count += 1
        continue

if box_count:
    print(f"Great! You filled {box_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')

if paper_size:
    print(f'Pieces of paper left: {", ".join([str(x) for x in paper_size])}')
