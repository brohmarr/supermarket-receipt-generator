# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

import json


class Customer:
    """
    A class used to represent a customer.

    ---

    Attributes
    ----------
    customer_data : dict
        A dictionary to hold the data read from the customer_data.json input
        file.
    
    Methods
    -------
    get_customer_data()
        Returns the customer_data attribute.
    """
    
    
    def __init__(self):
    
        self.customer_data = {}

        # Opens the JSON file to get the input data into a dictionary.
        with open('customer_data.json', mode = 'r') as json_file:
            self.customer_data = json.load(json_file)
    
    # Retrieves the data received.
    def get_customer_data(self):
        """
        Returns the customer_data attribute.
        """
    
        return self.customer_data
