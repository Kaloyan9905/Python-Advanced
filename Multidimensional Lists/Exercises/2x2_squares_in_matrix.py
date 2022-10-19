rows, columns = [int(x) for x in input().split()]

matrix = []
curr_matrix = []
counter = 0

for _ in range(rows):
    matrix.append(input().split())

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        curr_matrix = [
            matrix[row_index][col_index],
            matrix[row_index][col_index + 1],
            matrix[row_index + 1][col_index],
            matrix[row_index + 1][col_index + 1]
        ]
        if curr_matrix[0] == curr_matrix[1] == curr_matrix[2] == curr_matrix[3]:
            counter += 1

print(counter)
