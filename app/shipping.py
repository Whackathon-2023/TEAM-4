import pandas as pd
import random
import numpy as np
import regex as re
from datetime import datetime, timedelta
import json

class Shipping:
    def __init__(self) -> None:
        # Create a list of dictionaries containing the data
        self.look_up_table = [
            {'Product': 'Urea', 'Port': 'Mesaieed', 'Country': 'Qatar', 'Manufacturer': 'Muntajat'},
            {'Product': 'Urea', 'Port': 'Al Jubail', 'Country': 'RSA', 'Manufacturer': 'Sabic'},
            {'Product': 'Urea', 'Port': 'Bontang', 'Country': 'Indonesia', 'Manufacturer': 'Kaltim'},
            {'Product': 'Urea', 'Port': 'Sitra', 'Country': 'Bahrain', 'Manufacturer': 'GPIC'},
            {'Product': 'Urea', 'Port': 'Sipitang', 'Country': 'Malaysia', 'Manufacturer': 'Petronas'},
            {'Product': 'UAN', 'Port': 'Donaldsonville', 'Country': 'USA', 'Manufacturer': 'CF Industries'},
            {'Product': 'UAN', 'Port': 'Port Lisas', 'Country': 'Trinidad', 'Manufacturer': 'Helm'},
            {'Product': 'UAN', 'Port': 'Novorossiysk', 'Country': 'Russia', 'Manufacturer': 'Eurochem'},
            {'Product': 'MOP', 'Port': 'Aqaba', 'Country': 'Egypt', 'Manufacturer': 'APC'},
            {'Product': 'MOP', 'Port': 'Portland', 'Country': 'USA', 'Manufacturer': 'Canpotex'},
            {'Product': 'MAP', 'Port': 'Ras Al Khair', 'Country': 'RSA', 'Manufacturer': 'Maaden'}
        ]


        self.products = ['Urea', 'UAN', 'MOP', 'MAP', 'SSP']

        # Create a dictionary with values
        self.discharge_rate = {
            'Urea': 3500,
            'UAN': 10000,
            'MOP': 5000,
            'MAP': 5000,
            'SSP': 4500
            }

        self.table = self.make_table()


    def make_table(self):
        # Starting date: January 2020
        start_date = datetime(2020, 1, 1)
        # Data Processing
        df = pd.read_excel("data/shipping_file.xlsx")
        df.columns = df.iloc[2]
        df = df.iloc[3:]
        df = df[['Day', 'Month' ,'Geraldton', 'BCJ4', 'BCJ3', 'Bunbury', 'Albany', 'Esperance']].reset_index()
        df = df.drop('index', axis=1)
        ##############################
        competitiors = ['Nutrien','Summit','CBH']
        ports = ['Geraldton', 'BCJ4', 'BCJ3', 'Bunbury', 'Albany', 'Esperance']
        def calculate_ship_details(summer_dwt, max_depth, empty_depth, actual_depth):
            # Calculate maximum freight capacity (95% of Summer DWT)
            max_freight_capacity = summer_dwt * 0.95

            # Determine the depth of the ship when it leaves the port of loading
            loaded_depth = actual_depth - empty_depth

            # Calculate the estimated weight on the ship
            estimated_weight_on_ship = (loaded_depth / 6) * max_freight_capacity

            return {
                "Volume": max_freight_capacity,
                "Max Depth": max_depth,
                "Min Depth": empty_depth,
                "Loaded Depth": loaded_depth,
                "Estimated Weight on Ship": estimated_weight_on_ship,
            }
        def random_volume():
            # Example usage:
            summer_dwt = random.randint(25000, 35000)  # Summer DWT in tons
            max_depth = random.randint(9,13)    # Maximum depth
            empty_depth = random.randint(3,7)   # Empty depth
            actual_depth = random.randint(8,12)  # Actual depth when leaving port

            ship_details = calculate_ship_details(summer_dwt, max_depth, empty_depth, actual_depth)
            return ship_details['Volume']
        # Create a boolean mask to check for matches
        def num_processing(df):
            df = df.apply(lambda x: re.sub(r'[^a-zA-Z]', '', x.split(' ')[0]))
            return df

        def competitors_name(df):
            for c in competitiors:
                if c in str(df):
                    return c


        def data_processing(port):
            data = df[df[port].notna()==True]
            mask = data[port].str.contains('|'.join(competitiors), case=True, regex=True)
            table = data[mask==True][['Day', 'Month', port]].reset_index()
            product = num_processing(data[mask==False][port]).reset_index().drop('index', axis = 1)

            table['product'] = product
            table['volume'] = [round(random_volume()) for i in range(len(table))]
            table['index'] = table.apply(lambda x: (x['index']//30 +1), axis = 1)
            table['competitor'] = table[port].apply(competitors_name)
            table = table[table['product'].str.len() > 2]
            table = table.dropna()
   
     
            return table.T


        ports = {p:data_processing(p)  for p in ports}
        return ports
    
    def json_form(self):
        for x,y in self.table.items():
            self.table[x] = y.to_json()
        result = json.dumps(self.table)
        return result

        
















    
    

        
