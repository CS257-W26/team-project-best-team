"""A bunch of large constants used for tests"""

valid_table = """State                           | MN   | WY   | US         
Year                            | 1990 | 2005 | 2026       
--------------------------------|------|------|------------
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 100  | NULL | NULL       
CO2 Emmissions            (Tons)| NULL | NULL | 50,000,000 
total Revenue              ($1K)| NULL | 1.20 | NULL"""

valid_ca_table = """State                           | CA             
Year                            | 2025           
--------------------------------|----------------
Generation                 (kWh)| 97,548,285,658 
Useful Thermal Output    (MMBtu)| 58,032,798     
Total Fuel Consumption   (MMBtu)| 767,934,359    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 681,143,617    
CO2 Emmissions            (Tons)| 43,645,341     
CO2 Emmissions     (Metric Tons)| 39,594,436     
Residential Revenue        ($1K)| 22,774,432     
Residential Sales          (MWh)| 70,422,342     
Residential Customers           | 14,240,133     
Residential Price    (cents/kWh)| 32.44          
Commercial Revenue         ($1K)| 25,163,599     
Commercial Sales           (MWh)| 95,373,077     
Commercial Customers            | 1,775,758      
Commercial Price     (cents/kWh)| 26.21          
Industrial Revenue         ($1K)| 7,812,009      
Industrial Sales           (MWh)| 35,470,004     
Industrial Customers            | 145,731        
Industrial Price     (cents/kWh)| 21.72          
Transportation Revenue     ($1K)| 100,886        
Transportation Sales       (MWh)| 595,049        
Transportation Customers        | 13             
Transportation Price (cents/kWh)| 16.91          
total Revenue              ($1K)| 55,850,924     
total Sales                (MWh)| 201,860,469    
total Customers                 | 16,161,635     
total Price          (cents/kWh)| 27.49"""

valid_ga_e_table = """State                           | GA             
Year                            | 2024           
--------------------------------|----------------
Generation                 (kWh)| 75,096,813,674 
Useful Thermal Output    (MMBtu)| 26,949,036     
Total Fuel Consumption   (MMBtu)| 649,945,364    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 612,469,605    
CO2 Emmissions            (Tons)| 47,088,360     
CO2 Emmissions     (Metric Tons)| 42,717,893"""

valid_wa_nm_table = """State                           | WA             | NM             
Year                            | 2025           | 2025           
--------------------------------|----------------|----------------
Generation                 (kWh)| 21,119,893,670 | 20,106,485,132 
Useful Thermal Output    (MMBtu)| 10,095,169     | 526,233        
Total Fuel Consumption   (MMBtu)| 190,433,710    | 189,048,426    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 174,834,966    | 188,281,551    
CO2 Emmissions            (Tons)| 12,798,157     | 14,773,195     
CO2 Emmissions     (Metric Tons)| 11,610,306     | 13,402,031     
Residential Revenue        ($1K)| 4,171,296      | 941,033        
Residential Sales          (MWh)| 32,028,521     | 6,215,761      
Residential Customers           | 3,406,879      | 921,341        
Residential Price    (cents/kWh)| 13.16          | 15.06          
Commercial Revenue         ($1K)| 2,997,604      | 892,115        
Commercial Sales           (MWh)| 26,311,854     | 7,926,320      
Commercial Customers            | 407,217        | 147,369        
Commercial Price     (cents/kWh)| 11.40          | 11.20          
Industrial Revenue         ($1K)| 1,146,597      | 756,119        
Industrial Sales           (MWh)| 17,104,864     | 12,402,315     
Industrial Customers            | 26,180         | 9,522          
Industrial Price     (cents/kWh)| 6.71           | 6.10           
Transportation Revenue     ($1K)| 9,858          | 0              
Transportation Sales       (MWh)| 81,611         | 0              
Transportation Customers        | 5              | 0              
Transportation Price (cents/kWh)| 12.09          | 0              
total Revenue              ($1K)| 8,325,351      | 2,589,267      
total Sales                (MWh)| 75,526,843     | 26,544,396     
total Customers                 | 3,840,281      | 1,078,234      
total Price          (cents/kWh)| 11.04          | 9.71"""

