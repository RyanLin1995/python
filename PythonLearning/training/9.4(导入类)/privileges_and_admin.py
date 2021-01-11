'''一个表示权限的类'''
from user import User
class Privileges():
    def __init__(self):
        self.privileges = ['add post' ,'delete post' ,'ban user']

    def show_privileges(self):
        print("\nThe admin peivileges with: ")
        for self.privilege in self.privileges:
            print(self.privilege.title())

class Admin(User):
    """这是一个继承了父类User的子类"""
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges = Privileges()