def union_values(set_1, set_2):
    return set_1.union(set_2)


def different_values(set_1, set_2):
    return set_1.difference(set_2)


def symmetric_different_values(set_1, set_2):
    return set_1.symmetric_difference(set_2)


n = int(input())

odd = set()
even = set()

for iteration in range(1, n + 1):
    name = input()
    ascii_sum = 0

    for char in name:
        ascii_sum += ord(char)

    ascii_sum //= iteration

    if ascii_sum % 2 == 0:
        even.add(ascii_sum)
        continue

    odd.add(ascii_sum)

if sum(odd) == sum(even):
    print(*union_values(odd, even), sep=", ")

elif sum(odd) > sum(even):
    print(*different_values(odd, even), sep=", ")

else:
    print(*symmetric_different_values(odd, even), sep=", ")
