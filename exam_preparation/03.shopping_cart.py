def shopping_cart(*args):
    meals_dict = {"Soup": [], "Pizza": [], "Dessert": [], }
    result = []

    for arg in args:
        if arg == 'Stop':
            break
        else:
            if arg[0] == "Soup":
                if len(meals_dict['Soup']) < 3 and arg[1] not in meals_dict['Soup']:
                    meals_dict['Soup'].append(arg[1])
            if arg[0] == "Pizza":
                if len(meals_dict['Pizza']) < 4 and arg[1] not in meals_dict['Pizza']:
                    meals_dict['Pizza'].append(arg[1])
            if arg[0] == "Dessert":
                if len(meals_dict['Dessert']) < 2 and arg[1] not in meals_dict['Dessert']:
                    meals_dict['Dessert'].append(arg[1])

    for meal, products in sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{meal}:")
        [result.append(f" - {product}") for product in sorted(products)]

    if len(meals_dict["Soup"]) == 0 and len(meals_dict["Pizza"]) == 0 and len(meals_dict["Dessert"]) == 0:
        return 'No products in the cart!'
    else:
        return '\n'.join(el for el in result)

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
