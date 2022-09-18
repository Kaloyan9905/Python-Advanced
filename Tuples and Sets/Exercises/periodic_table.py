n = int(input())

chemical_elements_set = set()

for _ in range(n):
    elements = input().split()
    for ele in elements:
        chemical_elements_set.add(ele)

for ele in chemical_elements_set:
    print(ele)