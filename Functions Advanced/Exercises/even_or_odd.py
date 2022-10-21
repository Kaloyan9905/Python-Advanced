def even_odd(*args):
    odd_even = args[-1]
    args = args[0:-1]
    result = []

    if odd_even == "even":
        result.extend([x for x in args if int(x) % 2 == 0])
    else:
        result.extend([x for x in args if not int(x) % 2 == 0])

    return result



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
