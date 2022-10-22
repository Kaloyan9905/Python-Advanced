from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
pizza_employees = [int(x) for x in input().split(", ")]

total_pizza = 0

while pizza_employees and pizza_orders:
    pizza = pizza_orders.popleft()
    employee = pizza_employees.pop()

    if pizza <= 0:
        pizza_employees.append(employee)
        continue

    if pizza > 10:
        pizza_employees.append(employee)
        continue

    if employee >= pizza:
        total_pizza += pizza
        continue

    if employee < pizza:
        total_pizza += employee
        pizza_orders.appendleft(pizza - employee)
        continue

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in pizza_employees])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")

