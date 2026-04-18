from datetime import datetime

def write_invoice(items, free_items, name, is_sale=True, total_vat=0, total_price=0):
    """Write the invoice to a file and display it in the terminal, adding VAT and total price."""
    filename = f"invoice_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

    # Prepare invoice header
    invoice_header = ""
    if is_sale:
        invoice_header = f" Sale Invoice for Customer: {name}\n"
    else:
        invoice_header = f" Restock Invoice for Vendor: {name}\n"

    date_str = f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    # Terminal output
    print(invoice_header)
    print(date_str)

    # Prepare invoice content
    if is_sale:
        header = "{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}\n".format(
            "Product", "Brand", "Qty Sold", "Free Qty", "Price", "Total", "VAT"
        )
        separator = "-" * 85 + "\n"
        print(header)
        print(separator)

        total = 0
        for item in items:
            free = free_items.get(item['name'], 0)
            line_total = item['quantity'] * item['price']
            vat_amount = line_total * 0.13  # 13% VAT
            item_line = "{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}\n".format(
                item['name'], item['brand'], item['quantity'], free, int(item['price']),
                int(line_total), int(vat_amount)
            )
            print(item_line)
            total += line_total
        print("-" * 85)
        print(f"Total Amount (excluding free items): Rs. {int(total)}")
        print(f"Total VAT: Rs. {int(total_vat)}")
        print(f"Total Price (including VAT): Rs. {int(total_price)}")

    else:
        header = "{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}\n".format(
            "Product", "Brand", "Quantity", "Price", "Total", "VAT"
        )
        separator = "-" * 80 + "\n"
        print(header)
        print(separator)

        total = 0
        for item in items:
            line_total = item['quantity'] * item['price']
            vat_amount = line_total * 0.13  # 13% VAT
            item_line = "{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}\n".format(
                item['name'], item['brand'], item['quantity'], int(item['price']),
                int(line_total), int(vat_amount)
            )
            print(item_line)
            total += line_total
        print("-" * 80)
        print(f"Total Restocking Cost (excluding VAT): Rs. {int(total)}")
        print(f"Total VAT: Rs. {int(total_vat)}")
        print(f"Total Cost (including VAT): Rs. {int(total_price)}")

    # Save the invoice to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(invoice_header)
        file.write(date_str)

        if is_sale:
            file.write(header)
            file.write(separator)

            total = 0
            for item in items:
                free = free_items.get(item['name'], 0)
                line_total = item['quantity'] * item['price']
                vat_amount = line_total * 0.13  # 13% VAT
                file.write("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}\n".format(
                    item['name'], item['brand'], item['quantity'], free, int(item['price']),
                    int(line_total), int(vat_amount)
                ))
                total += line_total
            file.write("-" * 85 + "\n")
            file.write(f"Total Amount (excluding free items): Rs. {int(total)}\n")
            file.write(f"Total VAT: Rs. {int(total_vat)}\n")
            file.write(f"Total Price (including VAT): Rs. {int(total_price)}\n")

        else:
            file.write(header)
            file.write(separator)

            total = 0
            for item in items:
                line_total = item['quantity'] * item['price']
                vat_amount = line_total * 0.13  # 13% VAT
                file.write("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}\n".format(
                    item['name'], item['brand'], item['quantity'], int(item['price']),
                    int(line_total), int(vat_amount)
                ))
                total += line_total
            file.write("-" * 80 + "\n")
            file.write(f"Total Restocking Cost (excluding VAT): Rs. {int(total)}\n")
            file.write(f"Total VAT: Rs. {int(total_vat)}\n")
            file.write(f"Total Cost (including VAT): Rs. {int(total_price)}\n")

    print(f"Invoice saved as: {filename}")


def write_products(products):
    """Write the updated products list to the products file."""
    with open("products.txt", "w") as file:
        for p in products:
            file.write(f"{p['name']},{p['brand']},{p['quantity']},{p['cost_price']},{p['country']}\n")
