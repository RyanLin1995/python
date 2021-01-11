class User():
    """模拟一个用户简介"""
    def __init__(self,first_name,last_name,age,location):
        """初始化人物简介值"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print('First name is: ' + self.first_name.title())
        print('Last name is: ' + self.last_name.title())
        print('Age is: ' + str(self.age))
        print('Location is: ' + self.location.title())

    def greet_user(self):
        print('Welcome to KN!')

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

Admin = Admin('ryan','lin',25,'foshan')
Admin.describe_user()
Admin.greet_user()
Admin.privileges.show_privileges()