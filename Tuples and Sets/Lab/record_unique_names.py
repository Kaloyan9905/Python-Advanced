n = int(input())
set_names = set()

for i in range(n):

    name = input()
    set_names.add(name)

print("\n".join(set_names))