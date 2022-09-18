n, m = map(int, input().split())

first = set()
second = set()

for _ in range(n):
    first.add(input())

for _ in range(m):
    second.add(input())

result = first.intersection(second)
print("\n".join(result))