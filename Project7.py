###############################################################
# CSE 231 project #7
#
# program that deals with data from MovieLens website.
# this program will read user, review, and movie data from the specified files and return avg max ratings.
# 
#function to open the 3 files.
#function to read the 3 different files and contstruct main lists for each.
#function to find movies for a specified year and returns their movie ids.
#function to find movies for a specified genre and returns their movie ids.
#function to filter lists of reviews based on a gender and returns a list of lists.
#function to filter lists of reviews based on occupation and returns list of lists.
#function to calculate average rating for reviews in the reviews list.
#function to calculate average reating for movies by a specified group of users.
#main function to call all other functions and interact with the user/options.
###############################################################

#initialize all constants
GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
#function to open the different files
def open_file(s):
    ''' A function that opens the 3 different files and returns a file pointer
    S: string of the file that we want to open
    Returns: fp'''
    if s == 'users':
        s_users = input("\nInput users filename: ")
        while True:
            try:
                fp = open(s_users, "r", encoding ="windows-1252")
                return fp
                break
            except FileNotFoundError:
                print('\nError: No such file; please try again.')
                s_users = input("\nInput users filename: ")
    elif s == 'reviews':
        s_reviews = input("\nInput reviews filename: ")
        while True:
            try:
                fp = open(s_reviews, "r", encoding ="windows-1252")
                return fp
                break
            except FileNotFoundError:
                print('\nError: No such file; please try again.')
                s_reviews = input("\nInput reviews filename: ")
    elif s == 'movies':
        s_movies = input("\nInput movies filename: ")
        while True:
            try:
                fp = open(s_movies, "r", encoding ="windows-1252")
                return fp
                break
            except FileNotFoundError:
                print('\nError: No such file; please try again.')
                s_movies = input("\nInput movies filename: ")

#function to read the reviews file and contstruct main list.
def read_reviews(N,fp):
    ''' A function that reads the review file and returns a main list of reviews
    N: number of users
    fp: file pointer that was returned by open_file
    returns: main list of reviews'''
    #initialize two empty lists
    l_reviews = []
    empty_list = []
    #append an empty list to l_reviews for length of N+1
    for i in range(0, N+1):
        l_reviews.append([])
    #read each line and get the three key pieces of information
    for line in fp:
        split_line = line.split()
        user_id = int(split_line[0])
        movie_id = int(split_line[1])
        rating = int(split_line[2])
        #add three pieces of info into a tuple
        reviews_tuple = (movie_id, rating)
        #append thr tuple to l_reviews and sort
        l_reviews[user_id].append(reviews_tuple)
        l_reviews[user_id].sort()
    #return the ist
    return l_reviews

#function to read the rusers file and contstruct main list.
def read_users(fp):
    ''' A function that reads the users file and returns a main list of users
    fp: file pointer that was returned by open_file
    returns: main list of users'''
    #initialize two empty lists
    L_users = []
    empty_list = []
    #append empty list at index 0
    L_users.append(empty_list)
    #read through each line and get the three important pieces information
    for line in fp:
        split_line = line.split('|')
        reviewer_id_int = int(split_line[0])
        age_int = int(split_line[1])
        gender_str = str(split_line[2])
        occupation_str = str(split_line[3])
        #add the information to a tuple
        users_tuple = (age_int, gender_str, occupation_str)
        #append the tuple to a list
        L_users.append(users_tuple)
    #return the list
    return L_users

