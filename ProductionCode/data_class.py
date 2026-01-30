import csv
class Data:
    '''
    Class which will handle loading of all the data into one dictionary,
    each key in dictionary will be StateYear ie "MN2024"
    access an entry with data.data_dict["MN2024"]["generation"]
    to add a dictionary to table: data.data_dict["MN2024"]
    '''
    def __init__(self):
        self.data_dict = {}

    def to_num_or_zero(entry):
        '''
        Docstring for self.to_num_or_zero
        converts the entry for the data into a numeric type
        :param entry: the value for a specific cell in data set
        :return : returns the value of the cell as a float
        '''
        if entry is None:
            return 0
        if isinstance(entry, (int, float)):
            value = float(entry)
        elif isinstance(entry, str):
            entry = entry.strip().strip('"')
            if entry == "." or entry == "":
                return 0
            entry = entry.replace(",", "")
            try:
                value = float(entry)
            except ValueError:
                return 0
        else: return 0
        if value.is_integer():
            return int(value)
        else:
            return round(value, 2)
    
    def average_customers_prices(self):
        '''
        Docstring for average_customers_prices
        sets the values for customer and prices to the averages 
        :param self: Description
        :return: Description
        :rtype: type[dict]
        '''
        customer_fields = ["residentialCustomers", "commercialCustomers", 
                  "industrialCustomers", "transportationCustomers", "totalCustomers", ]
        price_fields = ["residentialPrice","commercialPrice","industrialPrice","transportationPrice","totalPrice"]
        for key in self.data_dict:
            num_months = 12
            if self.data_dict[key]["year"] == 2025:
                num_months = 10
            for customer, price in zip(customer_fields, price_fields):
                self.data_dict[key][customer] = self.data_dict[key][customer] / num_months
                self.data_dict[key][price] = round(self.data_dict[key][price]/num_months, 2)
                if self.data_dict[key]["state"] == "US":
                    self.data_dict[key][customer] *= 51 
                
    def load_price_row(self, row):
        '''
        Docstring for load_price_row
        
        :param self: Description
        :param row: row from csv file to be reader, form of list
        :return: Description
        :rtype: type[dict]
        '''
        state_year_key = row[2] + str(row[0])
        if state_year_key not in self.data_dict:
            self.data_dict[state_year_key] = {}
            self.data_dict[state_year_key]["state"] = row[2]
            self.data_dict[state_year_key]["year"] = int(row[0])
        field_names = ["Revenue", "Sales", "Customers", "Price"]
        sales_types = {
            "residential":  (4, 5, 6, 7),
            "commercial":   (8, 9, 10, 11),
            "industrial":   (12, 13, 14, 15),
            "transportation": (16, 17, 18, 19),
            "total":        (20, 21, 22, 23),
        }
        #key = row[2] + str(row[0])
        empty_price_count = 0
        i = 1
        for type, idxs in sales_types.items():
            for field_name, idx in zip(field_names, idxs):
                key = type + field_name

                if field_name == "Price" and self.self.to_num_or_zero(row[idx]) == 0:
                    empty_price_count += 1

                self.data_dict[state_year_key][key] = (
                    self.data_dict[state_year_key].get(key, 0)
                    + self.to_num_or_zero(row[idx])
                )

    def load_us_price_data(self):
        for year in range(2013,2026):
            self.load_us_price_data_for_year(year)


    def load_us_price_data_for_year(self,year):
        '''
        Docstring for load_us_price_data
        adds data for US for year to self.data_dict
        :param self: Description
        :param year: year for us data
        :rtype: type[dict]
        '''
        us_year_key = "US" + str(year)
        if us_year_key not in self.data_dict:
            self.data_dict[us_year_key] = {}
            self.data_dict[us_year_key]["state"] = "US"
            self.data_dict[us_year_key]["year"] =int(year)
        for key in self.data_dict.keys():
            if self.data_dict[key]["year"] != year and self.data_dict[key]["state"] == "US":
                continue
            #This will all be replaced with like a mapping but not rn
            self.data_dict[us_year_key]["residentialRevenue"] = self.data_dict[us_year_key].get("residentialRevenue", 0) + self.data_dict[key]["residentialRevenue"]
            self.data_dict[us_year_key]["residentialSales"] = self.data_dict[us_year_key].get("residentialSales", 0) + self.data_dict[key]["residentialSales"]
            self.data_dict[us_year_key]["residentialCustomers"] = self.data_dict[us_year_key].get("residentialCustomers", 0) + self.data_dict[key]["residentialCustomers"]
            self.data_dict[us_year_key]["residentialPrice"] = self.data_dict[us_year_key].get("residentialPrice", 0) + self.data_dict[key]["residentialPrice"]
            self.data_dict[us_year_key]["commercialRevenue"] = self.data_dict[us_year_key].get("commercialRevenue", 0) + self.data_dict[key]["commercialRevenue"]
            self.data_dict[us_year_key]["commercialSales"] = self.data_dict[us_year_key].get("commercialSales", 0) + self.data_dict[key]["commercialSales"]
            self.data_dict[us_year_key]["commercialCustomers"] = self.data_dict[us_year_key].get("commercialCustomers", 0) + self.data_dict[key]["commercialCustomers"]
            self.data_dict[us_year_key]["commercialPrice"] = self.data_dict[us_year_key].get("commercialPrice", 0) + self.data_dict[key]["commercialPrice"]
            self.data_dict[us_year_key]["industrialRevenue"] = self.data_dict[us_year_key].get("industrialRevenue", 0) + self.data_dict[key]["industrialRevenue"]
            self.data_dict[us_year_key]["industrialSales"] = self.data_dict[us_year_key].get("industrialSales", 0) + self.data_dict[key]["industrialSales"]
            self.data_dict[us_year_key]["industrialCustomers"] = self.data_dict[us_year_key].get("industrialCustomers", 0) + self.data_dict[key]["industrialCustomers"]
            self.data_dict[us_year_key]["industrialPrice"] = self.data_dict[us_year_key].get("industrialPrice", 0) + self.data_dict[key]["industrialPrice"]
            self.data_dict[us_year_key]["transportationRevenue"] = self.data_dict[us_year_key].get("transportationRevenue", 0) + self.data_dict[key]["transportationRevenue"]
            self.data_dict[us_year_key]["transportationSales"] = self.data_dict[us_year_key].get("transportationSales", 0) + self.data_dict[key]["transportationSales"]
            self.data_dict[us_year_key]["transportationCustomers"] = self.data_dict[us_year_key].get("transportationCustomers", 0) + self.data_dict[key]["transportationCustomers"]
            self.data_dict[us_year_key]["transportationPrice"] = self.data_dict[us_year_key].get("transportationPrice", 0) + self.data_dict[key]["transportationPrice"]
            self.data_dict[us_year_key]["totalRevenue"] = self.data_dict[us_year_key].get("totalRevenue", 0) + self.data_dict[key]["totalRevenue"]
            self.data_dict[us_year_key]["totalSales"] = self.data_dict[us_year_key].get("totalSales", 0) + self.data_dict[key]["totalSales"]
            self.data_dict[us_year_key]["totalCustomers"] = self.data_dict[us_year_key].get("totalCustomers", 0) + self.data_dict[key]["totalCustomers"]
            self.data_dict[us_year_key]["totalPrice"] = self.data_dict[us_year_key].get("totalPrice", 0) + self.data_dict[key]["totalPrice"]

    def load_emission_data(self):
        with open("Data/state_year_power_summary.csv", mode='r') as emission_file:
            reader = csv.DictReader(emission_file)
            for row in reader:
                key = row.get("State") + str(row.get("Year"))
                self.data_dict[key]["generation"] = self.self.to_num_or_zero(row.get("Generation (kWh)"))
                self.data_dict[key]["thermalOutput"] = self.self.to_num_or_zero(row.get("Useful Thermal Output (MMBtu)"))
                self.data_dict[key]["totalFuelConsumption"] = self.to_num_or_zero(row.get("Total Fuel Consumption (MMBtu)"))
                self.data_dict[key]["totalFuelConsumptionGeneration"] = self.to_num_or_zero(row.get("Fuel Consumption for Electric Generation (MMBtu)"))
                self.data_dict[key]["co2Tons"] = self.to_num_or_zero(row.get("Tons of CO2 Emissions"))
                self.data_dict[key]["co2MetricTons"] = self.to_num_or_zero(row.get("Metric Tonnes of CO2 Emissions"))

                us_key = "US" + str(row.get("Year"))
                self.data_dict[us_key]["generation"] = self.data_dict[us_key].get("generation",0) + self.to_num_or_zero(row.get("Generation (kWh)"))
                self.data_dict[us_key]["thermalOutput"] = self.data_dict[us_key].get("thermalOutput",0) + self.to_num_or_zero(row.get("Useful Thermal Output (MMBtu)"))
                self.data_dict[us_key]["totalFuelConsumption"] = self.data_dict[us_key].get("totalFuelConsumption",0) + self.to_num_or_zero(row.get("Total Fuel Consumption (MMBtu)"))
                self.data_dict[us_key]["totalFuelConsumptionGeneration"] = self.data_dict[us_key].get("totalFuelConsumptionGeneration",0) + self.to_num_or_zero(row.get("Fuel Consumption for Electric Generation (MMBtu)"))
                self.data_dict[us_key]["co2Tons"] = self.data_dict[us_key].get("co2Tons",0) + self.to_num_or_zero(row.get("Tons of CO2 Emissions"))  
                self.data_dict[us_key]["co2MetricTons"] = self.data_dict[us_key].get("co2MetricTons",0) + self.to_num_or_zero(row.get("Metric Tonnes of CO2 Emissions"))  

    def load_data(self):
        '''
        Docstring for load_data
        Loads in all the data for each state and year - both emissions and prices
        :param self: Description
        :return: Description
        :rtype: type[dict]
        '''
        #load in price data
        with open('Data/sales_revenue.csv', mode='r', newline='') as price_file:
            for _ in range(3):
                next(price_file)
            reader = csv.reader(price_file)
            for row in reader:
                """if int(row[0]) < self.year:
                    break"""
                self.load_price_row(row)
        self.load_us_price_data()
        self.average_customers_prices()
        self.load_emission_data()