# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

from inventory import Inventory
from customer import Customer


class Supermarket:
    
    def __init__(self, name: str = "Supermarket"):
        self.name = name
        self.inventory = Inventory()
        self.customer = Customer()
    
    # TODO: Implement this!
    def print_receipt(self):
        pass
