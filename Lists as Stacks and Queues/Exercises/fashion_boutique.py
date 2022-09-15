box_clothes = [int(x) for x in input().split()]
space = int(input())

counter = 0
curr_space = space

while box_clothes:
    piece = box_clothes.pop()

    if curr_space >= piece:
        curr_space -= piece

        if not box_clothes:
            counter += 1
        continue

    counter += 1
    curr_space = space
    box_clothes.append(piece)

print(counter)