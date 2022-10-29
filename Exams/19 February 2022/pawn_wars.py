def white_pawn_move(row, col, board):
    if 0 <= row < 8 and 0 <= col < 8:
        board[row][col] = "w"
        board[row + 1][col] = "-"
    return board


def black_pawn_move(row, col, board):
    if 0 <= row < 8 and 0 <= col < 8:
        board[row][col] = "b"
        board[row - 1][col] = "-"
    return board


def square_check(row, col, ranks, lines):
    rank = ""
    line = ""

    for key, value in ranks.items():
        if key == row:
            rank = value

    for key, value in lines.items():
        if key == col:
            line = value

    return f"{line.lower()}{rank}"


matrix = []
black_row, black_col = None, None
white_row, white_col = None, None
impossible_capture_between_pawns = False
game_is_on = True
square = None

chess_board_ranks = {
    7: "1",
    6: "2",
    5: "3",
    4: "4",
    3: "5",
    2: "6",
    1: "7",
    0: "8",
}

chess_board_lines = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
}

for r in range(8):
    matrix.append(input().split())

for r in range(8):
    for c in range(8):
        if matrix[r][c] == "w":
            white_row, white_col = r, c
        elif matrix[r][c] == "b":
            black_row, black_col = r, c

if abs(black_col - white_col) > 1:
    impossible_capture_between_pawns = True

if black_row == white_row:
    impossible_capture_between_pawns = True

if white_row < black_row:
    impossible_capture_between_pawns = True

if impossible_capture_between_pawns:
    while game_is_on:

        white_row -= 1
        matrix = white_pawn_move(white_row, white_col, matrix)

        if white_row == 0:
            square = square_check(white_row, white_col, chess_board_ranks, chess_board_lines)
            print(f"Game over! White pawn is promoted to a queen at {square}.")
            game_is_on = False
            break

        black_row += 1
        matrix = black_pawn_move(black_row, black_col, matrix)

        if black_row == 7:
            square = square_check(black_row, black_col, chess_board_ranks, chess_board_lines)
            print(f"Game over! Black pawn is promoted to a queen at {square}.")
            game_is_on = False
            break

while game_is_on:
    if matrix[white_row - 1][white_col - 1] == "b":
        white_row -= 1
        white_col -= 1
        game_is_on = False
    elif matrix[white_row - 1][white_col + 1] == "b":
        white_row -= 1
        white_col += 1
        game_is_on = False
    else:
        white_row -= 1
        matrix = white_pawn_move(white_row, white_col, matrix)

    if not game_is_on:
        square = square_check(white_row, white_col, chess_board_ranks, chess_board_lines)
        print(f"Game over! White win, capture on {square}.")
        break

    if matrix[black_row + 1][black_col + 1] == "w":
        black_row += 1
        black_col += 1
        game_is_on = False
    elif matrix[black_row + 1][black_col - 1] == "w":
        black_row += 1
        black_col -= 1
        game_is_on = False
    else:
        black_row += 1
        matrix = black_pawn_move(black_row, black_col, matrix)

    if not game_is_on:
        square = square_check(black_row, black_col, chess_board_ranks, chess_board_lines)
        print(f"Game over! Black win, capture on {square}.")
        break
