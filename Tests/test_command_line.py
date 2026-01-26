import unittest
from command_line import get_price_data, get_US_data
import sys
from io import StringIO
from command_line import main

if __name__ == '__main__':
    unittest.main()

class commandLineTestRW(unittest.TestCase):
    maxDiff=None
    def test_get_price_data_KS25(self):
        '''
        Docstring for test_get_price_data_KS25
        Test getPriceData function from command_line.py
        :param self: Description
        '''
        data_ks24 = get_price_data("KS")
        self.assertEqual(data_ks24["residentialRevenue"],1769141)
        self.assertEqual(data_ks24["totalPrice"], 11.46)
        self.assertEqual(data_ks24["commercialSales"],13728250)
    def test_get_us_data(self):
        '''
        Docstring for test_get_us_data
        Test getUSData function from command_line.py
        :param self: Description
        '''
        usData = get_US_data()
        self.assertEqual(usData["state"], "US")
        self.assertEqual(usData["commercialSales"], 1246808835)
        self.assertEqual(usData["transportationPrice"], 12.13)
class TestCommandLine(unittest.TestCase):
    def test_normal_query(self):
        """test a valid state in the command line interface"""
