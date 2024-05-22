# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

from datetime import datetime
from inventory import Inventory
from customer import Customer


class Supermarket:
    
    def __init__(self, name: str = "Supermarket"):
        self.name = name
        self.receipt = []
        self.inventory = Inventory()
        self.customer = Customer()
    
    def format_receipt_heading(self, heading_align, width, section_separator):
        # Formatting the Supermarket's name.
        name = f"{self.name:{heading_align}{width}}"

        # Formatting the current date.
        current_date = datetime.now()
        formatted_date = f"{current_date:%a %b %d, %Y @ %I:%M %p}"
        centered_date = f"{formatted_date:{heading_align}{width}}"

        # Adding the newly formatted strings to the "receipt" list.
        self.receipt.extend([section_separator, name, section_separator, centered_date, section_separator])

    def format_receipt_shopping_list(self, price_total, num_separator, precision, width, fill, body_align, section_separator):
        # Formatting the customer's shopping list.
        for item in self.customer.customer_data["shopping_list"]:
            product = item["fruit"]
            quantity = item["quantity"]
            price = self.inventory.get_item_prices()[product] * quantity
            price_total += price
            formatted_price = f"${price:{num_separator}.{precision}f}"

            # The '2' below refers to the " x" in the "current_line" string.
            price_width = width - len(product) - 2 - len(str(quantity))
            
            current_line = f"{product} x{quantity}"
            current_line += f"{formatted_price:{fill}{body_align}{price_width}}"

            # Adding the newly formatted strings to the "receipt" list.
            self.receipt.append(current_line)
        
        # Adding the section separator to the "receipt" list.
        self.receipt.append(section_separator)

        return price_total

    def format_price_and_payment(self, price_total, value_paid, num_separator, precision, width, fill, body_align, section_separator):
        # Formatting the total price.
        formatted_price_total = f"${price_total:{num_separator}.{precision}f}"
        # The '5' below refers to the "Total" in the "str_price_total" string.
        price_total_width = width - 5

        str_price_total = f"Total{formatted_price_total:{fill}{body_align}{price_total_width}}"

        # Formatting the value paid.
        if not value_paid:
            value_paid = price_total
            formatted_value_paid = formatted_price_total
        else:
            formatted_value_paid = f"${value_paid:{num_separator}.{precision}f}"
        
        # The '4' below refers to the "Paid" in the "str_value_paid" string.
        value_paid_width = width - 4

        str_value_paid = f"Paid{formatted_value_paid:{fill}{body_align}{value_paid_width}}"

        # Formatting the change.
        change = value_paid - price_total
        formatted_change = f"${change:{num_separator}.{precision}f}"

        # The '6' below refers to the "Change" in the "str_change" string.
        change_width = width - 6

        str_change = f"Change{formatted_change:{fill}{body_align}{change_width}}"

        # Adding the newly formatted strings to the "receipt" list.
        self.receipt.extend([str_price_total, str_value_paid, str_change, section_separator])

    def format_customer_information(self, fill, body_align, width):
        # Retrieving the customer's data.
        customer_data = self.customer.get_customer_data()
        
        # Formatting the customer's name with their payment method.
        customer_first_name = customer_data["first_name"]
        customer_last_name = customer_data["last_name"]
        customer_name = f"{customer_first_name} {customer_last_name}"

        payment_method = customer_data["payment_method"]
        payment_method_width = width - len(customer_name)

        str_name_and_payment = f"{customer_name}{payment_method:{fill}{body_align}{payment_method_width}}"

        # Formatting the customer's card flag with its number...
        if payment_method[-4:].lower() == "card":
            card_flag = customer_data["card_flag"]

            card_number = customer_data["card_number"][-4:]
            formatted_card_number = f"**** {card_number}"
            card_number_width = width - len(card_flag)

            str_payment_method = f"{card_flag}{formatted_card_number:{fill}{body_align}{card_number_width}}"
        
        # ... or setting it as "Cash".
        else:
            str_payment_method = f"Cash"

        # Adding the newly formatted strings to the "receipt" list.
        self.receipt.extend([str_name_and_payment, str_payment_method])

    def build_receipt(self, value_paid: float = None):
        # Defining the formatting values.
        fill = ''
        heading_align = '^'
        body_align = '>'
        width = 40
        num_separator = ','
        precision = 2
        section_separator = f"-" * width

        # Clearing the receipt strings and total price.
        price_total = 0
        self.receipt.clear()

        # Formatting the receipt's heading section.
        self.format_receipt_heading(heading_align, width, section_separator)

        # Formatting the shopping list section.
        price_total = self.format_receipt_shopping_list(price_total, num_separator, precision, width, fill, body_align, section_separator)

        # Formatting the total price and payment section.
        self.format_price_and_payment(price_total, value_paid, num_separator, precision, width, fill, body_align, section_separator)

        # Formatting the customer's information.
        self.format_customer_information(fill, body_align, width)

        # Returning the fully built receipt (a list of formatted strings).
        return self.receipt
