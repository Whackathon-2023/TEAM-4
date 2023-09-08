import random
import json
from datetime import datetime, timedelta
import uuid

class ShippingDataGenerator:
    def __init__(self, id, departure_places, destination_places, start_date_range, max_period):
        self.id = id
        self.departure_places = departure_places
        self.destination_places = destination_places
        self.start_date_range = [datetime.strptime(date, '%Y-%m-%d') for date in start_date_range]
        self.max_period = int(max_period)

    def generate_random_start_date(self):
        # Generate a random starting date within the specified range
        start_date = random.choice(self.start_date_range)
        return start_date

    def generate_random_period(self):
        # Generate a random period within the specified maximum period
        period = random.randint(1, self.max_period)
        return period

    def generate_lookup_data(self, num_records):
        # Seed the random number generator with the hash of the ID
        seed = hash(self.id)
        random.seed(seed)

        data = []
        for _ in range(num_records):
            # Generate random departure and destination places from the object's lists
            departure_place = random.choice(self.departure_places)
            destination_place = random.choice(self.destination_places)

            # Generate a random starting date within the specified range
            shipping_date = self.generate_random_start_date()

            # Generate a random period
            period = self.generate_random_period()

            # Calculate the end date based on the shipping date and period
            end_date = shipping_date + timedelta(days=period)

            record = {
                "id": self.id,
                "departure_place": departure_place,
                "destination_place": destination_place,
                "start_date": shipping_date.strftime('%Y-%m-%d'),
                "end_date": end_date.strftime('%Y-%m-%d'),
                "period": period,
                "PORT":random.randint(1,100)
            }
            data.append(record)

        json_data = json.dumps(data, indent=4)  # Optional: Use indent for pretty formatting

        return json_data


