from MODELSA.accountholder import AccountHolder
from MANAGERS.AccountHolderManager import AccountHolderManager
from MODELSA.manager import Manager
from MANAGERS.ManagersManager import ManagersManager
from MANAGERS.AccountManager import AccountManager
from MODELSA.account import Account
from MODELSA.loan import Loan
from MANAGERS.LoanManager import LoanManger
from MANAGERS.OverdraftManager import OverdraftManger
from MODELSA.overdraft import Overdraft
from typing import List

acount_holder_manager = AccountHolderManager()
manager_man = ManagersManager()
account_manager = AccountManager()
loan_manager = LoanManger()
overdraft_manager = OverdraftManger()

def mainMenu():
    print("Welcome to Liverpool Bank" '\n' "Enter 0 to Quit" '\n' "Enter 1 to go to Account Holder Menu" '\n' "Enter 2 to go to Manager Menu")

def show_account_holder_menu():
    print("Enter 1 to Register" '\n' "Enter 2 to log into your account" '\n' "Enter 0 to go back" '\n')

def show_manager_menu():
    print('Enter 0 to go back' '\n' "Enter 1 to create a manager account" '\n' "Enter 2 to log into your manager account" '\n')


def show_sub_menu(option):
    if option == 0:
        mainMenu()
    elif option == 1:
        show_account_holder_menu()
        action = int(input('Please choose an option from the above options: '))
        if action == 0:
            mainMenu()
        else:
            handle_account_holder_menu(action)

    elif option == 2:
        show_manager_menu()
        action = int(input('Please choose an option from the above options: '))
        if action == 0:
            mainMenu()
        else:
            handle_manager_menu(action)
        
        

