n = int(input())

students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    reworked_value = []

    for x in value:
        res = f"{x:.2f}"
        reworked_value.append(res)

    print(f"{key} -> {' '.join(str(x) for x in reworked_value)} (avg: {sum(value) / len(value):.2f})")


