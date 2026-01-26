'''
This file contains functions which retrieve the desired data from the datasets for the command line functions to access
'''
import csv

def get_price_data_state(state, year):
    '''
    Docstring for get_price_data_state
    Accesses sales_revenue.xlsx - Monthly-States.csv
    finds rows for 

    :param state: two letter code for the State which we want data for, if state is US then take all month data for year to aggregate
    :param year: the year of data desired
    
    :return : returns a dict with entries for state/year then entries for the residential/commercial etc. for revenue/sales etc.
    If improper state or year value entered should return dict with empty values and state/year entries as the invalid inputs
    '''
    monthData = []
    with open('Data/sales_revenue.csv', mode='r',newline='') as csvFile:
        for _ in range(2): #skip first two lines of csv file to make third row column headers
            next(csvFile)
        reader = csv.reader(csvFile)
        headers = next(reader)
        for row in reader:
            if int(row[0]) < year:
                break
            if (row[2] == state and int(row[0]) == year) or (state == "US" and int(row[0]) == year):
                monthData.append(row)
    return fixed_dict_format(aggregate_month_data_sales(monthData), state)
def aggregate_month_data_sales(monthData):
    '''
    Docstring for aggregate_month_data_sales
    Sums the given month data into one dict containing the totals for revenue, sales, etc and the avg for the prices
    
    :param monthData: list of lists containing all the month data for a year for a state
    :return totals: dict of dicts with each category ("residential" etc) having its own dict
    Dict format:
    {Residential: {Revenue: float, Sales: float, Customers: float, PriceAvg: float}, Commercial: {etc}, Industrial: {etc}, etc}
    '''
    fieldNames = ["revenue", "sales", "customers", "priceAvg"]
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
    emptyPriceCount = 0
    for month in monthData:
        for name, idxs in fields.items():
            for i, idx in zip(fieldNames, idxs):
                if str(i) == "priceAvg" and to_num_or_zero(month[idx]) == 0:
                    emptyPriceCount += 1
                totals[name][i] += to_num_or_zero(month[idx])
    numDataMonths = len(monthData)
    if numDataMonths > 0:
        for name in totals:
            if name == "transportation" and numDataMonths != emptyPriceCount:
                totals[name]["priceAvg"] /= (numDataMonths - emptyPriceCount)
            else: totals[name]["priceAvg"] /= numDataMonths
            totals[name]["priceAvg"] = round(totals[name]["priceAvg"],2)
            totals[name]["customers"] = int(totals[name]["customers"]/(numDataMonths)) # customer data is averaged across months
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
def fixed_dict_format(totalsDict, state):
    '''
    Docstring for fixed_dict_format
    
    :param totalsDict: dictionary from aggregate function whos formating is being fixed
    :param state: the state for which the dictionary is made for
    year is set to 2025 as fixed year for now, only care about most recent data
    '''
    stateDict = {}
    stateDict["state"] = state
    stateDict["year"] = 2025 
    #If state is US need to average months across all states
    if stateDict["state"] == "US":
        stateDict["residentialCustomers"] = int(totalsDict["residential"]["customers"]*51)
        stateDict["commercialCustomers"] = int(totalsDict["commercial"]["customers"]*51)
        stateDict["industrialCustomers"] = int(totalsDict["industrial"]["customers"]*51)
        stateDict["transportationCustomers"] = int(totalsDict["transportation"]["customers"]*51)
        stateDict["totalCustomers"] = int(totalsDict["total"]["customers"]*51)
    else:
        stateDict["residentialCustomers"] = totalsDict["residential"]["customers"]
        stateDict["commercialCustomers"] = totalsDict["commercial"]["customers"]
        stateDict["industrialCustomers"] = totalsDict["industrial"]["customers"]
        stateDict["transportationCustomers"] = totalsDict["transportation"]["customers"]
        stateDict["totalCustomers"] = totalsDict["total"]["customers"]
    stateDict["residentialRevenue"] = totalsDict["residential"]["revenue"]
    stateDict["residentialSales"] = totalsDict["residential"]["sales"]
    stateDict["residentialPrice"] = totalsDict["residential"]["priceAvg"]
    stateDict["commercialRevenue"] = totalsDict["commercial"]["revenue"]
    stateDict["commercialSales"] = totalsDict["commercial"]["sales"]
    stateDict["commercialPrice"] = totalsDict["commercial"]["priceAvg"]
    stateDict["industrialRevenue"] = totalsDict["industrial"]["revenue"]
    stateDict["industrialSales"] = totalsDict["industrial"]["sales"]
    stateDict["industrialPrice"] = totalsDict["industrial"]["priceAvg"]
    stateDict["transportationRevenue"] = totalsDict["transportation"]["revenue"]
    stateDict["transportationSales"] = totalsDict["transportation"]["sales"]
    stateDict["transportationPrice"] = totalsDict["transportation"]["priceAvg"]
    stateDict["totalRevenue"] = totalsDict["total"]["revenue"]
    stateDict["totalSales"] = totalsDict["total"]["sales"]
    stateDict["totalPrice"] = totalsDict["total"]["priceAvg"]
    return stateDict
def main():
    US25 = get_price_data_state("US", 2025)
    KY25 = get_price_data_state("KY", 2025)
    #print(US25["transportationPrice"])
    print(US25["commercialCustomers"])
    print(KY25["commercialCustomers"])
    print(KY25["totalCustomers"])

if __name__ == "__main__":
    main()