import math
from collections import deque

line = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
result = []

while line:

    first = line.popleft()
    second = line.pop() if line else ""

    color = first + second

    if color in main_colors or color in secondary_colors:
        result.append(color)
        continue

    color = second + first

    if color in main_colors or color in secondary_colors:
        result.append(color)
        continue

    first = first[:-1]
    second = second[:-1]

    half = len(line) // 2

    if first:
        line.insert(half, first)
    if second:
        line.insert(half, second)

final_colors = []

for color in result:

    if color in main_colors:
        final_colors.append(color)
    else:

        if color == "orange":
            if "red" in result and "yellow" in result:
                final_colors.append(color)
        elif color == "purple":
            if "blue" in result and "red" in result:
                final_colors.append(color)
        else:
            if "blue" in result and "yellow" in result:
                final_colors.append(color)

print(final_colors)
