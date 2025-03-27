import random                                                                                                                               
from list_movies import list_movies
from add_movie import add_movie

def get_user_choice():                                                                                                                       
    """This function keeps asking the user for a valid menu choice (1-8)."""                                                                
    while True:                                                                                                                             
        try:                                                                                                                                
            choice = int(input("\nEnter choice (1-8): "))                                                                                   
            if 1 <= choice <= 8:                                                                                                            
                return choice                                                                                                               
            else:                                                                                                                           
                print("Invalid choice! Please enter a number between 1 and 8.")                                                             
        except ValueError:                                                                                                                  
            print("Invalid input! Please enter a valid number.")
                                                                                                                                            

def delete_movie(movies):                                                                                                                    
    """This function deletes a movie from the movies database."""                                                                           
    movie_name = input("\nEnter movie name to delete: ").strip().title()                                                                      
                                                                                                                                            
    if movie_name in movies:                                                                                                                
        del movies[movie_name]                                                                                                              
        print(f"Movie '{movie_name}' successfully deleted")                                                                                 
    else:                                                                                                                                   
        print(f"Movie '{movie_name}' doesn't exist!")                                                                                       
                                                                                                                                            

                                                                                                                                            
def update_movie(movies):                                                                                                                    
    """This function updates the rating of a movie in the database."""                                                                      
    movie_name = input("Enter movie name: ").strip().title()                                                                                

    if movie_name in movies:                                                                                                                
        try:                                                                                                                                
            new_rating = float(input(f"Enter new movie rating: "))                                                                          
            # Check if the new rating is within the valid range (0 to 10)                                                                   
            if 0 <= new_rating <= 10:                                                                                                       
                movies[movie_name] = new_rating                                                                                             
                print(f"Movie '{movie_name}' successfully updated.")                                                                        
            else:                                                                                                                           
                print(f"Rating {new_rating} is invalid rating. The rating must be between 0 and 10.")                                       
        except ValueError:                                                                                                                  
                    print("Invalid input! Please enter a numeric rating.")                                                                  
    else:                                                                                                                                   
        print(f"Movie '{movie_name}' doesn't exist.")                                                                                       
                                                                                                                                            
                                                                                                                                            
def movie_stats(movies):                                                                                                                     
    if not movies:                                                                                                                          
        print("No movies in the database.")                                                                                                 
        return                                                                                                                              
                                                                                                                                            
    ratings = list(movies.values())                                                                                                         
    total_movies = len(ratings)                                                                                                             
                                                                                                                                            
    # We calculate Average rating                                                                                                           
    average_rating = sum(ratings) / total_movies                                                                                            
                                                                                                                                            
    # We find the Median rating                                                                                                             
    sorted_ratings = sorted(ratings)                                                                                                        
    middle_value = total_movies // 2                                                                                                        
    if total_movies % 2 == 0:                                                                                                               
        median_rating = (sorted_ratings[middle_value - 1] + sorted_ratings[middle_value]) / 2                                               
    else:                                                                                                                                   
        median_rating = sorted_ratings[middle_value]                                                                                        
                                                                                                                                            
    # We find the Best and worst movies by looping through the movies dictionary to find the movies with the ratings that match with max_rat
    max_rating = max(ratings)                                                                                                               
    min_rating = min(ratings)                                                                                                               
                                                                                                                                            
    best_movies = []                                                                                                                        
    for movie, rating in movies.items():                                                                                                    
        if rating == max_rating:                                                                                                            
            best_movies.append(movie)                                                                                                       
                                                                                                                                            
    worst_movies = []                                                                                                                       
    for movie, rating in movies.items():                                                                                                    
        if rating == min_rating:                                                                                                            
            worst_movies.append(movie)                                                                                                      
                                                                                                                                            
    # Printing results                                                                                                                      
    print(f"\nAverage rating: {average_rating}")                                                                                            
    print(f"Median rating: {median_rating}")                                                                                                
    print("Best movie(s):", ", ".join(best_movies), f"({max_rating})")                                                                      
    print("Worst movie(s):", ", ".join(worst_movies), f"({min_rating})")                                                                    
                                                                                                                                            
                                                                                                                                            
def random_movie(movies):                                                                                                                    
    if not movies:                                                                                                                          
        print("No movies in the database.")                                                                                                 
        return                                                                                                                              
                                                                                                                                            
    movie, rating = random.choice(list(movies.items()))                                                                                     
    print(f"\nYour Movie for tonight: {movie}. It is rated {rating}")                                                                         
                                                                                                                                            
                                                                                                                                            
def search_movie(movies):                                                                                                                    
    search_input = input("Enter part of the movie name: ").strip().lower()                                                                  
                                                                                                                                            
    matching_movies = {}  # Initialize an empty dictionary to store matching movies.                                                        
                                                                                                                                            
    # Search for movies that contain the input                                                                                              
    for movie, rating in movies.items():                                                                                                    
        if search_input in movie.lower():                                                                                                   
            matching_movies[movie] = rating                                                                                                 
                                                                                                                                            
    # Print the matching movies if found                                                                                                    
    if matching_movies:  # Check if there are matches                                                                                       
        for movie, rating in matching_movies.items():                                                                                       
            print(f"{movie}: {rating}")                                                                                                     
    else:                                                                                                                                   
        print("No matching movies found.")                                                                                                  
                                                                                                                                            
                                                                                                                                            
def get_rating(movie_tuple):                                                                                                                 
    """This function is a helper function to get the rating from a movie tuple."""                                                          
    return movie_tuple[1]  # Extracts the rating (second item in the tuple)                                                                 
                                                                                                                                            
def sort_movies_by_rating(movies):                                                                                                           
    """This function sorts and display movies based on ratings in descending order."""                                                      
                                                                                                                                            
    # Convert the dictionary into a list of tuples and sort it                                                                              
    sorted_movies = sorted(movies.items(), key=get_rating, reverse=True)                                                                    
                                                                                                                                            
    # Print the sorted movies                                                                                                               
    print() # A single blank line for good readability                                                                                      
    for movie, rating in sorted_movies:                                                                                                     
        print(f"{movie}: {rating}")                                                                                                         
                                                                                                                                            
                                                                                                                                            
