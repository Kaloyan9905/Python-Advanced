matrix = []
matrix_sum = 0

rows_columns = [int(x) for x in input().split(", ")]

for _ in range(rows_columns[0]):

    matrix_info = [int(x) for x in input().split(", ")]
    matrix.append(matrix_info)
    matrix_sum += sum(matrix_info)

print(matrix_sum)
print(matrix)
