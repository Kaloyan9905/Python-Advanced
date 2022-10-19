import sys

rows, cols = [int(x) for x in input().split()]

matrix = []
curr_matrix = []
final_matrix = [-sys.maxsize]

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        curr_matrix = [
            matrix[row_index][col_index],
            matrix[row_index][col_index + 1],
            matrix[row_index][col_index + 2],
            matrix[row_index + 1][col_index],
            matrix[row_index + 1][col_index + 1],
            matrix[row_index + 1][col_index + 2],
            matrix[row_index + 2][col_index],
            matrix[row_index + 2][col_index + 1],
            matrix[row_index + 2][col_index + 2]
        ]
        if sum(curr_matrix) > sum(final_matrix):
            final_matrix.clear()
            final_matrix = curr_matrix.copy()

print(f"Sum = {sum(final_matrix)}")
for i in range(3):
    print(*final_matrix[:3])
    del final_matrix[:3]