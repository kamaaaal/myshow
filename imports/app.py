from admin import Admin
from theater import Theater
from customer import Customer

class App:
    def __init__(self) -> None:
        self.theaters = {}
        self.customers = {}
        self.movies = {}
        self.admins = {}
        self.current_user = None

        # add user(sign up)
        def sign_up(self,name,mail,password) -> None:
            if name in self.customers:
                raise(Exception('user already exists'))
            self.customers[name] = Customer(name,mail,password) 
        
        # add admin(sign up)
        def sign_up_admin(self,name,mail,password) -> None:
            if name in self.admins:
                raise(Exception('user already exists'))
            self.admins[name] = Admin(name,mail,password) 

        # login
        def login(self,user_name,password) -> None:
            if user_name in self.customers:
                user = self.customers[user_name]
                if user.password == password:
                    self.current_user = user
                else:
                    raise(Exception('wrong password'))
            else:
                raise(Exception('user not found'))

        # logout
        def logout(self) -> None:
            self.current_user = None

        # adds theater if current user is admin 
        def add_theater(self,theater_name,location) -> None:
            if self.current_user.is_admin:
                if theater_name in self.theaters:
                    raise(Exception('theater already exists'))
                self.theaters[theater_name] = Theater(theater_name,location)
            else:
                raise(Exception('only admin can add theater'))
        
        # adds movie if current user is admin
        def add_movie(self.theater_list,movie_name,date_list,time_list) -> None:
            for theater in self.theater_list:
                if theater in self.theaters:
                    self.theaters[theater].add_movies(movie_name,date_list,time_list)
                else:
                    raise(Exception('theater not found'))
        
        # prints all movies and its value(tuple) date and time
        def print_movies(self) -> None:
            for theater in self.theaters:
                self.theaters[theater].print_movies() 
        
        # prints all theaters
        def print_theaters(self) -> None:
            for theater in self.theaters:
                print(theater)
        
        # book a seat is current user is customer
        def book_seat(self,theater_name,date,time,seat_list) -> None:
            if self.current_user.is_customer:
                if theater_name in self.theaters:
                    for seat in seat_list:
                        self.theaters[theater_name].shows[date][time].book_seat(seat)
                        #adding bookings to cumstomers history
                    self.current_user.bookings.append(f'{self.current_user} booked {seat_list} for  {theater_name}{date},{time} ')
                else:
                    raise(Exception('theater not found'))
            else:
                raise(Exception('only customer can book seat'))

