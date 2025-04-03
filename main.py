from movie_project import *


def main():
    """Main function runs the movie database program by calling the functions"""

    # Dictionary to store the movies and their ratings
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 10.0,
        "The Room": 6.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 9.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 0.0
    }

    while True:
        print("\n********** YOU ARE WARMLY WELCOME TO MY MOVIES DATABASE **********\n")
        print("Menu:")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")

        choice = get_user_choice()  # Ensures user enters a valid number (1-8)

        # We use if-conditions to call the various functions to execute the program.
        if choice == 1:
            list_movies(movies)
        elif choice == 2:
            add_movie(movies)
        elif choice == 3:
            delete_movie(movies)
        elif choice == 4:
            update_movie(movies)
        elif choice == 5:
            movie_stats(movies)
        elif choice == 6:
            random_movie(movies)
        elif choice == 7:
            search_movie(movies)
        elif choice == 8:
            sort_movies_by_rating(movies)

        input(
            "\nPress Enter to continue...")  # We pause before displaying the menu


# Run the program
if __name__ == "__main__":
    main()  # The main() function runs when the script is executed directly, but not when it's imported into another program.