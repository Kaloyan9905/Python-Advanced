def stock_availability(items, parameter, *args):
    if parameter == "delivery":
        for stock in args:
            items.append(stock)
        return items

    if not args:
        items.pop(0)
        return items

    for stock in args:
        if isinstance(stock, int):
            for _ in range(stock):
                items.pop(0)
        else:
            count = items.count(stock)
            for _ in range(count):
                if stock in items:
                    items.remove(stock)
    return items


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
