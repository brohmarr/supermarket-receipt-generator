# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

import csv


class Inventory:
    """
    A class used to represent a supermarket inventory.

    ---

    Attributes
    ----------
    price_per_item : dict
        A dictionary to hold the data read from the item_prices.txt (CSV)
        input file.
    
    Methods
    -------
    get_item_prices()
        Returns the price_per_item attribute.
    """
    

    def __init__(self):
    
        self.price_per_item = {}

        # Opens the CSV file to get the input data.
        with open('item_prices.txt', mode = 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Copy the data received into a dictionary.
            for row in csv_reader:
                self.price_per_item[row["name"]] = float(row["price"])
    
    # Retrieves the data received.
    def get_item_prices(self):
        """
        Returns the price_per_item attribute.
        """
    
        return self.price_per_item
