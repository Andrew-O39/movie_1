def list_movies(movies):
    """ This function lists all the movies, their ratings and the total count in the movies database."""
    if not movies:
        print("\n No movies in the database.")
    else:
        print(f"\n{len(movies)} movies in total")
        for movie, rating in movies.items():
            print(f"{movie}: {rating}")