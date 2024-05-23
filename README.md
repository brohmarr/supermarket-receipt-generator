# Supermarket Receipt Generator

I was trying to think of a small/quick project to play around a bit with Python's “Format Specification Mini-Language”, and ended up building a receipt generator for supermarkets (keep in mind that it isn’t connected to any real-world system, so it outputs to a text file).

The program receives as input a CSV text file, containing each of the available items’ prices, and a JSON file, containing the customer’s data.

The program starts by taking in the input files and converting both of them to dictionaries for fast lookups. Then, it uses this newly organized data to output a carefully formatted receipt to a new text file.

In the end, this quick idea helped me review Python’s string interpolation tools and when to use each of them; f-strings (I was used to str.format()); working with CSV and JSON files; and to learn Python's Format Specification Mini-Language.