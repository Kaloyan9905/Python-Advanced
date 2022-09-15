from collections import deque

green_light = int(input())
free_window = int(input())

cars_queue = deque()
light = green_light
window = free_window
passed_cars = 0

while True:
    command = input()

    if command == "END":
        break

    if not command == "green":
        cars_queue.append(command)
        continue

    while cars_queue:
        if not light:
            break

        car = cars_queue.popleft()

        if len(car) > window + light:
            print("A crash happened!")
            print(f"{car} was hit at {car[window + light]}.")
            exit()

        elif len(car) > light:
            light = 0
            passed_cars += 1
            continue

        light -= len(car)
        passed_cars += 1

    light = green_light

print(f"Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")




