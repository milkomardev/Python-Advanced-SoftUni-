def start_spring(**kwargs):
    types_dict = {}
    result = []
    for name, type in kwargs.items():
        if type not in types_dict:
            types_dict[type] = []
        types_dict[type].append(name)

    for type, names in sorted(types_dict.items(), key=lambda x: (-len(x[1]), x)):
        result.append(f"{type}:")
        for name in sorted(names):
            result.append(f"-{name}")
    return '\n'.join(el for el in result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
