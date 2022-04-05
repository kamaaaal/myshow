from user import User

class Admin(User):
    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)
        self.is_admin = True
        self.history = []