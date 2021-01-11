import unittest
from city_functions_2 import city_info_2

class Citytest(unittest.TestCase):
    """测试新的城市信息是否能通过"""
    def test_city_info(self):
        """能正确处理新的Foshan, China这样的城市信息吗?"""
        info = city_info_2('foshan', 'china')
        self.assertEqual(info,'Foshan, China')

    def test_city_info_population(self):
        """能正确处理新的Foshan, China -population xxx这样的城市信息吗?"""
        info_population = city_info_2('foshan', 'china', 200000)
        self.assertEqual(info_population,"Foshan, China -population 200000")

unittest.main()