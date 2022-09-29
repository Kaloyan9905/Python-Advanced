import sys

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
biggest_matrix = [-sys.maxsize]

for _ in range(rows):
    matrix.append(list(map(int, input().split(", "))))

for row in range(rows - 1):
    for col in range(cols - 1):
        curr_matrix = [
            matrix[row][col],
            matrix[row][col + 1],
            matrix[row + 1][col],
            matrix[row + 1][col + 1]
        ]

        if sum(curr_matrix) > sum(biggest_matrix):
            biggest_matrix = curr_matrix.copy()

sum_matrix = sum(biggest_matrix)

for ele in biggest_matrix:
    for r in range(2):
        print(biggest_matrix.pop(0), end=" ")
    print()

print(sum_matrix)
