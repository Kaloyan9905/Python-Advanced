string = input()

stack = []

for index in range(len(string)):
    char = string[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        last_opening_bracket_index = stack.pop()
        res = string[last_opening_bracket_index:index + 1]
        print(res)