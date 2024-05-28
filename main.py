# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

from supermarket import Supermarket


def main():

    
    supermarket = Supermarket("Fresh Fruits")
    
    # Saving the receipt in a list o strings to be iterated and written into
    # a text file (this program's output).    
    receipt = supermarket.build_receipt()
    
    # Creates the output text file (if it doesn't exist yet) and opens it to
    # start writting the receipt content line by line.
    first_line = True
    with open("receipt.txt", mode = "w") as receipt_file:
        for line in receipt:
            # This condition helps to avoid an extra empty line at the end
            # of the text output file.
            if first_line:
                receipt_file.write(line)
                first_line = False

                continue

            receipt_file.write("\n" + line)


# Starting the program...
main()
