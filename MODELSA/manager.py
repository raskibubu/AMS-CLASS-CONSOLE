import datetime

class Manager:
    def __init__(self, first_name, email: str, password: str):
        self.first_name = first_name
        self.middle_name = None
        self.last_name = None
        self.email = email
        self.password = password
        self.phone = None
        
    def change_password(self, password: str):
        self.password = password
        return True        
        
