import datetime
from AccountHolder import AccountHolder


class Account:
    def __init__(self, account_holder: AccountHolder):
        self.account_holder = account_holder
        self.balance = 0.0
        self.account_number = None
        self.date_created = datetime.date.today()
        self.account_status = 'active'
