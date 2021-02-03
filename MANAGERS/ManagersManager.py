from MODELSA.manager import Manager 




class ManagersManager:
    manager_list = []
    
    def create_manager(self, email: str, password: str, confirm_password: str, first_name: str, middle_name, last_name, phone):
        themanager = Manager(email=email, first_name=first_name, password=password)
        themanager.middle_name = middle_name
        themanager.last_name = last_name
        themanager.phone = phone
        self.manager_list.append(themanager)
        return True

    
    def update_manager(self, email: str, first_name: str, last_name: str, password: str, middle_name: str, phone: str):
        manager = self.__find(email)
        if manager is not None:
            manager.first_name = first_name
            manager.last_name = last_name
            manager.middle_name = middle_name
            manager.phone = phone
            return True
        else:
            return False
        
    def show_manager(self):
        # Print all account_holder
        for manager in self.manager_list:
            self.__show(manager)

    def login(self, email: str, password: str):
        # verify if the person trying to access an account is the owner
        for manager in self.manager_list:
            if manager.email == email and manager.password == password:
                return manager
            else:
                return False


    def change_password(self, email: str, new_password: str):
        manager = self.__find(email)
        if manager != None:
            manager.change_password(password=new_password)
        else:
            return False


    def __find(self, email: str):
        # Finds the account holder by the given email in the account holder list a private function
        for manager in self.manager_list:
            if manager.email == email:
                return manager
            else:
                return None



    def __show(self, manager: Manager):
        #print(manager.first_name, ' ', manager.middle_name, ' ', manager.last_name, '\t', manager.email, '\t', manager.phone)
        print('MANAGER NAME: ' + manager.first_name + ' ' + manager.middle_name + ' ' + manager.last_name, '\n' 'MANAGER EMAIL ' + manager.email, '\n' 'MANAGER PHONE NUMBER: ' + manager.phone )

