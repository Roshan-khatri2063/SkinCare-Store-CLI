# Function to read product details from a file (default: 'products.txt')
def read_products(filename='products.txt'):
    # List to store all product dictionaries
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:

                # Remove any leading/trailing whitespace and split line by commas
                parts = line.strip().split(',')

                # Ensure the line has exactly 5 parts (name, brand, quantity, cost price, country)
                if len(parts) == 5:
                    name, brand, qty, cost, country = parts

                    # Create a product dictionary and append to the list
                    products.append({
                        'name': name.strip(),
                        'brand': brand.strip(),
                        'quantity': int(qty.strip()),
                        'cost_price': float(cost.strip()),
                        'country': country.strip()
                    })
    except FileNotFoundError:
        print(" 'products.txt' file not found.")
    # Return the list of products
    return products
