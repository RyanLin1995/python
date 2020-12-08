class User():
    """模拟一个用户简介"""
    def __init__(self,first_name,last_name,age,location):
        """初始化人物简介值"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        #print('First name is: ' + self.first_name.title())
        #print('Last name is: ' + self.last_name.title())
        #print('Age is: ' + str(self.age))
        #print('Location is: ' + self.location.title())
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        return full_name

    def greet_user(self):
        print('Welcome to KN!')


user = User('lily','xu','22','foshan')
print(user.describe_user())
user.greet_user()




