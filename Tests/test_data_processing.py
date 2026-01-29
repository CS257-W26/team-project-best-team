"""tests for data_processing module"""

import unittest
from ProductionCode.data_processing import format_string

class TestFormating(unittest.TestCase):
    """tests data_processing module formating functions"""
    def test_format_string(self):
        """test format_string function"""
        self.assertEqual(format_string('4000'), '4,000')
        self.assertEqual(format_string('63.6432'), '63.64')
        self.assertEqual(format_string('str'), 'str')