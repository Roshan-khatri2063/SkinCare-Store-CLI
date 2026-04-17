VAT_RATE = 0.13  # 13% VAT

# Function to display all available products in a formatted tabl
def display_products(products):
    print("\n Available Products")
    print("{:<4} {:<20} {:<15} {:<10} {:<10} {:<15}".format("ID", "Product", "Brand", "Quantity", "Price", "Country"))
    print("-" * 80)
    for idx, p in enumerate(products, 1):
        selling_price = p['cost_price'] * 2  # 200% markup
        print("{:<4} {:<20} {:<15} {:<10} {:<10} {:<15}".format(
            idx, p['name'], p['brand'], p['quantity'], int(selling_price), p['country']
        ))

def calculate_vat(price):
    """Calculate 13% VAT on a given price."""
    return price * VAT_RATE

# Function to handle product sales and generate customer invoice
def sell_product():
    products = read_products()
    display_products(products)
    items = []
    free_items = {}
    customer_name = input(" Enter Customer Name: ").strip()

    while True:
        try:
            pid = int(input("Enter Product ID to buy (0 to finish): "))
            if pid == 0:
                break       # Exit loop when user finishes purchase
            if pid < 1 or pid > len(products):
                print(" Invalid ID.")
                continue

            product = products[pid - 1]
            qty = int(input(f"How many of '{product['name']}'? "))
            if qty <= 0:
                print(" Quantity must be a positive number.")
                continue

            free_qty = qty // 3
            total_needed = qty + free_qty
            # Checking the stock
            if total_needed > product['quantity']:
                print(f" Not enough stock! Needed: {total_needed}, Available: {product['quantity']}")
                continue
            # Updating stock and recording sales
            product['quantity'] -= total_needed

            items.append({
                'name': product['name'],
                'brand': product['brand'],
                'quantity': qty,
                'price': product['cost_price'] * 2
            })
            # Handling free items
            if free_qty > 0:
                free_items[product['name']] = free_qty

        except ValueError:
            print(" Please enter valid numbers.")

    # The invoice is saved using the write_invoice() function,
    # and the updated product quantities are saved using write_products().
    if items:
        # Calculate VAT for the sale items
        total_price = 0
        total_vat = 0
        for item in items:
            line_total = item['quantity'] * item['price']
            total_price += line_total
            vat_amount = calculate_vat(line_total)
            total_vat += vat_amount

        write_invoice(items, free_items, customer_name, is_sale=True, total_vat=total_vat, total_price=total_price)
        write_products(products)
        print(" Sale completed and invoice is generated (to get the invoice of all just treminate the whole program to see details).")
    else:
        print(" No items were sold.")

def restock_product():
    products = read_products()
    items = []

    while True:
        print("\n Restock Menu:")
        print("1. Restock Existing Product")
        print("2. Add New Product")
        print("0. Finish Restocking")
        choice = input("Enter your choice: ").strip()

        if choice == '0':
            break

        elif choice == '1':
            display_products(products)
            try:
                pid = int(input("Enter product ID to restock: "))
                if pid < 1 or pid > len(products):
                    print(" Invalid ID.")
                    continue

                vendor = input(" Enter Vendor Name: ").strip()
                qty = int(input("Enter quantity to restock: "))
                if qty <= 0:
                    print(" Quantity must be a positive number.")
                    continue

                update_price = input("Update price? (y/n): ").lower()
                if update_price == 'y':
                    new_price = float(input("Enter new cost price: "))
                    if new_price > 0:
                        products[pid - 1]['cost_price'] = new_price
                    else:
                        print(" Invalid price. Keeping old price.")

                update_country = input("Update country? (y/n): ").lower()
                if update_country == 'y':
                    new_country = input("Enter new country: ").strip()
                    if new_country:
                        products[pid - 1]['country'] = new_country

                # Update the product quantity with the new stock
                products[pid - 1]['quantity'] += qty

                # Record the restocked product details for the invoice
                items.append({
                    'name': products[pid - 1]['name'],
                    'brand': products[pid - 1]['brand'],
                    'quantity': qty,
                    'price': products[pid - 1]['cost_price'],
                    'vendor': vendor
                })

            except ValueError:
                print("️ Please enter valid numbers.")

        elif choice == '2':
            try:
                name = input("Enter product name: ").strip()
                brand = input("Enter brand name: ").strip()
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print(" Quantity must be a positive number.")
                    continue
                price = float(input("Enter cost price: "))
                if price <= 0:
                    print(" Price must be a positive number.")
                    continue
                country = input("Enter country of origin: ").strip()
                vendor = input(" Enter vendor name: ").strip()

                products.append({
                    'name': name,
                    'brand': brand,
                    'quantity': qty,
                    'cost_price': price,
                    'country': country
                })

                items.append({
                    'name': name,
                    'brand': brand,
                    'quantity': qty,
                    'price': price,
                    'vendor': vendor
                })
            except ValueError:
                print("️ Please enter valid numbers.")
        else:
            print(" Invalid choice.")

    if items:
        # Calculate VAT for the restock items
        total_price = 0
        total_vat = 0
        for item in items:
            line_total = item['quantity'] * item['price']
            total_price += line_total
            vat_amount = calculate_vat(line_total)
            total_vat += vat_amount

        write_invoice(items, {}, items[0]['vendor'], is_sale=False, total_vat=total_vat, total_price=total_price)
        write_products(products)
        print("✅ Restocking complete and invoice saved.")
