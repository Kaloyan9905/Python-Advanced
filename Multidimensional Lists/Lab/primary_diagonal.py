n = int(input())

matrix = []
sum_list = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

condition = 0

for row in range(len(matrix)):
    for num in range(len(matrix[row])):
        sum_list.append(matrix[row][condition])
        condition += 1
        break

print(sum(sum_list))
