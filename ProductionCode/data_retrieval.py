'''
This file contains functions which retrieve the desired data from the datasets 
for the command line functions to access
'''
import csv

def get_price_data_state(state, year):
    '''
    Docstring for get_price_data_state
    Accesses sales_revenue.xlsx - Monthly-States.csv
    finds rows for 
    :param state: two letter code for the State which we want data for, 
    if state is US then take all month data for year to aggregate
    :param year: the year of data desired
    
    :return : returns a dict with entries for state/year then entries 
    for the residential/commercial etc. for revenue/sales etc.
    If improper state or year value entered should return dict with empty values and 
    state/year entries as the invalid inputs
    '''
    month_data = []
    with open('Data/sales_revenue.csv', mode='r',newline='') as csv_file:
        for _ in range(3): #skip first two lines of csv file to make third row column headers
            next(csv_file)
        reader = csv.reader(csv_file)
        for row in reader:
            if int(row[0]) < year:
                break
            if (row[2] == state and int(row[0]) == year) or (state == "US" and int(row[0]) == year):
                month_data.append(row)
    return fixed_dict_format(aggregate_month_data_sales(month_data), state)
def aggregate_month_data_sales(month_data):
    '''
    Docstring for aggregate_month_data_sales
    Sums the given month data into one dict containing: 
    totals for revenue, sales, etc and the avg for the prices
    
    :param month_data: list of lists containing all the month data for a year for a state
    :return totals: dict of dicts with each category ("residential" etc) having its own dict
    Dict format:
    {Residential: {Revenue: float, Sales: float, Customers: float, PriceAvg: float}, Commercial: {etc}, etc}
    '''
    field_names = ["revenue", "sales", "customers", "priceAvg"]
    fields = {
    "residential":  (4, 5, 6, 7),
    "commercial":   (8, 9, 10, 11),
    "industrial":   (12, 13, 14, 15),
    "transportation": (16, 17, 18, 19),
    "total":        (20, 21, 22, 23),
    }
    totals = {
        name: {
            "revenue": 0,
            "sales": 0,
            "customers": 0,
            "priceAvg": 0
        } for name in fields
    }
    empty_price_count = 0
    for month in month_data:
        for name, idxs in fields.items():
            for i, idx in zip(field_names, idxs):
                if str(i) == "priceAvg" and to_num_or_zero(month[idx]) == 0:
                    empty_price_count += 1
                totals[name][i] += to_num_or_zero(month[idx])
    num_data_months = len(month_data)
    if num_data_months > 0:
        for name in totals:
            if name == "transportation" and num_data_months != empty_price_count:
                totals[name]["priceAvg"] /= (num_data_months - empty_price_count)
            else: totals[name]["priceAvg"] /= num_data_months
            totals[name]["priceAvg"] = round(totals[name]["priceAvg"],2)
            # customer data is averaged across months
            totals[name]["customers"] = int(totals[name]["customers"]/(num_data_months))
    return totals
def to_num_or_zero(entry):
    '''
    Docstring for to_num_or_zero
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
def fixed_dict_format(totals_dict, state):
    '''
    Docstring for fixed_dict_format
    
    :param totals_dict: dictionary from aggregate function whos formating is being fixed
    :param state: the state for which the dictionary is made for
    year is set to 2025 as fixed year for now, only care about most recent data
    '''
    state_dict = {}
    state_dict["state"] = state
    state_dict["year"] = 2025
    #If state is US need to average months across all states
    if state_dict["state"] == "US":
        state_dict["residentialCustomers"] = int(totals_dict["residential"]["customers"]*51)
        state_dict["commercialCustomers"] = int(totals_dict["commercial"]["customers"]*51)
        state_dict["industrialCustomers"] = int(totals_dict["industrial"]["customers"]*51)
        state_dict["transportationCustomers"] = int(totals_dict["transportation"]["customers"]*51)
        state_dict["totalCustomers"] = int(totals_dict["total"]["customers"]*51)
    else:
        state_dict["residentialCustomers"] = totals_dict["residential"]["customers"]
        state_dict["commercialCustomers"] = totals_dict["commercial"]["customers"]
        state_dict["industrialCustomers"] = totals_dict["industrial"]["customers"]
        state_dict["transportationCustomers"] = totals_dict["transportation"]["customers"]
        state_dict["totalCustomers"] = totals_dict["total"]["customers"]
    state_dict["residentialRevenue"] = totals_dict["residential"]["revenue"]
    state_dict["residentialSales"] = totals_dict["residential"]["sales"]
    state_dict["residentialPrice"] = totals_dict["residential"]["priceAvg"]
    state_dict["commercialRevenue"] = totals_dict["commercial"]["revenue"]
    state_dict["commercialSales"] = totals_dict["commercial"]["sales"]
    state_dict["commercialPrice"] = totals_dict["commercial"]["priceAvg"]
    state_dict["industrialRevenue"] = totals_dict["industrial"]["revenue"]
    state_dict["industrialSales"] = totals_dict["industrial"]["sales"]
    state_dict["industrialPrice"] = totals_dict["industrial"]["priceAvg"]
    state_dict["transportationRevenue"] = totals_dict["transportation"]["revenue"]
    state_dict["transportationSales"] = totals_dict["transportation"]["sales"]
    state_dict["transportationPrice"] = totals_dict["transportation"]["priceAvg"]
    state_dict["totalRevenue"] = totals_dict["total"]["revenue"]
    state_dict["totalSales"] = totals_dict["total"]["sales"]
    state_dict["totalPrice"] = totals_dict["total"]["priceAvg"]
    return state_dict
def main():
    ''' 
    Main 
    '''
    US25 = get_price_data_state("US", 2025)
    KY25 = get_price_data_state("KY", 2025)
    #print(US25["transportationPrice"])
    print(US25["commercialCustomers"])
    print(KY25["commercialCustomers"])
    print(KY25["totalCustomers"])

if __name__ == "__main__":
    main()
