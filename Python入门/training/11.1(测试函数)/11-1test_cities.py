import unittest
from city_functions_1 import city_info

class CityTest(unittest.TestCase):
    '''测试城市信息是否通过'''

    def test_city_info(self):
        '''能正确处理Foshan, China这样的城市信息吗?'''
        info = city_info('foshan', 'china')
        self.assertEqual(info, 'Foshan, China')

unittest.main()





