def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    res = ""

    res += f"Rectangle area: {area()}" + '\n'
    res += f"Rectangle perimeter: {perimeter()}"

    return res


print(rectangle(2, 10))
