def operate(sign, *args):
    res = args[0]

    if sign == "+":
        for num in args[1::]:
            res += num
    elif sign == "-":
        for num in args[1::]:
            res -= num
    elif sign == "*":
        for num in args[1::]:
            res *= num
    else:
        for num in args[1::]:
            res /= num

    return res


print(operate("-", 1, 2, 3, 5, 10))