player_1, player_2 = input().split(", ")

matrix = []

player_1_break = False
player_2_break = False

for _ in range(6):
    matrix.append(input().split())

while True:
    line = input()

    line = line.replace("(", "")
    line = line.replace(")", "")

    row, col = [int(x) for x in line.split(", ")]

    if not player_1_break:
        if matrix[row][col] == "E":
            print(f"{player_1} found the Exit and wins the game!")
            exit()

        if matrix[row][col] == "T":
            print(f"{player_1} is out of the game! The winner is {player_2}.")
            exit()

        if matrix[row][col] == "W":
            print(f"{player_1} hits a wall and needs to rest.")
            player_1_break = True

    else:
        player_1_break = False

    line = input()

    line = line.replace("(", "")
    line = line.replace(")", "")

    row, col = [int(x) for x in line.split(", ")]

    if not player_2_break:
        if matrix[row][col] == "E":
            print(f"{player_2} found the Exit and wins the game!")
            exit()

        if matrix[row][col] == "T":
            print(f"{player_2} is out of the game! The winner is {player_1}.")
            exit()

        if matrix[row][col] == "W":
            print(f"{player_2} hits a wall and needs to rest.")
            player_2_break = True

    else:
        player_2_break = False
