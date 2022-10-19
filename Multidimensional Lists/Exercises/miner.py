def is_inside(r, c, num):
    if 0 <= r < num and 0 <= c < num:
        return True
    return False


n = int(input())
commands = input().split()

matrix = []
miner_row, miner_col = 0, 0
collected_coals = 0
total_coals = 0

for _ in range(n):
    matrix.append(input().split())

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            miner_row, miner_col = row, col
        elif matrix[row][col] == "c":
            total_coals += 1

for command in commands:
    if command == "up":
        miner_row -= 1
    elif command == "down":
        miner_row += 1
    elif command == "right":
        miner_col += 1
    else:
        miner_col -= 1

    if is_inside(miner_row, miner_col, n):
        if matrix[miner_row][miner_col] == "*":
            continue

        if matrix[miner_row][miner_col] == "c":
            matrix[miner_row][miner_col] = "*"
            collected_coals += 1

        if total_coals == collected_coals:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            exit()

        if matrix[miner_row][miner_col] == "e":
            print(f"Game over! ({miner_row}, {miner_col})")
            exit()
    else:
        if command == "up":
            miner_row += 1
        elif command == "down":
            miner_row -= 1
        elif command == "right":
            miner_col -= 1
        else:
            miner_col += 1

print(f"{total_coals - collected_coals} pieces of coal left. ({miner_row}, {miner_col})")
