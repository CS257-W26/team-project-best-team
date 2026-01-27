"""this class manages managing and formatting tables for the command line
Each entry has two required fields"""

import io

#variables
DISPLAY_ALLIASES = [
    ("state"                          , "State                           "),
    ("year"                           , "Year                            "),
    ("generation"                     , "Generation                 (kWh)"),
    ("thermalOutput"                  , "Useful Thermal Output    (MMBtu)"),
    ("totalFuelConsumption"           , "Total Fuel Consumption   (MMBtu)"),
    ("totalFuelConsumptionGeneration" , "Total Fuel Consumption for      |\n\
Electric Generation      (MMBtu)"),
    ("co2Tons"                        , "CO2 Emmissions            (Tons)"),
    ("co2MetricTons"                  , "CO2 Emmissions     (Metric Tons)"),
    ("residentialRevenue"             , "Residential Revenue        ($1K)"),
    ("residentialSales"               , "Residential Sales          (MWh)"),
    ("residentialCustomers"           , "Residential Customers           "),
    ("residentialPrice"               , "Residential Price    (cents/kWh)"),
    ("commercialRevenue"              , "Commercial Revenue         ($1K)"),
    ("commercialSales"                , "Commercial Sales           (MWh)"),
    ("commercialCustomers"            , "Commercial Customers            "),
    ("commercialPrice"                , "Commercial Price     (cents/kWh)"),
    ("industrialRevenue"              , "Industrial Revenue         ($1K)"),
    ("industrialSales"                , "Industrial Sales           (MWh)"),
    ("industrialCustomers"            , "Industrial Customers            "),
    ("industrialPrice"                , "Industrial Price     (cents/kWh)"),
    ("transportationRevenue"          , "Transportation Revenue     ($1K)"),
    ("transportationSales"            , "Transportation Sales       (MWh)"),
    ("transportationCustomers"        , "Transportation Customers        "),
    ("transportationPrice"            , "Transportation Price (cents/kWh)"),
    ("totalRevenue"                   , "total Revenue              ($1K)"),
    ("totalSales"                     , "total Sales                (MWh)"),
    ("totalCustomers"                 , "total Customers                 "),
    ("totalPrice"                     , "total Price          (cents/kWh)")
]

class TableMaker:

    """each entry is a dictionary"""
    def __init__(self):
        self.entries = []

    def add_new_empty_entry(self, state, year):
        """Adds a new empty entry for the state and year. If one exists throws an error"""
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                raise KeyError("Entry already exists")
                return
        self.entries.append({"state" : state, "year" : year})

    def add_new_entry(self, entry):
        """add a new entry. Throws an error if one already exists for state, year
        entry is a dictionary, must contain "state" and "year".
        Dictionary entries not listed in display Alliases will not be printed"""
        if not isinstance(entry, dict):
            raise TypeError("Entry must be of <class 'dict'>")
        for row in self.entries:
            if row.get("state") == entry.get("state") and row.get("year") == entry.get("year"):
                raise KeyError("Entry already exists")
                return
        self.entries.append(entry)

    def add_data_for_entry(self, state, year, data):
        """adds a new data entry for the state and year.
        raises an error if entry for state and year does not exist 
        data is a tuple (key, data) and key must be an acceptable key for this class
        (See DISPLAY_ALLIASES)"""
        if not isinstance(data, tuple):
            raise TypeError("Data must be a tuple of (key, value)")
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                entry[data[0]] = data[1]
                return
        raise KeyError("Entry does not exists")



    def print_table(self):
        """Displays the table"""   
        buffer = io.StringIO()
        colSizes = self.get_col_sizes()

        for i in range(0,len(DISPLAY_ALLIASES)):
            if self.is_row_empty(DISPLAY_ALLIASES[i][0]):
                continue
            line = DISPLAY_ALLIASES[i][1]
            for j in range(0, len(self.entries)):
                if self.entries[j].get(DISPLAY_ALLIASES[i][0]) == None:
                    line += f"| {'NULL':<{colSizes[j]}}"
                else:
                    value = self.entries[j].get(DISPLAY_ALLIASES[i][0])
                    if DISPLAY_ALLIASES[i][0] is not 'year':
                        value = self.format_entry(value)
                    line += f"| {value:<{colSizes[j]}}"
            if i < len(DISPLAY_ALLIASES)-1:
                buffer.write(line + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for size in colSizes:
                    buffer.write("|" + "-" * (size+1))
                buffer.write("\n")

        print(buffer.getvalue())
        buffer.close()

    def is_row_empty(self, rowName):
        """returns True if one or more entries is present in a row. Used for print_table()"""
        for entry in self.entries:
            if entry.get(rowName) != None:
                return False
        return True

    def get_col_sizes(self):
        """gets the width for each col based on the widest piece of data (character wise)"""
        sizes = []
        for entry in self.entries:
            largestEntry = 4
            for i in range(0, len(DISPLAY_ALLIASES)):
                value = entry.get(DISPLAY_ALLIASES[i][0])
                if value == None:
                    continue
                if DISPLAY_ALLIASES[i][0] is not 'year':
                    value = self.format_entry(value)
                    if len(value) > largestEntry:
                        largestEntry = len(value)
            sizes.append(largestEntry + 1)
        return sizes

    def format_entry(self, entry):
        """returns a formatted string
        if value is an int -> truncates and adds ,s
        if value is a float -> truncates to two decimal places and add ,s
        if it cant be interperated as either -> return entry"""
        try:
            value = float(entry)
            if value % 1 == 0:
                value = f"{int(value):,.0f}"
            else:
                value = f"{float(value):,.2f}"
            return value
        except ValueError:
            return entry

