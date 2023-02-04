def shopping_cart(*args):
    dishes = {
        "Pizza": [],
        "Dessert": [],
        "Soup": []
    }

    counter = 0

    for items in args:
        if items == "Stop":
            for key, value in dishes.items():
                if len(value) == 0:
                    counter += 1

            if counter == 3:
                return "No products in the cart!"

            res = ""
            reworked_dict = sorted(dishes.items(), key=lambda x: (-len(x[1]), x[0]))

            for key, value in reworked_dict:
                value.sort()
                res += f"{key}:" + "\n"
                for ele in value:
                    res += f" - {ele}" + "\n"

            return res

        dish, product = items

        if product not in dishes[dish]:
            if dish == "Pizza":
                if len(dishes[dish]) < 4:
                    dishes[dish].append(product)
            elif dish == "Dessert":
                if len(dishes[dish]) < 2:
                    dishes[dish].append(product)
            elif dish == "Soup":
                if len(dishes[dish]) < 3:
                    dishes[dish].append(product)


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