def handle_account_holder_menu(action):
    if action == 1:
        email = str(input('Input your email address: ' '\n'))

        password = str(input('Input the password of your choice: ' '\n'))
        
        confirm_password = str(input('Confirm your password: ' '\n'))

        first_name = str(input('Input your first name: ' '\n'))

        middle_name = str(input('Input your middle name.' '\n'))

        last_name = str(input('Input your last name:'  '\n'))
        
        phone = str(input('Input your phone number:' '\n'))

        pin = int(input('Enter your 4 digit pin: ' '\n'))

        holder = acount_holder_manager.create_account_holder(email=email, password=password, confirm_password=confirm_password,
        
                                                             first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
        

        
        if holder is True:
            account_number = account_manager.create_account(account_holder=holder, pin=pin)
            print('Account created, Your account number is: ', account_number)

        else:
            print('ACCOUNT COULD NOT BE CREATED SUCESSFULLY' '\n')

    elif action == 2:

        
        email = str(input('Input your email address: ' '\n'))
        
        password = str(input('Input your password: ' '\n'))
        
        holder = acount_holder_manager.login(email=email, password=password)

        if holder is not None:

            if holder is False:
                print('EMAIL OR PASSWORD INCORRECT'  '\n')

            else:             

                print('SUCESSFULLY LOGGED IN' '\n' '\n' 'Enter 1 to change your password' '\n' 'Enter 2 to search for your account' '\n'
                'Enter 3 to delete your account' '\n' 'Enter 4 to deposit into your account' '\n'
                'Enter 5 to withdraw' '\n' 'Enter 6 to collect a loan' '\n' 'Enter 7 to collect an overdraft')

                action2 = int(input('Please choose one of the following options: ' '\n'))

                if action2 == 0:
                    show_account_holder_menu()

                            
                elif action == 1:
                    email = str(input('Enter your email address: '))
                    new_password = str(input('Enter the new password: '))
                    status = acount_holder_manager.change_password(
                        email=email, new_password=new_password)
                    if status is True:
                        print('Password is valid')
                    else:
                        print('information invalid')

                elif action2 == 2:
                    email = str(input('Input your email address: ' '\n'))

                    holder = acount_holder_manager.search(email=email)
                    
                    if holder is False:
                        print('ACCOUNT NOT FOUND'  '\n')


                elif action2 == 3:
                    
                    email = str(input('Input your email address: ' '\n'))
                    
                    password = str(input('Input your password: ' '\n'))
                    
                    holder = acount_holder_manager.login(email=email, password=password)
                    
                    if holder is False:
                        print('PASSWORD INVALID'  '\n')
                    else:
                        status = acount_holder_manager.delete_account_holder(email=email)
                        if status is True:
                            print('ACCOUNT DELETED SUCESSFULLY'  '\n')
                        else:
                            print('ACCOUNT NOT DELTED' '\n')


                elif action2 == 4:
                    account_number = str(input('Enter Your Account Number: '))
                    pin = int(input('Enter Your Pin: '))
                    amount = float(input('Enter the amount you want to deposit: '))
                    status = account_manager.deposit(pin=pin, amount=amount, account_number=account_number)
                    if status is False:
                        print('Operation unsuccessful')
                    else:
                        print('Operation successful')

                elif action2 == 5:
                    account_number = str(input('Enter Your Account Number: '))
                    pin = int(input('Enter Your Account Pin: '))
                    amount = float(input('Enter the amount you want to withdraw: '))
                    status = account_manager.withdraw(pin=pin, amount=amount, account_number=account_number)
                elif action2 == 6:
                    account_number = str(input('Enter Your account Number: '))
                    pin = int(input('Enter Your pin: '))
                    print(
                        'Enter 0 for Household Loan Amount: 'f'{loan_manager.loan_types.get("household")}"\n' 'Enter 1 for Car Loan: '
                        f'{loan_manager.loan_types.get("car")}"\n' 'Enter 2 for School fees Loan: 'f'{loan_manager.loan_types.get("school fee")}" \n' 'Enter 3 For Business Loan: '
                        f'{loan_manager.loan_types.get("business")}"\n' 'Enter 4 for Emergency loan: 'f'{loan_manager.loan_types.get("emergency")}"')
                    val = int(input())
                    def handle_loan_type(val: int):
                        loan_names = ['household', 'car', 'school fee', 'business', 'emergency']
                        for name in range(len(loan_names)):
                            if val == name:
                                return loan_names[name]
                    
                    loan_type = handle_loan_type(val)
                    number_of_mounts = int(input('Enter numbers of months to pay back: '))
                    account = account_manager.return_account(account_number=account_number, pin=pin)
                    loan = loan_manager.create_loan(account=account, loan_type=loan_type, number_of_months=number_of_mounts)
                    try:
                        if loan['not_granted']:
                            print(loan['not_granted'])
                    except KeyError:
                        print(loan['message'])
                elif action2 == 7:
                    account_number = str(input('Input your account number:' '\n'))
                    pin = int(input('Enter your pin' '\n'))
                    amount = float(input('Enter the ammount you want to collect as overdraft' '\n'))
                    account = account_manager.return_account(account_number=account_number, pin=pin)
                    response = overdraft_manager.create_overdraft(account=account, amount=amount)
                    print(response)


        else:
            print('NO ACCOUNT HAS BEEN REGISTERED INTO THIS SYSTEM. REGISTER AN ACCOUNT INTO THIS SYSTEM FIRST BEFORE YOU CAN LOG INTO YOUR ACCOUNT')    


    show_sub_menu(1)



def show_manager_login_menu():
        print('Enter 1 to update your manager details' '\n' 'Enter 2 to change your password' '\n' 'Enter 3 to display your details' '\n'
            'Enter 4 to block an account' '\n' 'Enter 5 to unblock an account' '\n' 'Enter 6 to display all account holders' '\n' 'Enter 7 to list all loans in the system' '\n'
             'Enter 8 to search for a loan' '\n' 'Enter 9 to list all loans in the system' '\n' 'Enter 10 to search for a loan')



def handle_manager_menu(action):
    if action == 1:
        first_name = str(input('Input your first name:' '\n'))

        middle_name = str(input('Input your middle name:' '\n'))

        last_name = str(input('Input your last name:' '\n'))

        phone = input('Input your phone number:' '\n')

        email = str(input('What is your email address:' '\n'))

        password = str(input('What is your password? ' '\n'))

        confirm_password = str(input('Confirm your password: ' '\n'))

        manager = manager_man.create_manager(email=email, password=password, confirm_password=confirm_password, first_name=first_name, middle_name=middle_name,  last_name=last_name, phone=phone)

        if manager is True:
            print('MANAGER ACCOUNT CREATION SUCESSFUL'  '\n')
        else:
            print('WRONG ACCOUNT DETAILS' '\n' )

    
    elif action == 2:
        email = str(input('Input your email address: ' '\n'))

        password = str(input('Input your password: ' '\n'))

        manager = manager_man.login(email=email, password=password)

        if manager is not None:

            if manager is False:
                print('YOUR PASSWORD IS INCORRECT'  '\n')
            else:
                show_manager_login_menu()
                action = int(input('Please choose one of the following options' '\n'))


                if action == 0:
                    show_manager_menu()

        
                elif action == 1:
                    first_name = str(input('Input your first name: ' '\n'))

                    last_name = str(input('Input your last name: ' '\n'))

                    middle_name = str(input('Input your last name: ' '\n'))

                    phone = str(input('Input your phone number: ' '\n'))

                    new_holder = manager_man.update_manager(email=email, first_name=first_name, last_name=last_name, middle_name=middle_name, phone=phone, password=password)

                    if new_holder is True:
                        print('UPDATE SUCESSFUL'  '\n')
                    else:
                        print('UPDATE NOT SUCESSFUL'  '\n')


                elif action == 2:
                    email = str(input('Input your email address: ' '\n'))

                    new_password = str(input('Input the new password: ' '\n'))

                    status = manager_man.change_password(email=email, new_password=new_password)

                    if status is True:
                        print('INFORMATION IS VALID'  '\n')
                    else:
                        print('INFORMATION IS INVALID' '\n')

                elif action   == 3:
                    manager_man.show_manager()
                    

                elif action == 4:
                    account_number = str(input('Input your account number: '))
                    account_manager.block_account(account_number=account_number)

                elif action == 5:
                    account_number = str(input('Input your account number: '))
                    account_manager.unblock_account(account_number=account_number)

                elif action == 6:
                    acount_holder_manager.list_account_holders()

                elif action == 7:
                    loan_manager.list_loan()
                    
                elif action == 8:
                    account_number = str(input('Input the account number: ' '\n'))

                    holder = loan_manager.search(account_number=account_number)
                    
                    if holder is False:
                        print('NO LOAN HAS BEEN COLLECTED BY THIS USER'  '\n')
                
                elif action == 9:
                    overdraft_manager.list_overdraft()

                elif action == 10:
                    account_number = str(input('Input  the aaccount number: ' '\n'))

                    holder = overdraft_manager.search(account_number=account_number)

                    if holder is False:
                        print('NO OVERDRAFT HAS BEEN COLLECTED BY THIS USER ' '\n') 
        
        else:
            print('NO MANAAGER ACCOUNT HAS BEEN REGISTERED INTO THIS SYSTEM. PLEASE REGISTER A MANAGER ACCOUNT')
    

        show_sub_menu(2)


def main():
    flag = True
    while(flag):
        mainMenu()
        option = int(input())
        if(option == 0):
            flag = False
        else:
            show_sub_menu(option)


main()

