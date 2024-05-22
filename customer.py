# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

import json


class Customer:
    
    def __init__(self):
        self.customer_data = {}

        # Opening the JSON file to get the input data into a dictionary.
        with open('customer_data.json', mode = 'r') as json_file:
            self.customer_data = json.load(json_file)
    
    # Retrieving the data received.
    def get_customer_data(self):
        return self.customer_data
