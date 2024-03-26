def list_manipulator(numbers_list, *args):
    if args[0] == 'add':
        if args[1] == 'beginning':
            for i in range(len(args)-1, 1, -1):
                numbers_list.insert(0, args[i])

        elif args[1] == 'end':
            for i in range(2, len(args)):
                numbers_list.append(args[i])

    elif args[0] == 'remove':
        if args[1] == 'beginning':
            if len(args) == 2:
                numbers_list.pop(0)

            else:
                for _ in range(args[2]):
                    numbers_list.pop(0)

        elif args[1] == 'end':
            if len(args) == 2:
                numbers_list.pop(-1)

            else:
                for _ in range(args[2]):
                    numbers_list.pop(-1)

    return numbers_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
