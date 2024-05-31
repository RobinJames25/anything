from user import User
class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges=Privileges()#Make a Privileges instance as an attribute in the Admin class
        # self.privileges_list=[]

    
class Privileges():
    def __init__(self) :
        self.privileges_list=[]

    def show_privileges(self):
        print("Below are a list of privileges for the admin: ")
        for privilege in self.privileges_list:
            print("-" + privilege.title())