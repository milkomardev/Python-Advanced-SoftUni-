def stock_availability(flavours_list,command, *args):

    if command == 'delivery':
        [flavours_list.append(arg) for arg in args]
    elif command == 'sell':
        if not args:
            flavours_list.pop(0)
        else:
            for arg in args:
                if isinstance(arg, str):
                    if arg in flavours_list:
                        count = flavours_list.count(arg)
                        for _ in range(count):
                            flavours_list.remove(arg)
                else:
                    for _ in range(arg):
                        flavours_list.pop(0)

    return flavours_list




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
