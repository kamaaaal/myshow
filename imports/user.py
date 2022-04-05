# createing a user class this will be inherited by customer and admin 

class User:
    def __init__(self,name,mail,password):
        self.name = name
        self.mail = mail
        self.password = password
        # will be used for identifying whether an user is admin
        self.is_admin = False
    
    def __str__(self) -> str:
        return self.name,self.mail        