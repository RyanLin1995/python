class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year = year

    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' ' +
              '-kwh nattry.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range = 270

        messange = 'This car go approximately ' + str(range)
        messange += ' miles on a full charge.'
        print(messange)

    def upgrade_batterty(self):
        if self.battery_size != 85:
            self.battery_size = 85

class Electric(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

new_car = Electric('audi','a6',2020)
print(new_car.get_descriptive())
new_car.battery.describe_battery()
new_car.battery.get_range()
new_car.battery.upgrade_batterty()
new_car.battery.get_range()