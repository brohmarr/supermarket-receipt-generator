# Supermarket Receipt Generator
# by: @brohmarr
# 
# Python v3.12.3

from supermarket import Supermarket


def main():
    supermarket = Supermarket("Fresh Fruits")
    
    receipt = supermarket.build_receipt()
    first_line = True
    with open("receipt.txt", mode = "w") as receipt_file:
        for line in receipt:
            if first_line:
                receipt_file.write(line)
                first_line = False

                continue
            
            receipt_file.write("\n" + line)


main()