#function to read the movies file and contstruct main list.
def read_movies(fp):
    ''' A function that reads the movie file and returns a main list of movies
    fp: file pointer returned by open_file
    returns: main list of movies'''
    #initial lize two empty lists
    empty_list = []
    L_movies = []
    #append empty list to L_movies at index 0
    L_movies.append(empty_list)
    use_this_list = []
    #read the lines in the file and get the three pieces of information
    for line in fp:
        split_line = line.split('|')
        movie_id = split_line[0]
        title = split_line[1]
        date = split_line[2]
        genre = split_line[5:24]
        #if genre has a 1, use the genre name
        for i, ch in enumerate(genre):
            for name in GENRES:
                if ch == '1' or ch =='1\n':
                    genre[i] = GENRES[i]
        #if the genre is 0, remove it
        #THIS WAS VERY DIFFICULT FOR ME
        #had to do this many times for it to work
        for i in genre:
            if i == '0' or i == '0\n':
                genre.remove(i)
        for i in genre:
            if i == '0' or i == '0\n':
                genre.remove(i)
        for i in genre:
            if i == '0' or i == '0\n':
                genre.remove(i)
        for i in genre:
            if i == '0' or i == '0\n':
                genre.remove(i)
        for i in genre:
            if i == '0' or i == '0\n':
                genre.remove(i)
        #add all information to a tuple
        movie_tuple =(title, date, genre)
        #append the tuple to a list and return the list
        L_movies.append(movie_tuple)
    return L_movies         
        
#function to find movies for a specified year and returns their movie ids.
def year_movies(year,L_movies):
    ''' A function that finds specified movies for a given year and return their ids
    year: user inputted year to filter the list
    L_movies: main list of movies
    returns: filtered list of movies'''
    #initialize first empty list
    return_list = []
    for i,ch in enumerate(L_movies):
        #we dont want to look at the first index, because it is empty
        if i > 0:
            the_date = ch[1].split('-')
            if len(the_date) >1:
                if int(the_date[2]) == year:
                    return_list.append(i)
    return return_list 

#function to find movies for a specified genre and returns their movie ids.
def genre_movies(genre,L_movies):
    ''' A function to find the movies of a specified genre and returns their ids
    genre: given genre input by the user to filter the list
    L_movies: main list of movies'''
    #initialize empty list
    return_list = []
    for index, ch in enumerate(L_movies):
        #we dont want the first index because it is empty
        if index > 0:
            the_genres = ch[2]
            if len(the_genres) >=0:
                if genre in the_genres:
                    return_list.append(index)
    return return_list #return_list

#function to filter lists of reviews based on a gender and returns a list of lists.
def gen_users (gender, L_users, L_reviews):
    ''' A function that filters the list of reviews based on a gender and returns list of lists
    gender: given gender input by the user to filter the list
    L_users: main list of users
    L_reviews: main list of reviews
    returns: a filtered list of lists'''
    #initialize empty list
    empty_list = []
    for index, ch in enumerate(L_users):
        #we dont want the first index, because it is empty
        if index > 0:
            the_gen = ch[1]
            if the_gen == gender:
                empty_list.append(L_reviews[index])
    return empty_list

#function to filter lists of reviews based on occupation and returns list of lists.          
def occ_users (occupation, L_users, L_reviews):
    ''' A function that filters the list of reviews based on an occupation
    occupation: given occupation input by user in order to filter the data
    L_users: main list of users
    L_reviews: main list of reviews
    returns: filtered list of lists'''
    #initialize empty list
    empty_list = []
    for index, ch in enumerate(L_users):
        #we dont want the first index, because it is empty
        if index > 0:
            the_occupation = ch[2]
            if the_occupation == occupation:
                empty_list.append(L_reviews[index])
    return empty_list

