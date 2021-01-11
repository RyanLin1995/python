"""一个用户表示餐厅的类"""

class Restaurant():
    """一个餐厅的模拟"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅名字和菜式的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Name: ' + self.restaurant_name.title())
        print('Cuisine_Type: ' + self.cuisine_type.title())

    def open_restaurant(self):
        print('\nThe restaurant is opening')


class IceCreamStand(Restaurant):
    '''这是一个继承了Restaurant父类的子类'''
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate' ,'strawberry' ,'matcha']

    def flavor(self):
        print('\nIce cream has the following flavors: ')
        for self.flavor in self.flavors:
            print(self.flavor.title())