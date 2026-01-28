import argparse
import csv
from ProductionCode.table_maker import TableMaker
from ProductionCode.states import states_list
from ProductionCode.data_retrieval import get_price_data_state

EMISSIONS_FILE = "Data/state_year_power_summary.csv"
LATEST_EMISSIONS_YEAR = "2024"

def main():
    '''
    Docstring for main - Handles user input with argparse and calls functions to get data and displays info
    '''
    parser = argparse.ArgumentParser(
        description="Acesses and displays most recent emmisions and prices data by state.\n\n\
        Note: no year selection available ... yet",
        epilog='Example: python3 command_line.py -p KS -> will display price information for Kansas in 2024'
    )
    parser.add_argument('-p', '--prices', action='store_true',
                        help='add prices to output     (default is all data)')  
    parser.add_argument('-e', '--emissions', action='store_true',
                        help='add emissions to output  (default is all data)') 
    parser.add_argument('args', nargs='*',type=str,
                        help="A space seperated list of states to display, \
use all caps two letter state codes, \
'US' displays the totals/averages for the whole US")
    
    args = parser.parse_args()

    #process flags
    flags = [False] * 2
    if args.prices or args.emissions:
        flags[0] = args.prices
        flags[1] = args.emissions
    else:
        flags = [True] * 2
    #args
    for entry in args.args:
        if entry not in states_list:
            parser.error(entry + " is not a given state. \
Please use uppercase two letter state codes or 'US'")

    completeData = getData(args.args, flags)
    myTable = TableMaker()

    for i in completeData:
        myTable.add_new_entry(i)
      
    myTable.print_table()
def getEmissionData(state):
    """
    Returns emissions data for one state using the most recent year
    in state_year_power_summary.csv
    """
    year_to_use = LATEST_EMISSIONS_YEAR

    def toNumber(value):
        if value is None:
            return None
        s = str(value).replace(",","").strip()
        if s == "":
            return None
        try:
            return float(s)
        except:
            return None

    if state == "US":
        totals = {
            "generation": 0.0,
            "thermalOutput": 0.0,
            "totalFuelConsumption": 0.0,
            "totalFuelConsumptionGeneration": 0.0,
            "co2Tons": 0.0,
            "co2MetricTons": 0.0
        }
        found_any = False

        with open(EMISSIONS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("Year") != year_to_use:
                    continue

                found_any = True
                totals["generation"] += (toNumber(row.get("Generation (kWh)")) or 0.0)
                totals["thermalOutput"] += (toNumber(row.get("Useful Thermal Output (MMBtu)")) or 0.0)
                totals["totalFuelConsumption"] += (toNumber(row.get("Total Fuel Consumption (MMBtu)")) or 0.0)
                totals["totalFuelConsumptionGeneration"] += (toNumber(row.get("Fuel Consumption for Electric Generation (MMBtu)")) or 0.0)
                totals["co2Tons"] += (toNumber(row.get("Tons of CO2 Emissions")) or 0.0)
                totals["co2MetricTons"] += (toNumber(row.get("Metric Tonnes of CO2 Emissions")) or 0.0)

        if not found_any:
            raise KeyError("No emissions data found for US in " + year_to_use)

        return totals

    with open(EMISSIONS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("State") == state and row.get("Year") == year_to_use:
                return {
                    "generation": toNumber(row.get("Generation (kWh)")),
                    "thermalOutput": toNumber(row.get("Useful Thermal Output (MMBtu)")),
                    "totalFuelConsumption": toNumber(row.get("Total Fuel Consumption (MMBtu)")),
                    "totalFuelConsumptionGeneration": toNumber(row.get("Fuel Consumption for Electric Generation (MMBtu)")),
                    "co2Tons": toNumber(row.get("Tons of CO2 Emissions")),
                    "co2MetricTons": toNumber(row.get("Metric Tonnes of CO2 Emissions"))
                }

    raise KeyError("No emissions data found for " + state + " in " + year_to_use)
def getData(states, flags):
    """
    Returns an array of dict entries for TableMaker.

    states: list like ["MN","ND"]
    flags: [prices_flag, emission_flag]
    """
    results = []

    if flags[0] and flags[1]:
        year_label = LATEST_EMISSIONS_YEAR + " / 2025"
    elif flags[1]:
        year_label = LATEST_EMISSIONS_YEAR
    elif flags[0]:
        year_label = "2025"
    else:
        year_label = ""

    for state in states:
        entry = {
            "state": state,
            "year": year_label
        }

        if flags[1]:
            emissions = getEmissionData(state)
            entry.update(emissions)
        
        if flags[0]:
            prices = get_price_data(state)
            entry.update(prices)
        
        results.append(entry)

    return results
def get_price_data(state):
    '''
    Docstring for getPriceData
    
    :param state: two letter state code
    :return dictionary: format is entries for state and year then entries for each column in dataset like residentialReveune or totalPrice
    Example:
    dict["state"] = KS if state param is KS
    dict["residentialRevenue"] = residential revenue for year 2025 in KS, summed values from all months 
    '''
    return get_price_data_state(state, 2025) 

'''
REMOVED - no longer needed
def get_US_data():
    ''
    Will get data for entire us to be displayed
    Calls to getPriceData() and getEmmissionsData() with US as the state
    will store retreived data as a dict of dict with usData["price"] storing price dict and usData["emissions"] storing emissions dict
    ''
    usData = {}
    priceDict = get_price_data("US")
    emissionsDict = getEmissionData("US")
    for key, value in priceDict.items():
        usData[key] = value
    for key,value in emissionsDict.items():
        usData[key] = value
    return usData
'''
'''
REMOVED - no longer needed
def show_help(): 
    print("Usage: python3 command_line.py State --prices --emissions\n"\
        "--prices: optional tag - add tag to display information on prices\n"\
        "--emissions: optional tag - add tag to display information on emissions\n"\
        "no tag defaults to all info\n"\
        "State input must be of valid form ie 2 letter symbol; California = CA\n"\
        "   - US is the symbol used to get info for entire US\n"\
        "The year of retreived data is most recent data so 2025 (for now)"    
        )

    Usage: python3 command_line.py State --prices --emissions 
    --prices: optional tag - add tag to display information on prices
    --emissions: optional tag - add tag to display information on emissions
    no tag defaults to all info 
    State input must be of valid form ie 2 letter symbol; California = CA
        - US is the symbol used to get info for entire US

    Help: 
        retrieve information from the data sets about energy prices, emissions, and generation
        Usage: python3 command_line.py State --prices --year 2023
    Prices tag: Get the price data 

'''
if __name__ == "__main__":
    main()
