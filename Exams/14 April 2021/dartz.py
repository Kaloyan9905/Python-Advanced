def is_inside(r, c):
    if 0 <= r < 7 and 0 <= c < 7:
        return True
    return False


def directions(mtrx, r, c, result):
    result = sum([
        int(mtrx[0][c]),
        int(mtrx[6][c]),
        int(mtrx[r][0]),
        int(mtrx[r][6])
    ])

    return result


player_1, player_2 = input().split(", ")
matrix = [[x for x in input().split()] for _ in range(7)]

counter = 0
player_1_score = 0
player_2_score = 0
player_1_throws = 0
player_2_throws = 0
instant_win = False

while True:
    total_sum = 0

    command = input()

    command = command.replace("(", "")
    command = command.replace(")", "")

    row, col = [int(x) for x in command.split(", ")]

    player_1_throws += 1

    if is_inside(row, col):
        if matrix[row][col] == "B":
            instant_win = True
        elif matrix[row][col] == "D":
            total_sum = directions(matrix, row, col, total_sum)
            player_1_score += total_sum * 2
        elif matrix[row][col] == "T":
            total_sum = directions(matrix, row, col, total_sum)
            player_1_score += total_sum * 3
        else:
            player_1_score += int(matrix[row][col])

    if player_1_score >= 501 or instant_win:
        print(f"{player_1} won the game with {player_1_throws} throws!")
        break

    total_sum = 0

    command = input()

    command = command.replace("(", "")
    command = command.replace(")", "")

    row, col = [int(x) for x in command.split(", ")]

    player_2_throws += 1

    if is_inside(row, col):
        if matrix[row][col] == "B":
            instant_win = True
        elif matrix[row][col] == "D":
            total_sum = directions(matrix, row, col, total_sum)
            player_2_score += total_sum * 2
        elif matrix[row][col] == "T":
            total_sum = directions(matrix, row, col, total_sum)
            player_2_score += total_sum * 3
        else:
            player_2_score += int(matrix[row][col])

    if player_2_score >= 501 or instant_win:
        print(f"{player_2} won the game with {player_2_throws} throws!")
        break
