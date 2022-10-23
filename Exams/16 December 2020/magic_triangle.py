def get_magic_triangle(number):
    matrix = [[1], [1, 1]]
    for i in range(number - 2):
        matrix.append([])


print(get_magic_triangle(5))
