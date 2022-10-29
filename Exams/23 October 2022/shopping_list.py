def shopping_list(money, **kwargs):
    bought_items = []
    res = ""

    if money < 100:
        return "You do not have enough budget."

    for key, value in kwargs.items():
        price, quantity = float(value[0]), int(value[1])

        if len(bought_items) == 5:
            break

        if price * quantity <= money:
            bought_items.append(f"You bought {key} for {price * quantity:.2f} leva.")
            money -= price * quantity

    for item in bought_items:
        res += item + "\n"

    return res


