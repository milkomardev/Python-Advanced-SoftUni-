from collections import deque

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"},
}

words = deque(input().split())
colors_found = []
while words:
    first_substring = words.popleft()
    last_substring = words.pop() if words else ''

    for color in (first_substring + last_substring, last_substring + first_substring):
        if color in colors:
            colors_found.append(color)
            break
    else:
        for el in (first_substring[:-1], last_substring[:-1]):
            if el:
                words.insert(len(words)//2, el)

for color in set(req_colors.keys()).intersection(colors_found):
    if not req_colors[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)