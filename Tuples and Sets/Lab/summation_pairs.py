from collections import deque

nums = deque([int(x) for x in input().split()])
target = int(input())

copy_nums = nums.copy()
unique_pairs = set()
iterations = 0
res = []

for first in nums:

    copy_nums.popleft()

    for second in copy_nums:

        if first + second == target:
            unique_pairs.add((first, second))
            print(f"{first} + {second} = {target}")
        iterations += 1

print(f"Iterations done: {iterations}")
for pair in unique_pairs:
    print(pair)

