def words_sorting(*words):
    words_dict = {word: sum(map(ord, word)) for word in words}

    if sum(words_dict.values()) % 2 == 0:
        return '\n'.join(f"{w} - {v}" for w, v in sorted(words_dict.items(), key=lambda x: x[0]))
    elif sum(words_dict.values()) % 2 != 0:
        return '\n'.join(f"{w} - {v}" for w, v in sorted(words_dict.items(), key=lambda x: -x[1]))


print(
    words_sorting(
        'escape', 'charm', 'mythology'
    )
)

print(words_sorting(
    'escape', 'charm', 'eye'
    )
)

print(
    words_sorting(
        'cacophony',
        'accolade'
    )
)