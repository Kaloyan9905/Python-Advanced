n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(len(matrix[i])):
        primary_diagonal.append(matrix[i][i])
        break

counter = 1

for i in range(n):
    for j in range(len(matrix[i]) - 1, -1, -1):
        secondary_diagonal.append(matrix[i][n - counter])
        counter += 1
        break

print(abs(sum(secondary_diagonal) - sum(primary_diagonal)))
