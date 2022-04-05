from mimetypes import init


class Movie:
    # overloaded constructor 
    def __init__(self,movie_name,actor = None,actress = None,director = None,music_director = None) -> None:
        self.name = movie_name
        self.actor = actor
        self.actress = actress
        self.director = director
        self.music_director = music_director

    def __str__(self) -> str:
        return self.name
    
    # creating a equality operator
    def __eq__(self,other) -> bool:
        return self.name == other.name
    
    # creating a hash function
    def __hash__(self) -> int:
        return hash(self.name)


