def concatenate(*args, **kwargs):
    line = ''.join(args)

    for key, value in kwargs.items():
        line = line.replace(key, value)

    return line





print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))