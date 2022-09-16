n = int(input())
set_cars = set()

for _ in range(n):

    command, name = input().split(", ")

    if command == "IN":
        set_cars.add(name)
    else:
        set_cars.remove(name)

if set_cars:
    print("\n".join(set_cars))
else:
    print("Parking Lot is Empty")