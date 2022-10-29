def is_inside(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def contains_queen(row, col, board):
    if board[row][col] == "Q":
        return True
    return False


matrix = [[x for x in input().split()] for _ in range(8)]

king_row, king_col = 0, 0
total_queens_that_attack = []

for index in range(8):
    if "K" in matrix[index]:
        king_row = index
        king_col = matrix[index].index("K")
        break

og_king_row, og_king_col = king_row, king_col

while is_inside(king_row - 1, king_col - 1):  # up-left
    king_row -= 1
    king_col -= 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row - 1, king_col + 1):  # up-right
    king_row -= 1
    king_col += 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row + 1, king_col - 1):  # down-left
    king_row += 1
    king_col -= 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row + 1, king_col + 1):  # down-right
    king_row += 1
    king_col += 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row, king_col - 1):  # left
    king_col -= 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row, king_col + 1):  # right
    king_col += 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row + 1, king_col):  # down
    king_row += 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

king_row, king_col = og_king_row, og_king_col
while is_inside(king_row - 1, king_col):  # down-right
    king_row -= 1

    if contains_queen(king_row, king_col, matrix):
        total_queens_that_attack.append([king_row, king_col])
        break

for queen in total_queens_that_attack:
    print(queen)

if not total_queens_that_attack:
    print("The king is safe!")
