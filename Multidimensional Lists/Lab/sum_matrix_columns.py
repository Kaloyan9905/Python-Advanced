from collections import deque

rows_columns = [int(x) for x in input().split(", ")]

matrix = deque([])
columns_nums = []

for _ in range(rows_columns[0]):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)


for i in range(rows_columns[1]):
    total = 0
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            total += matrix[row][i]
            break
    columns_nums.append(total)

print("\n".join([str(x) for x in columns_nums]))
