'''
File contains tests for command_line.py 
'''
import unittest
from command_line import get_price_data, getEmissionData, getData, main
from test_constants import valid_ca_table, valid_ga_e_table, valid_wa_nm_table
import sys
from io import StringIO

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

class TestGetEmissionData(unittest.TestCase):
    def test_valid_state(self):
        data = getEmissionData("MN")
        self.assertIsInstance(data, dict)
        for k in ["generation", "thermalOutput", "totalFuelConsumption",
                  "totalFuelConsumptionGeneration", "co2Tons", "co2MetricTons"]:
            self.assertIn(k, data)
    
    def test_invalid_state(self):
        with self.assertRaises(KeyError):
            getEmissionData("XX")
    
    def test_US(self):
        us = getEmissionData("US")
        mn = getEmissionData("MN")
        self.assertGreaterEqual(us["co2Tons"], mn["co2Tons"])

class TestGetData(unittest.TestCase):
    def test_emissions_only(self):
        states = ["MN", "ND"]
        flags = [False, True]

        entries = getData(states, flags)
        self.assertEqual(len(entries), 2)

        for entry in entries:
            self.assertIn("state", entry)
            self.assertIn("year", entry)
            self.assertIn("co2Tons", entry)

    def test_both_flags(self):
        states = ["MN"]
        flags = [True, True]

        entries = getData(states, flags)
        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertIn("co2Tons", entry) 
        self.assertIn("totalPrice", entry)  

class TestCommandLine(unittest.TestCase):
    """Full stack tests for the command_line"""
    def test_one_state(self):
        """test one state input"""
        sys.argv = ['command_line.py', 'CA']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_ca_table)
    def test_one_state_flags(self):
        """test one state with flags"""
        sys.argv = ['command_line.py', '-e', 'GA']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_ga_e_table)
    def test_multiple_states(self):
        """test two states and US because why not knock two birds with one stone""" 
        sys.argv = ['command_line.py', 'WA', 'NM']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_wa_nm_table)