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


first_restaurant = Restaurant('嘤嘤婴','bacon')
print('\nThe restaurant info is ')
first_restaurant.describe_restaurant()

second_restaurant = Restaurant('bbb','checkin')
print('\nThe restaurant info is ')
second_restaurant.describe_restaurant()

third_restaurant = Restaurant('ccc','beef')
print('\nThe restaurant info is ')
third_restaurant.describe_restaurant()