def add_movie(movies):
    """This function adds a new movie to the dictionary or the movies database."""
    movie_name = input("\nEnter new movie name: ").strip()
    if movie_name in movies:
        print(f"Movie '{movie_name}' already exists!")
        return

    while True:
        try:
            rating = float(input("Enter new movie rating (0-10): ").strip())
            if 0 <= rating <= 10:
                movies[movie_name] = rating
                print(f"Movie '{movie_name}' successfully added.")
            else:
                print(f"Rating {rating} is invalid! Rating must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid number for the rating.")
        break