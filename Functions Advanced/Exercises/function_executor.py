def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    res = []
    for name, params in args:
        fun_res = name(*params)
        res.append(f"{name} - {fun_res}")
    return "\n".join(res)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
