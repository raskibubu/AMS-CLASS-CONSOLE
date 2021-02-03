import random
import datetime
class AccountHolder:


    def __init__(self, id: int, email: str, first_name: str, password: str):
        self.first_name = first_name
        self.middle_name = None
        self.last_name = None
        self.email = email
        self.password = password
        self.phone = None
        self.id = id

    def __change_password(self, password: str):
        self.password = password
        return True


class Account:
    def __init__(self, id: int, account_holder: AccountHolder, pin: int):
        self.account_holder = account_holder
        self.balance = 0.0
        self.account_number = None
        self.date_created = datetime.date.today()
        self.account_status = 'active'
        self.pin = pin
        self.id = id

class Overdraft:
    def __init__(self, account: Account, amount: float):
        self.ammount = amount
        self.account = Account
        self.date = datetime.date.today()



        