#function to calculate average rating for reviews in the reviews list.
def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' A function to calculate the average rating for the reviews
    L_in: what was returned by year_movies or genre_movies
    L_reviews: main list of reviews
    N_movies: total movies in the file
    returns: highest avg rating and the movie ids'''
    #initialize list where sum and count are both 0
    empty_t = [[0,0]]
    #append each list of 0,0 for the length of N_movies
    for i in range(N_movies):
        empty_t.append([0,0])  
    #initalize 2 more empty lists  
    a_listy = []
    movies_ids = []
#------------------------------------------------------------------#
#this section gets the sum of ratings and counts, and adds them to a list
    for i,ch in enumerate(L_reviews):
        for x in ch:
            for y in L_in:
                if y == x[0]:
                    #add review to the sum and increment 1 for the count
                    empty_t[x[0]][0] += x[1]
                    empty_t[x[0]][1] += 1
#------------------------------------------------------------------#
#this section divides the sum by the count and gets the average
    for index1, z in enumerate(empty_t):
        if z[0] != 0:
            average_rate = round(z[0]/z[1], 2)
            a_listy.append(average_rate)
            #a_listy.insert(index, average_rate)
        else:
            average_rate = 0
            a_listy.insert(index1, average_rate)
#------------------------------------------------------------------#
#this section finds the max average value
    max_value = max(a_listy)
    for index2, character in enumerate(a_listy):
        if max_value == character:
            movies_ids.append(index2)

    return movies_ids, max_value

#function to calculate average reating for movies by a specified group of users.      
def highest_rated_by_reviewer(L_in,N_movies):
    ''' A function to calculate avg rating for movies specidied by group of users
    L_in: what was returned by gen_users or occ_users
    N_movies: total number of users
    returns: highest avg ratings and the ids'''
    
    #initialize empty list and append a list of 0,0 that will be used to sum the reviews and count 
    empty_t = []
    for i in range(N_movies+1):
        empty_t.append([0,0])

    #initialize two more empty lists   
    a_listy = []
    movies_ids2 = []
    
#this section gets the sum of ratings and counts, and adds them to a list
    for i in L_in:
        #print(i)
        for x in i:
            #print(x)
            the_id = x[0]
            the_review = x[1]
            empty_t[x[0]][0] += the_review
            empty_t[x[0]][1] += 1
    #------------------------------------------#
#this section calculates the avergae
    for indy, ch in enumerate(empty_t):
        if ch[1] != 0:
            average_rate = round(ch[0]/ch[1], 2)
            a_listy.append(average_rate)
        else:
            average_rate = 0
            a_listy.insert(indy, average_rate)
    #-------------------------------------------#
#this section finds the highest average rating and returns the movie ids associated with that value
    max_value = max(a_listy)
    for index2, char in enumerate(a_listy):
        if max_value == char:
            movies_ids2.append(index2)
    return movies_ids2, max_value

def main():
    '''A function to run the program
    parameters: none
    returns: nothing'''
    #initialize some empty lists to append names into
    movie_names = []
    lower_genre = []
    lower_occ = []
    final_list = []

    #here I am calling the open file 3 different times in order to open each unique file
    users_file = open_file('users')
    reviews_file = open_file('reviews')
    movies_file = open_file('movies')

    # create a list of users by calling read_users
    the_read_users = read_users(users_file)

    #initialize n for later calculations
    N = len(the_read_users)

    #create reviews and movies lists by calling each unique read function
    the_read_reviews = read_reviews(N, reviews_file)
    the_read_movies = read_movies(movies_file)

    #initialize N for later calculations
    N_movies = len(the_read_movies)

    #print the menu
    print(MENU)

    #get a user option and convert it to an int
    prompt = input('\nSelect an option (1-5): ')
    prompt_int = int(prompt)
    while prompt_int != 5:
        if prompt_int == 1:
            #if the prompt is equal to one, then prompt for a year
            get_year = input('\nInput a year: ')
            #loop for error checking
            while True:
                try:
                    get_year_int = int(get_year)
                    break
                except ValueError:
                    print("\nError in year.")
                    get_year = input('\nInput a year: ')
                    get_year_int = int(get_year)
            while get_year_int < 1930 or get_year_int > 1998:
                print("\nError in year.")
                get_year = input('\nInput a year: ')
                get_year_int = int(get_year)
                if 1930 < get_year_int < 1998:
                    break
            #call the year_movies and highest rated functions in order to be able to display highest average
            the_year_movies = year_movies(get_year_int, the_read_movies)
            the_hr_by_movie = highest_rated_by_movie(the_year_movies, the_read_reviews, N_movies)
            print('\nAvg max rating for the year is:',the_hr_by_movie[1])
            # use the movie ids given by highest rating function in order to slice movies list to get movie names
            for x in the_hr_by_movie[0]:
                print(the_read_movies[x][0])
        elif prompt_int == 2:
            #if prompt is equal to 2, print all genres and prompt for a genre
            print('\nValid Genres are: ',GENRES)
            #convert genres to lowercase for comparison
            for gen in GENRES:
                genres_list_low = gen.lower()
                lower_genre.append(genres_list_low)
            genre_prompt = input('Input a genre: ')
            #loop for error checking of genre input
            while True:
                try:
                    genre_low = genre_prompt.lower()
                    break
                except ValueError:
                    print("\nError in genre.")
                    genre_prompt = input('\nInput a genre: ')
                    genre_low = genre_prompt.lower()
                while True:
                    if genre_low not in lower_genre:
                        print("\nError in genre.")
                        genre_prompt = input('\nInput a genre: ')
                        genre_low = genre_prompt.lower()
                        break
            #call the genre_movies and highest rating function to be able to display the highest average
            the_genre_movies = genre_movies(genre_low.capitalize(), the_read_movies)
            the_hr_by_movie = highest_rated_by_movie(the_genre_movies, the_read_reviews, N_movies)
            print('\nAvg max rating for the Genre is:', the_hr_by_movie[1])
            #use movie ids from highest average function in order to get movie names from the list of movies
            for x in the_hr_by_movie[0]:
                print(the_read_movies[x][0])         
        elif prompt_int == 3:
            #if the prompt is equal to 3, prompt for a gender and convert to lowercase for comparison
            gender_prompt = input('\nInput a gender (M,F): ')
            gender_low = gender_prompt.lower()
            #loop for error checking of gender
            while True:
                if gender_low not in ['m', 'f']:  #!= 'm' or gender_low != 'f':
                    print("\nError in gender.")
                    gender_prompt = input('\nInput a gender (M,F): ')
                    gender_low = gender_prompt.lower()
                    break  
                break
            # call gen_users function and hr by reviewer function in order to display avg max rating and movie names
            the_gen_users = gen_users(gender_low.upper(), the_read_users, the_read_reviews)     
            the_hr_by_reviewer = highest_rated_by_reviewer(the_gen_users, N_movies)       
            print('\nAvg max rating for the Gender is:', the_hr_by_reviewer[1])      
            #use movie ids from hr by reviewer in order to get movie names from list of movies
            for z in the_hr_by_reviewer[0]:
                print(the_read_movies[z][0])
        elif prompt_int == 4:
            #print all occupations and prompt user for occupation then convert all occupation to lowercase for comparing
            print('\nValid Occupatipns are: ',OCCUPATIONS)
            for occ in OCCUPATIONS:
                occ_list_low = occ.lower()
                lower_occ.append(occ_list_low)
            occupation_prompt = input('Input an occupation: ')
            occupation_low = occupation_prompt.lower()
            #loop for error checking of occupation
            while True:
                if occupation_low not in lower_occ:
                    print("\nError in occupation.")
                    occupation_prompt = input('Input an occupation: ')
                    occupation_low = occupation_prompt.lower()
                    break
                break
            #call occ_users and hr by reviewer functions in order to display max avg and movie names
            the_occ_users = occ_users(occupation_low, the_read_users, the_read_reviews)
            the_hr_by_reviewer = highest_rated_by_reviewer(the_occ_users, N_movies)      
            print('\nAvg max rating for the occupation is:', the_hr_by_reviewer[1])
            #use hr by reviewer in order to get movie names from list of movies
            for z in the_hr_by_reviewer[0]:
                print(the_read_movies[z][0])     
        #prompt again   
        prompt = input('\nSelect an option (1-5): ')
        prompt_int = int(prompt)


if __name__ == "__main__":
    main()
                                           
