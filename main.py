from Operation import sell_product, restock_product, display_products
from Read import read_products
# Main function to drive the inventory management system
def main():
    while True:
        # Displaying the main menu
        print("\n=========  WeCare Inventory Management =========")
        print("1.  Display All Products")
        print("2.  Sell Products")
        print("3.  Restock Products")
        print("0.  Exit")
        # Taking user's choice
        choice = input("Enter your choice: ")

        # Handling user options
        if choice == '1':
            products = read_products()
            display_products(products)
        elif choice == '2':
            sell_product()
        elif choice == '3':
            restock_product()
        elif choice == '0':
            print(" Exiting the system. Goodbye!")
            break
        else:
            # Invalid input handling
            print(" Invalid input. Please select a valid option.")


# Ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
