from MODELSA.account import Account
import datetime


class Loan:
    def __init__(self, account: Account, loan_type: str):
        self.account = account
        self.interest_rate = 0.0
        self.date = datetime.date.today()
        self.loan_type = loan_type
        self.balance = 0.0
        self.amount = 0.0
        self.status = 'inactive'
        self.id = 0

    
