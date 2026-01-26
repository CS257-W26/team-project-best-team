import argparse
import csv
from ProductionCode.table_maker import TableMaker
from ProductionCode.states import states_list

EMISSIONS_FILE = "Data/state_year_power_summary.csv"
LATEST_EMISSIONS_YEAR = "2024"

def main():
    parser = argparse.ArgumentParser(
        description='Acesses and displays most recent emmisions and prices data by state.',
        epilog='Example:'
    )
    parser.add_argument('-p', '--prices', action='store_true',
                        help='add prices to output')  
    parser.add_argument('-e', '--emissions', action='store_true',
                        help='add emissions to output') 
    parser.add_argument('args', nargs='*',type=str,
                        help="A space seperated list of states to display,\
use all caps two letter state codes,\
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

    myTable = TableMaker()
    
    myTable.add_new_entry({"state": "MN", "year": "1990"})
    myTable.add_new_entry({"state": "WY", "year": "2005" , "totalRevenue" : "1.2"})
    myTable.add_new_empty_entry("US", "2026")
    myTable.add_data_for_entry("US", "2026", ("co2Tons", "50000000"))
    myTable.add_data_for_entry("MN", "1990", ("totalFuelConsumptionGeneration", "100"))
    
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
    year_label = "2024" if flags[1] else ""

    for state in states:
        entry = {
            "state": state,
            "year": year_label
        }

        if flags[1]:
            emissions = getEmissionData(state)
            entry.update(emissions)
        
        if flags[0]:
            prices = getPriceData(state)
            entry.update(prices)
        
        results.append(entry)

    return results

#Rafael
#def getPriceData("State"):
#will have to add up all months for a given year

#Rafael
#def getUSData():

#Rafael
def showHelp(): 
    print("Usage:")


if __name__ == "__main__":
    main()
