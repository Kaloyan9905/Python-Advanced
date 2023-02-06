size = int(input())
racing_number = input()
matrix = [[x for x in input().split()] for _ in range(size)]

tunnels_coords = []
car_row, car_col = 0, 0
total_kilometers = 0
finished = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "T":
            tunnels_coords.append([r, c])

while True:
    if finished:
        break

    direction = input()

    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    for key, value in directions.items():

        if key == direction:
            car_row += value[0]
            car_col += value[1]

            if matrix[car_row][car_col] == ".":
                total_kilometers += 10
                continue

            if matrix[car_row][car_col] == "T":
                for tunnel_row, tunnel_col in tunnels_coords:
                    matrix[tunnel_row][tunnel_col] = "."

                    if tunnel_row == car_row and tunnel_col == car_col:
                        continue

                    car_row, car_col = tunnel_row, tunnel_col
                    total_kilometers += 30

            if matrix[car_row][car_col] == "F":
                total_kilometers += 10
                finished = True
                print(f"Racing car {racing_number} finished the stage!")
                break

matrix[car_row][car_col] = "C"

print(f"Distance covered {total_kilometers} km.")

for row in matrix:
    print(*row, sep="")
