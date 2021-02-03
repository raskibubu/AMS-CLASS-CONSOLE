from MODELSA.overdraft import Overdraft
from MODELSA.account import Account
from typing import List
import datetime
0
# overdraft = Overdraft()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
class OverdraftManger:
    overdrafts: List[Overdraft] = []
    

    def create_overdraft(self, account: Account, amount: float):
        active_account = self.__is_account_active(account)
        if active_account is True:
            if amount <= 100000.00:
                overdraft_status = self.__is_overdraft_not_active(account_number=account.account_number)
                if overdraft_status is False:
                    overdraft = Overdraft(amount=amount, account=account)
                    overdraft.id = self.__get_id()
                    overdraft.balance = account
                    account.balance -= amount
                    overdraft.date = datetime.date.today()
                    answer = 'Overdraft collected'
                    return answer
                else:
                    answer = 'You have already collected an overdraft. Please pay up'
                    return answer
            else:
                answer = 'You cannot collect above 100 thousand'
                return answer
        else:
            answer = 'Account is not active'
            return answer
            
            
    def pay_overdraft(self, account_number: str, amount: float):
        overdrafts = self.__get_overdraft(account_number=account_number)
        if overdrafts is not False:
            overdrafts.account.balance -= amount
            for overdraft in overdrafts:
                if overdraft.balance == 0:
                    overdraft.status == 'inactive'
                    answer = 'Overdraft has been totally paid'
                    return answer
                else:
                    answer = 'Deducted from overdraft'
                    return answer
        else:
            answer = 'No active overdraft found'
            return answer             
                    
    def __check__amount__overdraft(self, account_number: str):
        for Overdraft in self.overdrafts:
            if Overdraft.amount <= 100000:
                return True
        return False

    def __find(self, account_number: str): 
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                return overdraft
            else:
                return None

    
    def __get_overdraft_initial_balance(self,  amount: float):
            val = 100000 
            amount = val
            return amount       
        


    def __check_if_no_active_overdraft(self, account_number: str):
            for overdraft in self.overdrafts:
                if overdraft.account.account_number == account_number:
                    if overdraft.status == 'active':
                        return True
            return False
    
    
    def list_overdraft(self):
        for overdraft in self.overdrafts:
            self.__show(overdraft)


    def search(self, account_number: str):

        overdraft = self.__find(account_number)
        if overdraft is None:
            return False
        else:
            self.__show(overdraft)



    def __get_id(self):
        length = len(self.overdrafts)
        if length == 0:
            length += 1
            return length
        else:
            for overdraft in self.overdrafts:
                if overdraft.id == length:
                    length += 1
                    return length
                else:
                    continue
                
    def __get_overdraft(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.status == 'active':
                    return overdraft
                else:
                    return False

    def __is_account_active(self, account: Account):
        if account.account_status == False:
            return False
        else:
            return True

    def __is_overdraft_not_active(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.status == 'active':
                    return overdraft
        return False

    def __show(self, overdraft: Overdraft):
        print(
              overdraft.id, '.', ' ', overdraft.account.account_number, ' ',overdraft.account.account_holder.first_name," ", overdraft.amount,
              ' ', '\t', overdraft.balance, )
