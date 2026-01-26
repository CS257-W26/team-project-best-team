import unittest
from ProductionCode.dataRetrieval import get_price_data_state, aggregate_month_data_sales, to_num_or_zero, fixed_dict_format
if __name__ == '__main__':
    unittest.main()
class dataRetrievalTest(unittest.TestCase):
    maxDiff=None
    def test_get_price_data_state_KS24(self):
        '''
        Docstring for test_get_price_data_state_KS24
        Given valid input outputs correct output
        :param self: part of class
        '''
        data_ks24 = get_price_data_state("KS", 2024)
        self.assertEqual(data_ks24["residentialRevenue"],1958283)
        self.assertEqual(data_ks24["totalPrice"], 11.15)
        self.assertEqual(data_ks24["commercialSales"],15790721)
    def test_get_price_data_state_bad_state(self):
        '''
        Docstring for test_get_price_data_state_bad_state
        Tests that empty values are giving for invalid input (state)
        :param self: Description
        '''
        data_bad = get_price_data_state("America", 2024)
        self.assertEqual(data_bad["state"], "America")
        self.assertEqual(data_bad["residentialRevenue"], 0)
    def test_get_price_data_state_bad_year(self):
        '''
        Docstring for test_get_price_data_state_bad_year
        Tests that empty values are giving for invalid input (year)
        :param self: Description
        '''
        data_bad = get_price_data_state("KS", 2030)
        self.assertEqual(data_bad["state"], "KS")
        self.assertEqual(data_bad["residentialRevenue"], 0)
    def test_aggregate(self):
        '''
        Docstring for test_aggregate
        Tests that aggregate_month_data_sales is able to take inputs in form of list of lists and output dict
        :param self: Description
        '''
        test_AL1025 = [2025,10,"AL","Preliminary","382,814","2,289,572","2,434,519",16.72,"274,505","1,869,742","397,623",14.68,"202,443","2,730,802","7,256",7.41,0,0,0,0.00,"859,762","6,890,116","2,839,398",12.48]
        test_AL925 = [2025,9,"AL","Preliminary","480,720","2,926,702","2,435,862",16.43,"302,522","2,097,871","397,761",14.42,"217,753","2,788,836","7,269",7.81,0,0,0,0.00,"1,000,995","7,813,408","2,840,892",12.81]
        #Prolly coulda just checked a few values were equal but alas
        self.assertEqual(aggregate_month_data_sales([test_AL1025,test_AL925]), 
                         {"residential": {"revenue": 863534, "sales": 5216274, "customers": 2435190, "priceAvg": 16.57},
                          "commercial": {"revenue": 577027, "sales": 3967613, "customers": 397692, "priceAvg": 14.55},
                          "industrial": {"revenue": 420196, "sales": 5519638, "customers": 7262, "priceAvg": 7.61},
                          "transportation": {"revenue": 0, "sales": 0, "customers": 0, "priceAvg": 0.00},
                          "total": {"revenue": 1860757, "sales": 14703524, "customers": 2840145, "priceAvg": 12.64}}
                         )
    def test_num_or_zero_comma(self):
        '''
        Docstring for test_num_or_zero_comma
        Checks that entries with commas are properly converted to float format
        :param self: Description
        '''
        self.assertEqual(to_num_or_zero("234,543"), 234543.0)
    def test_num_or_zero_period(self):
        '''
        Docstring for test_num_or_zero_period
        Checks that entries that are '.' are properly converted to 0.0
        :param self: Description
        '''
        self.assertEqual(to_num_or_zero("."), 0.0)
    def test_fixed_dict_formatting_AL(self):
        '''
        Docstring for test_fixed_dict_formatting
        Tests that given an output from aggregate_month_data_sales and the proper state, will make proper dictionary format
        :param self: Description
        '''
        badFormatDict = {"residential": {"revenue": 863534, "sales": 5216274, "customers": 4870381, "priceAvg": 16.57},
                          "commercial": {"revenue": 577027, "sales": 3967613, "customers": 795384, "priceAvg": 14.55},
                          "industrial": {"revenue": 420196, "sales": 5519638, "customers": 14525, "priceAvg": 7.61},
                          "transportation": {"revenue": 0, "sales": 0, "customers": 0, "priceAvg": 0.00},
                          "total": {"revenue": 1860757, "sales": 14703524, "customers": 5680290, "priceAvg": 12.64}}
        self.assertEqual(fixed_dict_format(badFormatDict, "AL"), 
                         {
                            "state": "AL", "year":2025, 
                            "residentialRevenue":863534, "residentialSales":5216274, "residentialCustomers":4870381, "residentialPrice":16.57,
                            "commercialRevenue":577027, "commercialSales":3967613, "commercialCustomers":795384, "commercialPrice":14.55,
                            "industrialRevenue":420196, "industrialSales":5519638, "industrialCustomers":14525, "industrialPrice":7.61,
                            "transportationRevenue":0, "transportationSales":0, "transportationCustomers":0, "transportationPrice":0.00,
                            "totalRevenue":1860757, "totalSales":14703524, "totalCustomers":5680290, "totalPrice":12.64,
                          }
                         )
    def test_fixed_dict_formatting_US(self):
        '''
        Docstring for test_fixed_dict_formatting
        Tests that given an output from aggregate_month_data_sales and the proper state, will make proper dictionary format
        :param self: Description
        '''
        badFormatDict = {"residential": {"revenue": 863534, "sales": 5216274, "customers": 4870381, "priceAvg": 16.57},
                          "commercial": {"revenue": 577027, "sales": 3967613, "customers": 795384, "priceAvg": 14.55},
                          "industrial": {"revenue": 420196, "sales": 5519638, "customers": 14525, "priceAvg": 7.61},
                          "transportation": {"revenue": 0, "sales": 0, "customers": 0, "priceAvg": 0.00},
                          "total": {"revenue": 1860757, "sales": 14703524, "customers": 5680290, "priceAvg": 12.64}}
        self.assertEqual(fixed_dict_format(badFormatDict, "US"), 
                         {
                            "state": "US", "year":2025, 
                            "residentialRevenue":863534, "residentialSales":5216274, "residentialCustomers":248389431, "residentialPrice":16.57,
                            "commercialRevenue":577027, "commercialSales":3967613, "commercialCustomers":40564584, "commercialPrice":14.55,
                            "industrialRevenue":420196, "industrialSales":5519638, "industrialCustomers":740775, "industrialPrice":7.61,
                            "transportationRevenue":0, "transportationSales":0, "transportationCustomers":0, "transportationPrice":0.00,
                            "totalRevenue":1860757, "totalSales":14703524, "totalCustomers":289694790, "totalPrice":12.64,
                          }
                         )
