n = int(input())

longest_intersection = []

for _ in range(n):
    info = input().split("-")

    first_set = set()
    second_set = set()

    first_start, first_end = [int(x) for x in info[0].split(",")]
    second_start, second_end = [int(x) for x in info[1].split(",")]

    for number in range(first_start, first_end + 1):
        first_set.add(number)

    for number in range(second_start, second_end + 1):
        second_set.add(number)

    result = first_set.intersection(second_set)

    if len(result) > len(longest_intersection):
        longest_intersection = result

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] \
with length {len(longest_intersection)}")



