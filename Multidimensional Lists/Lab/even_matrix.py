n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])

print(matrix)


