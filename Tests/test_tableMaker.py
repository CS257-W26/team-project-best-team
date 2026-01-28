"""Tests for TableMaker class"""

import unittest
import sys
from io import StringIO
from ProductionCode.table_maker import TableMaker
from command_line import getData
from Tests.test_constants import valid_table, valid_mn_table, valid_us_price_table, valid_nd_sd_table

class TestTableMakerInput(unittest.TestCase):
    """Tests the TableMaker class input functions"""
    def setUp(self):
        """setup"""
        self.table = TableMaker()
    def test_add_new_empty_entry(self):
        """test add_new_empty_entry function"""
        self.table.add_new_empty_entry('MN', "2025")
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025")     
    def testfail_add_new_empty_entry(self):
        """test add_new_empty_entry function fail cases"""
        self.table.add_new_empty_entry('MN', "2025")
        with self.assertRaises(KeyError):
            self.table.add_new_empty_entry('MN', "2025")
    def test_add_new_entry(self):
        """test add_new_entry function"""
        self.table.add_new_entry({'state':'MN', 'year':'2025', 'totalPrice':'25.6'})
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025") 
        self.assertEqual(self.table.entries[-1].get("totalPrice"), "25.6")
    def testfail_add_new_entry(self):
        """test add_new_entry function fail cases"""
        with self.assertRaises(TypeError):
            self.table.add_new_entry("dict")
        self.table.add_new_entry({'state':'MN', 'year':'2025', 'totalPrice':'25.6'})
        with self.assertRaises(KeyError):
            self.table.add_new_entry({'state':'MN', 'year':'2025', 'co2Tons':'5000'})
    def test_add_data_for_entry(self):
        """test add_data_for_entry function"""
        self.table.add_new_empty_entry('MN', "2025")
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025") 
        self.table.add_data_for_entry('MN', '2025', ('co2Tons', '5000')) 
        self.assertEqual(self.table.entries[-1].get("co2Tons"), "5000") 
    def testfail_add_data_for_entry(self):
        """test add_data_for_entry function fail cases"""
        self.table.add_new_empty_entry('MN', "2025")
        with self.assertRaises(TypeError):
            self.table.add_data_for_entry('MN', "2024", {'co2Tons': '5000'})
        with self.assertRaises(KeyError):
            self.table.add_data_for_entry('MN', "2024", ('co2Tons', '5000'))

class TestTableMakerOutput(unittest.TestCase):
    """Test the TableMaker class output functions"""
    def setUp(self):
        """setup"""
        self.table = TableMaker()
        self.table.add_new_entry({"state": "MN", "year": "1990"})
        self.table.add_new_entry({"state": "WY", "year": "2005" , "totalRevenue" : "1.2"})
        self.table.add_new_empty_entry("US", "2026")
        self.table.add_data_for_entry("US", "2026", ("co2Tons", "50000000"))
        self.table.add_data_for_entry("MN", "1990", ("totalFuelConsumptionGeneration", "100"))
    def test_format_entry(self):
        """test format_entry function"""
        self.assertEqual(self.table.format_entry('4000'), '4,000')
        self.assertEqual(self.table.format_entry('63.6432'), '63.64')
        self.assertEqual(self.table.format_entry('str'), 'str')
    def test_get_col_sizes(self):
        """test get_col_sizes function"""
        self.assertEqual(self.table.get_col_sizes(), [5,5,11])
    def test_is_row_empty(self):
        """test is_row_empty function"""
        self.assertFalse(self.table.is_row_empty('co2Tons'))
        self.assertTrue(self.table.is_row_empty('generation'))
    def test_print_table(self):
        """test a simple table print"""
        sys.stdout = StringIO()
        self.table.print_table()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_table)
    
class TestTableOutputUserStories(unittest.TestCase):
    maxDiff=None
    def test_us_display(self):
        us_price_data = getData(["US"], [True, False])
        us_table = TableMaker()
        us_table.add_new_entry(us_price_data[0])
        sys.stdout = StringIO()
        us_table.print_table()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_us_price_table)
    def test_two_state_display(self):
        two_state_data = getData(["ND", "SD"], [True, True])
        two_state_table = TableMaker()
        two_state_table.add_new_entry(two_state_data[0])
        two_state_table.add_new_entry(two_state_data[1])
        sys.stdout = StringIO()
        two_state_table.print_table()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_nd_sd_table)
    def test_single_state_display(self):
        one_state_data = getData(["MN"], [True, True])
        one_state_table = TableMaker()
        one_state_table.add_new_entry(one_state_data[0])
        sys.stdout = StringIO()
        one_state_table.print_table()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_mn_table)


if __name__ == '__main__':
    unittest.main()
