# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

from datetime import datetime
from inventory import Inventory
from customer import Customer


class Supermarket:
    """
    A class used to represent a supermarket.

    ---

    Attributes
    ----------
    name : str
        The name of the supermarket.
    
    receipt : list
        A list to hold the formatted strings that will compose the output
        file.
    
    inventory : Inventory
        An instance of the Inventory class to hold the information about the
        items available and their prices.
    
    customer : Customer
        An instance of the Customer class to hold the information about the
        person shopping at the supermarket.
    
    Methods
    -------
    format_receipt_heading(self, heading_align, width, section_separator)
        Formats the first section of the receipt (the heading).
    
    format_receipt_shopping_list(self, price_total, num_separator, precision,
                                     width, fill, body_align,
                                     section_separator)
        Formats the second section of the receipt (the customer's shopping
        list).
    
    format_price_and_payment(self, price_total, value_paid, num_separator,
                                 precision, width, fill, body_align,
                                 section_separator)
        Formats the third section of the receipt (the total price and value
        paid).
    
    format_customer_information(self, fill, body_align, width)
        Formats the fourth section of the receipt (the customer's
        information).
    
    build_receipt(self, value_paid: float = None)
        Handles the process of building the receipt attribute.
    """
    

    def __init__(self, name: str = "Supermarket"):
        """
        Parameters
        ----------
        name : str, optional
            The name of the supermarket (default is "Supermarket").
        """
    
        self.name = name
        self.receipt = []
        self.inventory = Inventory()
        self.customer = Customer()
    
    def format_receipt_heading(self, heading_align: str, width: int,
                               section_separator: str):
        """
        Formats the first section of the receipt (the heading).

        ---

        Parameters
        ----------
        heading_align : str
            The text alignment for the f-strings.
        
        width : int
            The text width for the f-strings.
        
        section_separator : str
            A pre-built string to separate each section of the receipt.
        """
    
        # Creates the formatted version of the Supermarket's name.
        name = f"{self.name:{heading_align}{width}}"

        # Creates the formatted version of the current date.
        current_date = datetime.now()
        formatted_date = f"{current_date:%a %b %d, %Y @ %I:%M %p}"
        centered_date = f"{formatted_date:{heading_align}{width}}"

        # Adds the newly formatted strings to the "receipt" list.
        self.receipt.extend([section_separator, name, section_separator, centered_date,
                             section_separator])

    def format_receipt_shopping_list(self, price_total: float, num_separator: str,
                                     precision: int, width: int, fill: str,
                                     body_align: str, section_separator: str):
        """
        Formats the second section of the receipt (the customer's shopping list).

        Returns the total cost of the customer's shopping list.

        ---

        Parameters
        ----------
        price_total : float
            The total cost of the customer's shopping list.
        
        num_separator : str
            The character used as the thousand separator for the f-strings.
        
        precision : int
            The number of decimal places to show in floats for the f-strings.
        
        width : int
            The text width for the f-strings.
        
        fill : str
            The character to be used in the empty spaces for the f-strings.
        
        body_align : str
            The text alignment for the f-strings.
        
        section_separator : str
            A pre-built string to separate each section of the receipt.
        """
    
        # Creates the formatted version of the customer's shopping list.
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

            # Adds the newly formatted strings to the "receipt" list.
            self.receipt.append(current_line)
        
        # Adds the section separator to the "receipt" list.
        self.receipt.append(section_separator)

        return price_total

    def format_price_and_payment(self, price_total: float, value_paid: float,
                                 num_separator: str, precision: int, width: int,
                                 fill: str, body_align: str,
                                 section_separator: str):
        """
        Formats the third section of the receipt (the total price and value
        paid).

        ---

        Parameters
        ----------
        price_total : float
            The total cost of the customer's shopping list.
        
        value_paid : float
            The amount of money received from the customer.
        
        num_separator : str
            The character used as the thousand separator for the f-strings.
        
        precision : int
            The number of decimal places to show in floats for the f-strings.
        
        width : int
            The text width for the f-strings.
        
        fill : str
            The character to be used in the empty spaces for the f-strings.
        
        body_align : str
            The text alignment for the f-strings.
        
        section_separator : str
            A pre-built string to separate each section of the receipt.
        """
    
        # Creates the formatted version of the total price value.
        formatted_price_total = f"${price_total:{num_separator}.{precision}f}"
        # The '5' below refers to the "Total" in the "str_price_total" string.
        price_total_width = width - 5

        # Creates the formatted version of the total price line of the receipt.
        str_price_total = f"Total{formatted_price_total:{fill}{body_align}{price_total_width}}"

        # Creates the formatted version of the value paid if it wasn't paid
        # with a credit/debit card (e.g.: paying $ 94.99 with a $ 100 bill).
        if not value_paid:
            value_paid = price_total
            formatted_value_paid = formatted_price_total
        else:
            formatted_value_paid = f"${value_paid:{num_separator}.{precision}f}"
        
        # The '4' below refers to the "Paid" in the "str_value_paid" string.
        value_paid_width = width - 4

        str_value_paid = f"Paid{formatted_value_paid:{fill}{body_align}{value_paid_width}}"

        # Creates the formatted version of the change value.
        change = value_paid - price_total
        formatted_change = f"${change:{num_separator}.{precision}f}"

        # The '6' below refers to the "Change" in the "str_change" string.
        change_width = width - 6

        # Creates the formatted version of the change line of the receipt.
        str_change = f"Change{formatted_change:{fill}{body_align}{change_width}}"

        # Adds the newly formatted strings to the "receipt" list.
        self.receipt.extend([str_price_total, str_value_paid, str_change,
                             section_separator])

    def format_customer_information(self, fill: str, body_align: str, width: int):
        """
        Formats the fourth section of the receipt (the customer's information).

        ---

        Parameters
        ----------        
        fill : str
            The character to be used in the empty spaces for the f-strings.
        
        body_align : str
            The text alignment for the f-strings.
        
        width : int
            The text width for the f-strings.
        """
        
    
        # Retrieves the customer's data for the payment section of the receipt.
        customer_data = self.customer.get_customer_data()
        
        # Saves the customer's name data into variables for the sake of code
        # clarity in the "str_name_and_payment" variable below.
        customer_first_name = customer_data["first_name"]
        customer_last_name = customer_data["last_name"]
        customer_name = f"{customer_first_name} {customer_last_name}"

        # Saves the customer's payment data into variables for the sake of code
        # clarity in the "str_name_and_payment" variable below.
        payment_method = customer_data["payment_method"]
        payment_method_width = width - len(customer_name)

        # Creates the formatted version of the customer's name with their
        # payment method.
        str_name_and_payment = f"{customer_name}{payment_method:{fill}{body_align}{payment_method_width}}"

        # Creates the formatted version of the customer's card flag with its
        # number if they paid with a credit/debit card.
        if payment_method[-4:].lower() == "card":
            # Saves the customer's card data into variables for the sake of code
            # clarity in the "str_name_and_payment" variable below.
            card_flag = customer_data["card_flag"]

            card_number = customer_data["card_number"][-4:]
            formatted_card_number = f"**** {card_number}"
            card_number_width = width - len(card_flag)

            str_payment_method = f"{card_flag}{formatted_card_number:{fill}{body_align}{card_number_width}}"
        
        # Otherwise (if they paid with cash) just save the word "Cash" to the
        # receipt string list.
        else:
            str_payment_method = f"Cash"

        # Adds the newly formatted strings to the "receipt" list.
        self.receipt.extend([str_name_and_payment, str_payment_method])

    def build_receipt(self, value_paid: float = None):
        """
        Handles the process of building the receipt attribute.

        Returns the receipt attribute.

        ---

        Parameters
        ----------        
        value_paid : float
            The amount of money received from the customer (default is None).
        """
    
        # Defines the formatting values for the receipt string list.
        fill = ''
        heading_align = '^'
        body_align = '>'
        width = 40
        num_separator = ','
        precision = 2
        section_separator = f"-" * width

        # Clears the receipt string list and total price value in case this
        # method is called again.
        self.receipt.clear()
        price_total = 0

        # Creates the formatted version of the receipt's heading section.
        self.format_receipt_heading(heading_align, width, section_separator)

        # Creates the formatted version of the shopping list section.
        price_total = self.format_receipt_shopping_list(price_total, num_separator,
                                                        precision, width, fill,
                                                        body_align, section_separator)

        # Creates the formatted version of the total price and payment section.
        self.format_price_and_payment(price_total, value_paid, num_separator, precision,
                                      width, fill, body_align, section_separator)

        # Creates the formatted version of the customer's information.
        self.format_customer_information(fill, body_align, width)

        # Returns the fully built receipt (a list of formatted strings).
        return self.receipt
