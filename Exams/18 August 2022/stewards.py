from collections import deque

seats = input().split(", ")

first_deque = deque([int(x) for x in input().split(", ")])
second_deque = deque([int(x) for x in input().split(", ")])

rotations = 10
matched_seats = []

while rotations and len(matched_seats) < 3:

    first = first_deque.popleft()
    second = second_deque.pop()

    ascii_res = chr(first + second)
    rotations -= 1

    seat = str(first) + ascii_res
    if str(first) + ascii_res in seats:
        if seat not in matched_seats:
            matched_seats.append(seat)
            continue

    seat = str(second) + ascii_res
    if seat in seats:
        if seat not in matched_seats:
            matched_seats.append(seat)
            continue

    first_deque.append(first)
    second_deque.appendleft(second)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {10 - rotations}")
