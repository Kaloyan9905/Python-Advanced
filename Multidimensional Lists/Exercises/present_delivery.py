presents = int(input())
size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

santa_row, santa_col = 0, 0
happy_kids = 0
happy_kids_left = 0

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for index in range(size):
    if "S" in matrix[index]:
        santa_row = index
        santa_col = matrix[index].index("S")

matrix[santa_row][santa_col] = "-"

while True:
    if not presents:
        matrix[santa_row][santa_col] = "S"
        break

    command = input()

    if command == "Christmas morning":
        matrix[santa_row][santa_col] = "S"
        break

    for key, value in positions.items():
        if command == key:
            santa_row += value[0]
            santa_col += value[1]
            break

    if matrix[santa_row][santa_col] == "-":
        continue

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        happy_kids += 1
        matrix[santa_row][santa_col] = "-"
        continue

    if matrix[santa_row][santa_col] == "X":
        matrix[santa_row][santa_col] = "-"
        continue

    for key, value in positions.items():
        if not presents:
            break

        curr_row, curr_col = santa_row, santa_col

        curr_row += value[0]
        curr_col += value[1]

        if matrix[curr_row][curr_col] == "-":
            continue

        if matrix[curr_row][curr_col] == "V":
            presents -= 1
            happy_kids += 1
            matrix[curr_row][curr_col] = "-"
            continue

        if matrix[curr_row][curr_col] == "X":
            matrix[curr_row][curr_col] = "-"
            presents -= 1
            continue

for index in range(size):
    if "V" in matrix[index]:
        happy_kids_left += matrix[index].count("V")

if happy_kids_left and not presents:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if happy_kids_left:
    print(f"No presents for {happy_kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")










