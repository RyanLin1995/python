"""一个用户表示用户的类"""
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