n = int(input())

primary_diagonal = []
secondary_diagonal = []
matrix = []

for row in range(n):
    matrix.append([int(x) for x in input().split(", ")])

index = 0
for row in range(n):
    for col in range(n):
        primary_diagonal.append(matrix[row][col + index])
        index += 1
        break

index = 0
for row in range(n):
    for col in range(n - 1, -1, -1):
        secondary_diagonal.append(matrix[row][col - index])
        index += 1
        break

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
