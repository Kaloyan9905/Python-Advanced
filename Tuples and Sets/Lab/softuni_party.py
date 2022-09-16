n = int(input())

reservation_numbers = set()

for _ in range(n):
    reservation_numbers.add(input())

while True:
    guest = input()

    if guest == "END":
        break

    if guest in reservation_numbers:
        reservation_numbers.remove(guest)

vips = []
regulars = []

if reservation_numbers:
    for guest in reservation_numbers:

        if guest[0].isnumeric():
            vips.append(guest)
            continue

        regulars.append(guest)

print(len(regulars) + len(vips))


vips.sort()
regulars.sort()

if vips:
    print("\n".join(vips))

if regulars:
    print("\n".join(regulars))
