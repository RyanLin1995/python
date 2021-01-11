class Employee():
    '''一个模拟雇员的类'''
    def __init__(self, first_name, last_name, annual_salary):
        '''初始化雇员的属性'''
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_annual_salary = 500):
        '''默认年薪增加500'''
        self.annual_salary += raise_annual_salary
        return self.annual_salary
