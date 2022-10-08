line = input().split("|")

line.reverse()
lst = []

for i in line:
    res = " ".join(i.split())
    for num in res.split():
        lst.append(int(num))

print(" ".join(str(x) for x in lst))

