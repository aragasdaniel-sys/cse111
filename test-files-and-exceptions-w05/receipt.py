
import csv
from datetime import datetime
now = datetime.now()
def read_dictionary(filename, key_column_index):
    """This function reads the product data from the csv file passed to the function
    in the filename parameter. The dictionary key is contained in the csv data column
    indicated by the key_column_index parameter, the value of each dictionary item is
    the list derived from the values in the row of the csv file. Function returns a
    dictionary of products."""
    products_dict = {}
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            key = row[key_column_index]
            products_dict[key] = row

    return products_dict


def main():
    """Reads the receipt.csv file, processes the file and displays the receipt
    according to the user requirements."""
    # PRODUCTS CSV
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    # REQUEST CSV
    PRODUCT_REQUEST_INDEX = 0
    QUANTITY_INDEX = 1
    print("Chanclada Store")
    try:
        products_dict = read_dictionary("products.csv", PRODUCT_INDEX)
        
        # PRINT ORDERED ITEMS
        with open("request.csv", "rt") as request_file:
            request_reader = csv.reader(request_file)
            next(request_reader)
            total_quantity = 0
            subtotal = 0
            for row in request_reader:
                key = row[PRODUCT_REQUEST_INDEX]
                quantity = int(row[QUANTITY_INDEX])
                #SUM AND PRINT THE NUMBER OF ORDERED ITEMS
                total_quantity += quantity
                print(f"{products_dict[key][NAME_INDEX]}: {row[QUANTITY_INDEX]} @ {products_dict[key][PRICE_INDEX]}")
                # SUM AND PRINT THE SUBTOTAL DUE 
                subtotal += quantity * float(products_dict[key][PRICE_INDEX])
            print(f"Number of Items: {total_quantity}")
            print(f"Subtotal: {round(subtotal, 2)}")
            sales_tax = subtotal * .06
            print(f"Sales Tax: {round(sales_tax, 2)}")
            print(f"Total: {round(subtotal + sales_tax, 2)}")
            print("Thank you for shopping at Chanclada Store.")
            print(now.strftime("%a %b %e %T %Y"))
    except FileNotFoundError as f_error:
        print("Error: missing file")
        print(f_error)
    except PermissionError as p_error:
        print("Permission denied")
        print(p_error)
    except KeyError as k_error:
        print("Error: unknown product ID in the request.csv file")
        print(k_error)
        


if __name__ == "__main__":
    main()