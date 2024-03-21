def forecast(*args):
    weather_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': [], }
    result = []
    for element in args:
        weather_dict[element[1]].append(element[0])

    for weather, cities in weather_dict.items():
        if cities:
            for city in sorted(cities):
                result.append(f"{city} - {weather}")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
