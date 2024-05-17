import csv


class Inventory:
    
    def __init__(self):
        self.price_per_item = {}

        # Opening the CSV file to get the input data.
        with open('items.txt', mode = 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Copying the data received into a dictionary for fast lookups.
            for row in csv_reader:
                self.price_per_item[row["name"]] = row["price"]
    
    # Retrieving the data received.
    def get_inventory(self):
        return self.price_per_item
