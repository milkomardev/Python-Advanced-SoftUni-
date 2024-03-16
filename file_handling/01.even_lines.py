import os

SYMBOLS = {"-", ",", ".", "!", "?"}

abs_path_dir = os.path.dirname(os.path.abspath(__file__))

text_path = os.path.join(abs_path_dir, 'text.txt')

with open(text_path, 'r') as file:
    text = file.readlines()

for i in range(0, len(text), 2):
    for symbol in SYMBOLS:
        text[i] = text[i].replace(symbol, '@')

    print(*text[i].split()[::-1], sep=' ')
