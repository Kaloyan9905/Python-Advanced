rows = int(input())
matrix = []
reworked_list = []

for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

for curr_row in range(len(matrix)):
    for num in range(len(matrix[curr_row])):
        reworked_list.append(matrix[curr_row][num])

print(reworked_list)
