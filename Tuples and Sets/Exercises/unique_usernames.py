n = int(input())

names_set = set()

for _ in range(n):

    name = input()
    names_set.add(name)

for name in names_set:
    print(name)