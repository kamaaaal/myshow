from logging import raiseExceptions
from seat import seat,seats,convert_seat
from movie import Movie 

class Theater:
    def __init__(self,theater_name,location) -> None:
        self.name = theater_name
        self.location = location
        self.movies = {}
        self.movies_det = {}
        self.shows = {
            # nesting another dictionary which will store time(keys) seats(values)
            # date -> time -> movie : movie name , seats : seats
        }

    def add_movies(self,movie,date_list,time_list): 
        # adding a movie to the dictionary
        self.movies_det = Movie (movie)
        if movie not in self.movies:
            curr_movie = self.movies[movie] = {}
        else:
            raise(Exception('movie already exists'))
    

        for date in date_list:
        #creating a dictionary of shows and time to store seats
            curr_movie[date] = set() # using set to store date because date are string and set is faster in traversal
            for time in time_list:
                # storing time and date in movies dictionary
                if time not in curr_movie[date]:
                    curr_movie[date].add(time)

                #updating the dictionary if date is already found
                if date in self.shows:
                    self.shows[date].update({time : {'movie' : movie,
                                                     'seats' : seats()}})
                # creating a new dictionary for new shows 
                else :
                    self.shows[date] = {time: {'movie' : movie,
                                            'seats' : seats()}}

    # to print the seats in order                
    def print_seats(self,date,time):
        selected = self.shows[date][time]
        for row in selected['seats']:
            for seat in row:
                print(seat,end='|')
            print()
    
    # prints all movies and its value 
    # date and time 
    def print_movies(self):
        for movie,dates in self.movies.items():
            print(movie)
            for date,times in dates.items():
                print(f'date: {date}')
                for time in times:
                    print(f'\t time :{time}')

    #prints all shows(date and time ) available for this theatrer
    def print_shows(self):
        for date,times in self.shows.items():
            print(f'date : {date} : ')
            for time,movie in times.items():
                print(f'\t{time} : {movie["movie"]} ',)
    
    def book_seat(self,date,time,seat_no):
        try:
            row,column = convert_seat(seat_no)
        except ValueError :
            raise Exception('invalid seat no')
        self.shows[date][time]['seats'][row][column].book('kamal')
        


luxe = Theater('luxe','velachery')
luxe.add_movies('manmatha leelai',['9','11','12','31'],['9:00','12:00','18:00'])
luxe.print_movies()
luxe.print_shows()
luxe.book_seat('9','9:00','100')
luxe.print_seats('9','9:00')
