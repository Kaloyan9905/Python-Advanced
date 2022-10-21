def fill_the_box(h, l, w, *args):
    total_space = h * l * w
    total_cubes = 0

    for num in args:
        if num == "Finish":
            if total_space > total_cubes:
                return f"There is free space in the box. You could put {total_space - total_cubes} more cubes."
            return f"No more free space! You have {total_cubes - total_space} more cubes."

        total_cubes += num




print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
