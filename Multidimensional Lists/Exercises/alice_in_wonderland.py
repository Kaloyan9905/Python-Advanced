def is_inside(curr_row, curr_col, num):
    if 0 <= curr_row < num and 0 <= curr_col < num:
        return True
    return False


def func(tea_counter_cmd, mtrx, curr_row, curr_col, position_r_cmd, outside_cmd):
    if not is_inside(r, c, n):
        outside_cmd = True
        return mtrx, outside_cmd, position_r_cmd, tea_counter_cmd

    if mtrx[curr_row][curr_col] == "*":
        return mtrx, outside_cmd, position_r_cmd, tea_counter_cmd

    if mtrx[curr_row][curr_col] == ".":
        mtrx[curr_row][curr_col] = "*"
        return mtrx, outside_cmd, position_r_cmd, tea_counter_cmd

    if mtrx[curr_row][curr_col] == "R":
        mtrx[curr_row][curr_col] = "*"
        position_r_cmd = True
        return mtrx, outside_cmd, position_r_cmd, tea_counter_cmd

    tea_counter_cmd += int(mtrx[curr_row][curr_col])
    mtrx[curr_row][curr_col] = "*"

    return mtrx, outside_cmd, position_r_cmd, tea_counter_cmd


n = int(input())

matrix = []
alice_position = ()
outside = False
position_r = False
tea_counter = 0

for _ in range(n):
    matrix.append(input().split())

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "A":
            alice_position = row, col

r, c = alice_position
matrix[r][c] = "*"

while True:
    command = input()

    if command == "left":
        c -= 1
        matrix, outside, position_r, tea_counter = func(tea_counter, matrix, r, c, position_r, outside)
    elif command == "right":
        c += 1
        matrix, outside, position_r, tea_counter = func(tea_counter, matrix, r, c, position_r, outside)
    elif command == "up":
        r -= 1
        matrix, outside, position_r, tea_counter = func(tea_counter, matrix, r, c, position_r, outside)
    else:
        r += 1
        matrix, outside, position_r, tea_counter = func(tea_counter, matrix, r, c, position_r, outside)

    if tea_counter >= 10 or outside or position_r:
        break

if outside or position_r:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep=" ")
