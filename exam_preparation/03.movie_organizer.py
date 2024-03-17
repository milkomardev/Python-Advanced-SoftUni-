def movie_organizer(*args):
    movie_dict = {}
    result = []

    for movie in args:
        if movie[1] not in movie_dict:
            movie_dict[movie[1]] = []
        movie_dict[movie[1]].append(movie[0])

    sorted_dict = sorted(movie_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for genre in sorted_dict:
        result.append(f"{genre[0]} - {len(genre[1])}")
        [result.append(f"* {movie}") for movie in sorted(genre[1])]

    return '\n'.join(result)





print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
