import pandas as pd
import random
import numpy as np
import regex as re
from datetime import date, timedelta
import json
import datetime
from dateutil.relativedelta import relativedelta
from app.shipping import Shipping
import json
from random import randint, uniform
from datetime import datetime
import uuid




class dashboard():
    def __init__(self) -> None:
        # Create a list of dictionaries containing the data
        self.competitiors = ['Nutrien','Summit','CBH']
        self.products = ['Urea', 'UAN', 'MOP', 'MAP', 'SSP']

        self.discharge_rate = {
            'Urea': 3500,
            'UAN': 10000,
            'MOP': 5000,
            'MAP': 5000,
            'SSP': 4500
            }
        
        self.agency   = {
            "Inchcape Shipping Services": 'Nutrien',
            "Sturrock Gridrod Maritime (australia) Pty Ltd": 'Nutrien',
            "Quay Marine Agencies P/L": 'Summit',
            "Gulf Agency Company (Australia) Pty/Ltd": 'Summit',
            "Monson Agencies Australia": 'CBH'
        }

    def company_name(self):
        company = ['Nutrien','Summit','CBH']
        return random.choice(company)
    
    
    def product_name(self):
        return random.choice(self.products)
    


    def calculate_ship_details(self,summer_dwt, max_depth, empty_depth, actual_depth):
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


    def random_volume(self):
            # Example usage:
            summer_dwt = random.randint(25000, 35000)  # Summer DWT in tons
            max_depth = random.randint(9,13)    # Maximum depth
            empty_depth = random.randint(3,7)   # Empty depth
            actual_depth = random.randint(8,12)  # Actual depth when leaving port

            ship_details = self.calculate_ship_details(summer_dwt, max_depth, empty_depth, actual_depth)
            return ship_details['Volume']
    
    def generate_id(self):
         return str(uuid.UUID(int=random.getrandbits(128)))

    def generate_data(self,num_records):

        data = []
        for _ in range(num_records):
            record = {
                 "ID":self.generate_id(),
                "COMPANY NAME": self.company_name(),
                "VESSEL": f"Vessel {randint(1, 20)}",
                "PRODUCT TYPE": self.product_name(),
                "VOLUME":round(self.random_volume()),
                "FOB PRICE PER UNIT (AUD)": round(uniform(10, 100), 2),
                "DATE": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "PORT":random.randint(1,100)
            }
            data.append(record)

        json_data = json.dumps(data, indent=4)  # Optional: Use indent for pretty formatting

        return json_data
    
   

        



   















    
    

        