valid_nd_sd_table = """State                           | ND             | SD            
Year                            | 2025           | 2025          
--------------------------------|----------------|---------------
Generation                 (kWh)| 25,668,864,763 | 3,839,359,578 
Useful Thermal Output    (MMBtu)| 7,839,786      | 1,468,469     
Total Fuel Consumption   (MMBtu)| 298,600,042    | 41,735,122    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 281,475,282    | 37,167,960    
CO2 Emmissions            (Tons)| 30,374,329     | 3,325,000     
CO2 Emmissions     (Metric Tons)| 27,555,161     | 3,016,390     
Residential Revenue        ($1K)| 489,689        | 596,428       
Residential Sales          (MWh)| 4,117,201      | 4,434,263     
Residential Customers           | 399,645        | 443,344       
Residential Price    (cents/kWh)| 12.23          | 13.60         
Commercial Revenue         ($1K)| 705,979        | 481,715       
Commercial Sales           (MWh)| 9,510,387      | 4,415,955     
Commercial Customers            | 77,714         | 79,613        
Commercial Price     (cents/kWh)| 7.43           | 10.90         
Industrial Revenue         ($1K)| 855,769        | 229,809       
Industrial Sales           (MWh)| 11,219,822     | 2,639,036     
Industrial Customers            | 10,877         | 4,366         
Industrial Price     (cents/kWh)| 7.63           | 8.70          
Transportation Revenue     ($1K)| 0              | 0             
Transportation Sales       (MWh)| 0              | 0             
Transportation Customers        | 0              | 0             
Transportation Price (cents/kWh)| 0              | 0             
total Revenue              ($1K)| 2,051,440      | 1,307,955     
total Sales                (MWh)| 24,847,406     | 11,489,256    
total Customers                 | 488,237        | 527,324       
total Price          (cents/kWh)| 8.27           | 11.40"""


valid_mn_table = """State                           | MN             
Year                            | 2025           
--------------------------------|----------------
Generation                 (kWh)| 27,814,120,731 
Useful Thermal Output    (MMBtu)| 17,095,959     
Total Fuel Consumption   (MMBtu)| 277,129,619    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 251,190,061    
CO2 Emmissions            (Tons)| 22,476,702     
CO2 Emmissions     (Metric Tons)| 20,390,541     
Residential Revenue        ($1K)| 3,109,470      
Residential Sales          (MWh)| 19,485,710     
Residential Customers           | 2,617,362      
Residential Price    (cents/kWh)| 15.97          
Commercial Revenue         ($1K)| 2,390,786      
Commercial Sales           (MWh)| 19,199,872     
Commercial Customers            | 311,253        
Commercial Price     (cents/kWh)| 12.42          
Industrial Revenue         ($1K)| 1,519,293      
Industrial Sales           (MWh)| 16,265,802     
Industrial Customers            | 9,407          
Industrial Price     (cents/kWh)| 9.34           
Transportation Revenue     ($1K)| 1,524          
Transportation Sales       (MWh)| 11,763         
Transportation Customers        | 1              
Transportation Price (cents/kWh)| 13.10          
total Revenue              ($1K)| 7,021,077      
total Sales                (MWh)| 54,963,144     
total Customers                 | 2,938,023      
total Price          (cents/kWh)| 12.75"""

valid_us_price_table = """State                           | US            
Year                            | 2025          
--------------------------------|---------------
Residential Revenue        ($1K)| 222,032,916   
Residential Sales          (MWh)| 1,285,315,546 
Residential Customers           | 143,918,481   
Residential Price    (cents/kWh)| 17.99         
Commercial Revenue         ($1K)| 168,213,048   
Commercial Sales           (MWh)| 1,246,808,835 
Commercial Customers            | 19,600,422    
Commercial Price     (cents/kWh)| 14.08         
Industrial Revenue         ($1K)| 75,739,319    
Industrial Sales           (MWh)| 876,774,834   
Industrial Customers            | 1,130,415     
Industrial Price     (cents/kWh)| 10.38         
Transportation Revenue     ($1K)| 838,132       
Transportation Sales       (MWh)| 6,061,921     
Transportation Customers        | 51            
Transportation Price (cents/kWh)| 12.13         
total Revenue              ($1K)| 466,823,401   
total Sales                (MWh)| 3,414,961,050 
total Customers                 | 164,649,420   
total Price          (cents/kWh)| 14.50"""
