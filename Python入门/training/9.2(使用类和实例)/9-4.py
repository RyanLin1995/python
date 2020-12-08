class Restaurant():
    """一个餐厅的模拟"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅名字和菜式的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\nRestaurant Name: ' + self.restaurant_name.title())
        print('Restaurant Cuisine_Type: ' + self.cuisine_type.title())

    def open_restaurant(self):
        print('The restaurant is opening')

    def set_number_served(self,numbers):
        self.number_served = numbers
        print('There are ' + str(self.number_served) + ' ' +
              'customers come to our restaurant.')

    def increment_number_served(self,number):
        self.number_served += number
        print('We can serve up to ' + str(self.number_served) + ' ' + 'people')


restaurant = Restaurant('嘤嘤婴','bacon')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(55)
restaurant.increment_number_served(65)