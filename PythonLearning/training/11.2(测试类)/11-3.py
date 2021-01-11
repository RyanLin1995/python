import unittest
from employee import Employee

class TestEmployees(unittest.TestCase):
    '''这是一个雇员的测试'''

    def setUp(self):
        '''创建一个雇员和雇员的年薪'''
        self.employee = Employee('ryan', 'lin', 12000)

    def test_give_default_raise(self):
        """测试默认年薪增加500元"""
        self.assertEqual(self.employee.give_raise(), 12500)

    def test_give_custom_raise(self):
        '''测试其他年薪增加值'''
        self.assertEqual(self.employee.give_raise(2000), 14000)

unittest.main()
