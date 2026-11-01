movies = {
    "action": ["John Wick", "Gladiator", "The Dark Knight"],
    "comedy": ["Home Alone", "The Mask", "Free Guy"],
    "horror": ["The Conjuring", "IT", "A Quiet Place"],
    "romance": ["The Notebook", "Titanic", "Me Before You"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

print("🎬 Welcome to Movie Recommender!")

print("\nAvailable genres:")
for genre in movies:
    print(genre)

choice = input("\nWhat genre do you like? ").lower()

if choice in movies:
    print("\nHere are your recommendations:")
    for movie in movies[choice]:
        print("🍿", movie)
else:
    print("Sorry, genre not found!")
