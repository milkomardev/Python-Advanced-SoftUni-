def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    result = []

    def place_kids():
        if len(kids) == 1:
            nice.append(kids[0][1]) if kid_type == 'Nice' else naughty.append(kids[0][1])
            santa_list.remove(*kids)

    for command in args:
        num, kid_type = command.split('-')
        kids = [data for data in santa_list if data[0] == int(num)]
        place_kids()

    for name, kid_type in kwargs.items():
        kids = [data for data in santa_list if data[1] == name]
        place_kids()

    for kid in santa_list:
        not_found.append(kid[1])

    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
    )
)

