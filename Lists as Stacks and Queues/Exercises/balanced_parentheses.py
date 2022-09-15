parentheses = list(input())

stack = []
are_balanced = True

for i in range(len(parentheses)):

    if not len(parentheses) % 2 == 0:
        are_balanced = False
        break

    if parentheses[i] in "([{":
        stack.append(parentheses[i])
        continue

    first = stack.pop()

    if first == "(" and not parentheses[i] == ")":
        are_balanced = False
        break
    elif first == "[" and not parentheses[i] == "]":
        are_balanced = False
        break
    elif first == "{" and not parentheses[i] == "}":
        are_balanced = False
        break

print("YES" if are_balanced else "NO")